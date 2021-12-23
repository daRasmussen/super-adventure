from aocd import submit, get_data

data = get_data(day=24, year=2018)
ans = ''

import re
import itertools
from copy import deepcopy
from enum import auto, Enum
from dataclasses import dataclass
from typing import FrozenSet

class Army(Enum):
    IMMUNE_SYSTEM = auto()
    INFECTION = auto()

class Damage(Enum):
    COLD = auto()
    FIRE = auto()
    SLASHING = auto()
    RADIATION = auto()
    BLUDGEONING = auto()

class Stalemate(Exception):
    pass

@dataclass
class Unit:
    army: Army
    count: int
    hp: int
    damage: int
    attack: Damage
    initiative: int
    weaknesses: FrozenSet[Damage] = frozenset()
    immunities: FrozenSet[Damage] = frozenset()

    def __hash__(self): return id(self)  # allow using units in dictionaries

    @classmethod
    def parse(cls, army, val):
        (count, hp, mods, damage, attack, initiative) = re.match(
            r'(\d+) units each with (\d+) hit points(?: \((.*?)\))?'
            r' with an attack that does (\d+) (\w+) damage at initiative (\d+)'
        , val).groups()

        kwargs = {}

        if mods:
            for mod in mods.split('; '):
                modifier, _, types = mod.split(' ', 2)
                damages = frozenset(Damage[damage.upper()] for damage in types.split(', '))
                if modifier == 'weak':
                    kwargs['weaknesses'] = damages
                elif modifier == 'immune':
                    kwargs['immunities'] = damages

        return cls(army=army, count=int(count), hp=int(hp), damage=int(damage),
            attack=Damage[attack.upper()], initiative=int(initiative), **kwargs)

    @property
    def effective_power(self):
        return self.count * self.damage

    def damage_dealt(self, other):
        if self.attack in other.immunities:
            return 0
        elif self.attack in other.weaknesses:
            return self.effective_power * 2
        else:
            return self.effective_power

def round(armies):
    targets = {}
    attacking = {}

    for group in sorted(armies, key=lambda group: (group.effective_power, group.initiative), reverse=True):
        if group.count <= 0:
            continue

        enemies = [enemy for enemy in armies if enemy.army != group.army]
        enemies = sorted(enemies, key=lambda enemy: (group.damage_dealt(enemy), enemy.effective_power, enemy.initiative), reverse=True)
        target = next((enemy for enemy in enemies if enemy.count > 0 and group.damage_dealt(enemy) and enemy not in targets), None)

        if not target:
            continue

        targets[target] = group
        attacking[group] = target

    stalemate = True

    for group in sorted(armies, key=lambda group: group.initiative, reverse=True):
        if group.count > 0 and attacking.get(group):
            target = attacking[group]
            killed = min(group.damage_dealt(target) // target.hp, target.count)

            if killed:
                target.count -= killed
                stalemate = False

    if stalemate:
        raise Stalemate()

    return armies

def fight(armies, boost=0):
    armies = deepcopy(armies)

    for group in armies:
        if group.army == Army.IMMUNE_SYSTEM:
            group.damage += boost

    while all(any(group.count for group in armies if group.army == army) for army in Army):
        armies = round(armies)

    return armies

armies = []

#for group in open('inputs/day24').read().split('\n\n'):
for group in data.split("\n\n"):
    name, *units = group.splitlines()

    army = Army[name.replace(':', '').replace(' ', '_').upper()]

    armies.extend(Unit.parse(army, line) for line in units)

result = fight(armies)

print('part 1:', sum(group.count for group in result if group.army == Army.INFECTION))

for boost in itertools.count(1):
    try:
        result = fight(armies, boost=boost)
    except Stalemate:
        continue
    else:
        if all(group.count == 0 for group in result if group.army == Army.INFECTION):
            break

ans = sum(group.count for group in result if group.army == Army.IMMUNE_SYSTEM)
print(ans) 
submit(ans, part='b', day=24, year=2018)

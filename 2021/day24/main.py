from typing import List, Tuple, Union
from aocd import submit, get_data

data = get_data(day=24, year=2021)
ans = ''

global CACHE
CACHE = {}

class Function:
  def __init__(self, cmds: List[str], optimized: bool = False) -> None:
    self.cmds, self.specials = self.__parse_cmds(cmds)
    self.registers = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    self.optimized = optimized

  def __parse_cmds(self, cmds: List[str]) -> Tuple[str, str, Union[str, int]]:
    parsed = []
    specials = [0, 0, 0]
    for cmd in cmds:
      if cmd.startswith("inp"):
        cmd += " 0"
      op, a, b = cmd.split(" ")
      if b[0] == "-" or b[0].isdigit():
        b = int(b)

      parsed.append((op, a, b))

      if cmd.startswith("div z"):
        specials[0] = b
      elif cmd.startswith("add x"):
        specials[1] = b
      elif cmd.startswith("add y"):
        specials[2] = b

    return parsed, specials

  def run(self, io: int, w: int, x: int, y: int, z: int) -> Tuple[bool, int, int, int, int]:
    if self.optimized:
      w = io
      x = int((z % 26) + self.specials[1] != w)
      z //= self.specials[0]

      if x == 1:
        z *= 25 * x + 1
        z += (w + self.specials[2]) * x

      return True, io, 0, 0, z

    success = False
    self.registers = {'w': w, 'x': x, 'y': y, 'z': z}

    for op, a, b in self.cmds:
      if not isinstance(b, int):
        b = self.registers[b]

      if op == "inp":
        self.registers[a] = io

      elif op == "add":
        self.registers[a] += b

      elif op == "mul":
        self.registers[a] *= b

      elif op == "div":
        if b == 0:
          break
        self.registers[a] //= b

      elif op == "mod":
        if self.registers[a] < 0 or b <= 0:
          break
        self.registers[a] %= b

      elif op == "eql":
        self.registers[a] = 1 if self.registers[a] == b else 0

    else:
      success = True

    return success, self.registers['w'], self.registers['x'], self.registers['y'], self.registers['z']


def find_model(funcs: List[Function], func_idx: int, z: int, val: int, lowest: bool = False) -> int:
  if (func_idx, z) in CACHE:
    return CACHE[func_idx, z]

  if func_idx == len(funcs):
    return val if z == 0 else 0

  numbers = range(1, 10)
  if not lowest: numbers = reversed(numbers)

  model = 0
  for n in numbers:
    result, _, _, _, nz = funcs[func_idx].run(n, 0, 0, 0, z)

    # we can only reduce a value by a factor of 26 per function
    # if our value is greater than 26^(# remaining functions),
    # we cannot ever reduce it to zero
    if not result or nz >= 26 ** (len(funcs) - func_idx):
      continue

    model = find_model(funcs, func_idx + 1, nz, val * 10 + n, lowest)
    if model != 0:
      break

  CACHE[func_idx, z] = model
  return model


def read_input() -> List[Function]:
  funcs = []
  cmds = []
  for line in data.splitlines():
    if line.startswith("inp") and cmds:
      funcs.append(Function(cmds, True))
      cmds = []
    cmds.append(line.strip())
  else:
    if cmds:
      funcs.append(Function(cmds, True))
  return funcs

functions = read_input()
CACHE = {}
model = find_model(functions, 0, 0, 0)
ans = model
print(ans)
submit(ans, part='a', day=24, year=2021)
# submit(ans, part='b', day=24, year=2021)

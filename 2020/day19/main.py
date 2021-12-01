with open('data.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]
    rules_data = data[:data.index('')]
    messages = data[data.index('')+1:]
# parse out the rules
rules = {}
for line in rules_data:
    line = line.split(': ')
    rule_num = int(line[0])
    options = []
    options_strings = line[1].split(' | ')
    for option_string in options_strings:
        options.append(option_string.split())
    rules[rule_num] = options
string_rules = {}
def solve1(rule_num):
    rule_options = rules[rule_num]
    if ['"a"'] in rule_options:
        return ['a']
    if ['"b"'] in rule_options:
        return ['b']
    if rule_num in string_rules:
        return string_rules[rule_num]
    final = []
    for rule_option in rule_options:
        string_options = []
        for rule in rule_option:
            sub_options = solve1(int(rule))
            if len(string_options) == 0:
                string_options = sub_options.copy()
            else:
                combined_options = []
                for sub_option in sub_options:
                    for string_option in string_options:
                        combined_options.append(string_option+sub_option)
                string_options = combined_options.copy()
        final += string_options
    string_rules[rule_num] = final
    return final

all_possibilities = solve1(0)
all_set = set()
for a in all_possibilities:
    all_set.add(a)

count = 0
for message in messages:
    if message in all_set:
        count += 1
print(count)

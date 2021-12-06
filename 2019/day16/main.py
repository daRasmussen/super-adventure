def read_integers(file: str) -> list:
    with open(file) as f:
        return list(map(int, [x for x in f.read().strip()]))

def fft(digits: list, target_phases: int) -> list:
    output = digits.copy()
    base_pat = [0, 1, 0, -1]
    for _ in range(0, target_phases):
        phase_output = []
        for i in range(0, len(output)):
            base_index = 0
            reps = i + 1
            digit_calc = 0
            count_reps = 1
            for _, digit in enumerate(output):
                if count_reps == reps:
                    count_reps = 0
                    if base_index == len(base_pat) - 1:
                        base_index = 0
                    else:
                        base_index += 1
                digit_calc += digit * base_pat[base_index]
                count_reps += 1
            phase_output.append(digit_calc % 10 if digit_calc >= 0 else abs(digit_calc % -10))
        output = phase_output
    return output


"""
    Calculates FFT for the second half of the input list [n/2, n].
    For a digit at position i, its new value is calculated as (A[i] + A[i+1] + ... + A[n]) % 10
"""
def fft_second_half(digits: list, target_phases: int) -> list:
    output = digits.copy()
    half_len = len(digits) // 2
    for _ in range(0, target_phases):
        phases_output = [0] * len(digits)
        right_array_sum = sum(output[half_len:])
        for i in range(half_len, len(output)):
            if i != 0:
                right_array_sum -= output[i - 1]
            phases_output[i] = right_array_sum % 10
        output = phases_output
    return output

# Part 1
data = read_integers("data.txt")
target_phases = 100
output = fft(data, target_phases)
print("".join(map(str, output[:8])))
print('\n PART 2')
# Part 2 
def read(name, strip = True):
    with open(name) as f:
        content = f.readlines()
    if strip:
        return [x.strip() for x in content]
    return content

def solve():
    input_values = read("data.txt")[0]
    offset = int(input_values[:7])
    elements = [int(num) for _ in range(10000) for num in input_values][offset:]
    for _ in range(100):
        for i in range(-2, -len(elements)-1, -1):
            elements[i] = (elements[i] + elements[i+1]) % 10
    return "".join([str(x) for x in elements[:8]])

r = solve()
print(f"Solution: {r}")




from intcode import Intcode


def read_program(file) -> list:
    with open(file) as f:
        return list(map(int, f.read().split(",")))

def get_num_blocks(program: list) -> int:
    block_title_count = 0
    vm = Intcode(program)
    while True:
        x = vm.run()
        if x is None:
            break
        vm.run()
        title_id = vm.run() # ignore y value
        block_title_count += 1 if title_id == 2 else 0
    return block_title_count

# part 1 
data = read_program("data.txt")
r = get_num_blocks(data)
print(r)

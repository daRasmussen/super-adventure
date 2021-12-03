import sys 


def get_image_pixels(file):
    with open(file) as f:
        return list(map(int, f.read().strip()))

def get_layer_with_fewest_zeros(freq_list):
    result = -1
    min_zeros = sys.maxsize
    for freq in freq_list:
        if freq[0] < min_zeros:
            min_zeros = freq[0]
            result = freq
    return result

def compute_frequencies(pixels, width, height):
    layer = -1
    freq_list = [] 
    for i, pixel in enumerate(pixels):
        if i % (width * height) == 0:
            layer += 1
            freq_list.append([0] * 10)
        freq_list[layer][pixel] += 1
    return freq_list

def compute_image(pixels, width, height):
    num_layers = int(len(pixels) / (width * height))
    message = [] 
    for row in range(0, height):
        line_str = []
        for col in range(0, width):
            color = 2 # transparent
            for l in range(0, num_layers):
                color = pixels[(l * width * height) + (width * row) + col]
                if color == 0 or color == 1: # black or white
                    break
            line_str.append("X" if color == 1 else " ")
        message.append("".join(line_str))
    return "\n".join(message)

# part 1
w, h  = 25, 6
images = get_image_pixels("data.txt")
r = get_layer_with_fewest_zeros(compute_frequencies(images, w, h))
print(r[1] * r[2])

# part 2
r = compute_image(images, w, h)
print(r)

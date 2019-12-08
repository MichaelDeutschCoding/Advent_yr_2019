import operator

with open('day8_input.txt') as f:
    digits = f.read()

layers = []

for i in range(0, len(digits), 150):
    layers.append(digits[i:i+150])


num_zeros = [layer.count('0') for layer in layers]

min_idx, min_val = min(enumerate(num_zeros), key=operator.itemgetter(1))
print(layers[min_idx].count('1') * layers[min_idx].count('2'))

image = []

for i in range(150):
    for layer in layers:
        if layer[i] == '2':
            continue
        if layer[i] == '0':
            image.append(' ')
            break
        else:
            image.append('*')
            break

for i in range(0, 150, 25):
    print(''.join(image[i:i+25]))
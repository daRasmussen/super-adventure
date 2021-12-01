with open('data.txt') as file:
    data = file.readlines()
    card_key = int(data[0].strip())
    door_key = int(data[1].strip())

card_count = 0
x = 1
while x != card_key:
    card_count += 1
    x = (x * 7) % 20201227
encryption_key = 1
for _ in range(card_count):
    encryption_key = (encryption_key * door_key) % 20201227
print(encryption_key)


from random import randint
name = []
for i in list(range(15)):
    name.append(randint(-6,50))
print("первоначальная последовательность:", name)
sum = 0
kolvo = 0
sra = 0
for i in name:
    if i % 2 == 0:
        index = name.index(i)
        name[index] = 'вот он!'
print('нашёлся кратный 2: ', name)
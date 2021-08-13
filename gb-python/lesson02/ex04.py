string = input("Введи строку из нескольких слов, разделённых пробелами ")
word = []
num = 1
for element in range(string.count(' ') + 1):
    word = string.split()
    if len(str(word)) <= 10:
        print(f" {num} {word [element]}")
        num += 1
    else:
        print(f" {num} {word [element] [0:10]}")
        num += 1
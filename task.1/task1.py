import re
a = input()
mas1 = []
mas2 = []
k = re.findall(r'\d+', a)
k = [int(i) for i in k]
for i in range(len(a)) :
    if a[i].isdigit() == True:
        mas1.append(int(a[i]))
a = re.sub("[0-9]", "", a)
print("Рядок без цифр:\n", a, sep='')
print("Масив цифр:\n", mas1, sep='')
a = ' '.join(map(lambda s: s[:-1]+s[-1].upper(), a.title().split()))
print("Перша і остання буква велика:\n", a, sep='')
max_num = max(k)
index_of_k = k.index(max_num)
print("Максимальне значення:", max_num)
for i in range(len(k)):
    if i != index_of_k:
        t = k[i] ** i
        mas2.insert(i, t)
print("Масив чисел в степені індекса:\n", mas2)

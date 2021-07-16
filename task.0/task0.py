import random
mas1=[]
mas2=[]
j=0
l=0
for i in range(30):
    mas1.append(random.randint(-100,100))
print(mas1)
for i in range(30):
    if mas1[i]==max(mas1):
        j=i
print("Максимальний елемент:",max(mas1), "Індекс:", j)
for i in range(30):
    if (mas1[i]%2)!=0:
        mas2.append(mas1[i])
        l=1
if l==0:
    print("Немає відьємних чисел")
print("Список відьємних чисел:\n",sorted(mas2,reverse=True))

n = input("Введите число элементов массива: ")
try:
    n = int(n)
except:
    print("Введено неверное значение")
    exit()

arr = input("Введите элементы массива через пробел: ").split()
zero_index = []
for i in range(n):
    if arr[i] == '0':
        zero_index.append(i)
result = []
for i in range(n):
    zero_temp = []
    for elem in zero_index:
        zero_temp.append(abs(elem - i))
    result.append(min(zero_temp))
print("Расстояния до ближайшего нуля:", *result)

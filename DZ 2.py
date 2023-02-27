# n = int(input('Количество монет:'))
# gerb = 0
# rechka = 0
# for i in range(n):
#     mon = int(input('1 герб, 2 решка:'))
#     if mon == 1:
#         gerb+=1
#     else: rechka+=1
#     print(min(rechka,gerb))



# from math import sqrt
# s = int(input('Введите сумму:'))
# p = int(input('Введите произведение:'))
# x = s/2 - (sqrt(-4 * p+s**2)/2)
# y = s - x
# print(x, y)



n = int(input())
s = 0
while 2**s<=n:
    print(2**s)
    s+=1
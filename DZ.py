n = int(input('Введите трех значное число:'))
b = n%10
a = n//10%10
c = n//100%10
print(b+a+c)



n = int(input('Введите сколько корабликов:'))
d = n/6
print(d)
print( "корабликов сделал Сережа")
print(d)
print( "корабликов сделал Петя")
c = d*4
print(c)
print( "корабликов сделала Катя")



n = int(input('Введите номер билета:'))
a = n%10
b = n//10%10
c = n//100%10
d = n//1000%10
e = n//10000%10
f = n//100000%10
print((a+b+c)==(d+e+f))



n = int(input())
m = int(input())
k = int(input())
if (k%n==0 or k%m==0)
print('yes')
else: 
print('no')
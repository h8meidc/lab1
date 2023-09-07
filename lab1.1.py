a = int(input ("Введіть а: "))
while (a < 1 or a > 100):
    print("Введіть правельне число")
      
    a = int(input ("Введіть а: "))
    
b = int(input ("Введіть b: "))

while (b < 1 or b > 100):
    print("Введіть правельне число")
    b = int(input ("Введіть ще раз b: "))

if a > b:

    r = 2*a/b+1

elif a == b:

    r = -445

else:

    r = (b+5) / a

print("Результат обчислення виразу: " , r)
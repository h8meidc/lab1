n = int(input("Введіть кількість поверхів піраміди (від 1 до 9): "))
while(n<=1 or n>=9):
    n = int(input("Введіть кількість поверхів піраміди (від 1 до 9): "))
k=n
for i in range(1, n + 1):
    num = k
    for j in range(1, n + 1):
        if j <= i:
            print(num, end=" ")
        else:
            print(" ", end=" ")
        num += 1
        
    print("\n")
    k-=1
print("")

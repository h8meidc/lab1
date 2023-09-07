n = int(input("Введіть кількість поверхів піраміди (від 1 до 9): "))

for i in range(1, n + 1):
  num = 5
  for j in range(1, n + 1):
    if j <= i:
      print(num, end=" ")
    else:
      print(" ", end=" ")
    num -= 1
  print("\n")
print("")

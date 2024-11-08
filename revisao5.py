num1 = int(input("Digite três numeros:"))
num2 = int(input(""))
num3 = int(input(""))

if num1 > num2 and num3:
    print(num1,"Esse é maior")
elif num2 > num3 and num1:
    print(num2,"Esse é maior")
elif num3 > num1 and num2:
    print(num3,"Esse é maior")

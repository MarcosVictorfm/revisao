salario = float(input("Digite o valor do seu salario: "))
if salario <= 280:
    aumento = salario * 0.20
    novo_salario= (aumento + salario)
    print(novo_salario,"com reajuste de 20%.Valor sem o reajuste",salario)

elif salario >280 and salario<= 700:
    aumento = salario * 0.15
    novo_salario= (aumento + salario)
    print(novo_salario,"com reajuste de 15%.Valor sem o reajuste",salario)

elif salario >700 and salario<= 1500:
    aumento = salario * 0.10
    novo_salario= (aumento + salario)
    print(novo_salario,"com reajuste de 10%.Valor sem o reajuste",salario)

if salario >1500:
    aumento = salario * 0.5
    novo_salario= (aumento + salario)
    print(novo_salario,"com reajuste de 5%.Valor sem o reajuste",salario)


     

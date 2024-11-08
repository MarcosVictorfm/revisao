turno = input("Digite apenas a primeira letra do turno que vc trabalha (Matutino,Vespertino,Noturno:")
if turno == "m" or turno =="M":
    print("Bom dia")
elif turno == "v" or turno =="V":
    print("Boa tarde")
elif turno == "n" or turno =="N":
    print("Boa noite")
else:
    print("letra invalida")
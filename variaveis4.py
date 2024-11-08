alimentos = ["maçã","Arroz","Feijão"]
categoria = ("Grãos","Frutas","Legumes")
pessoa = {"nome":"Paula","Idade":"38","Altura": "1.65"}

print (alimentos)
print (type(alimentos))
print (len(alimentos))
# adicionar mais um alimento 
alimentos.append("Macarrão")
print (alimentos)
print (len(alimentos))

print (categoria)
print (type(categoria))
print (len(categoria))

print (pessoa)
print (type(pessoa))
print (len(pessoa))
#Adicionar um item a pessoa 
pessoa["email"]="paulo@gmail.com"
print(pessoa)
print(len(pessoa))
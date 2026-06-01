# entrada de dados
# idade juliana
# idade cris
idade_juliana = int(input())
idade_cris = int(input())

#processamento
# True se ambos forem maior de idade 
# <exp1> juliana é maior de idade
# <exp2> cris é maior de idade
# <exp1> or <exp2>
# False em qualquer outro caso
pode_entrar = (idade_juliana >= 17 or idade_cris >=17)

#saida
print (pode_entrar)
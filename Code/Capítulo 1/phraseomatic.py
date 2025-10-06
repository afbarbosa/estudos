import random

verbos = ['comer','correr','jogar','dormir','trabalhar','criar','chorar','sorrir','escrever']
adjetivos = ['belo','feio','bom','mau','experiente','fraco','forte','rapido','lerdo']
substantivos = ['computador','carteira','livro','video game','trabalho','jornal','futebol','bolo','cama']

verbo = random.choice(verbos)
adjetivo = random.choice(adjetivos)
substantivo = random.choice(substantivos)
frase = verbo + " " + adjetivo + " " + substantivo
print(frase)

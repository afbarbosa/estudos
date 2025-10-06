name = input('Qual o nome do seu cachorro?')
age = int(input('Qual a idade do seu cachorro?'))
def calculator(name,age):
    human_age = 7*age
    return print('A idade do '+name+' é '+str(human_age)+' no tempo humano')
calculator(name,age)

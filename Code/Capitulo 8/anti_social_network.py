users = {}
def insert_user():
    global users
    name = input("Qual o seu nome? ")
    email = input("Qual o seu e-mail? ")
    gender = input("Qual o seu gênero? ")
    age = input("Qual a sua idade? ")
    friends = []
    add = input("Deseja adicionar um amigo? Sim ou Não ").lower()
    while(add == "sim"):
        friends.append(input("Nome do amigo: "))
        add = input("Deseja adicionar outro amigo? Sim ou Não ").lower()
    atributes = {
            'email':email,
            'gender':gender,
            'age':age,
            'friends':friends
        }
    users[name] = atributes

def average_age(name):
    user = users[name]
    soma = int()
    for f in user['friends']:
        friend = users[f]
        soma = soma + friend['age']

    average = soma/len(user['friends'])
    return average

def most_anti_social():
    global users
    max = 100
    for name in users:
        user = users[name]
        friends = user['friends']
        if len(friends) < max:
            most_anti_social = name
            max=len(friends)
    print('The most anti social user is', most_anti_social)

new_user = input("Quer se cadastrar? Sim ou Não ").lower()
while(new_user == "sim"):
    insert_user()
    new_user = input("Quer cadastrar outra conta? Sim ou Não ").lower()

print("obrigado")        
users['Kim'] = {'email' : 'kim@oreilly.com','gender': 'f', 'age': 27, 'friends': ['John', 'Josh']}
users['John'] = {'email' : 'john@abc.com','gender': 'm', 'age': 24, 'friends': ['Kim', 'Josh']}
users['Josh'] = {'email' : 'josh@wickedlysmart.com','gender': 'm', 'age': 32, 'friends': ['Kim']}

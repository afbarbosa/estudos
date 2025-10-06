def get_attribute(query,default):
    question = query + ' [' + default + ']? '
    answer = input(question)
    if (answer == ''):
        answer = default
    print('You chose', answer)
    return answer

hair =  get_attribute('Qual a cor do seu cabelo', 'Castanho')
hair_length = get_attribute('Seu cabelo é longo ou curto','Curto')
eye = get_attribute('Qual a cor dos olhos?','Azul')
gender = get_attribute('Qual seu genero','Homem')
glasses = get_attribute('Usa óculos','não')
barba = get_attribute('Tem barba','não')

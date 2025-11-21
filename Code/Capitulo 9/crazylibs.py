import sys
def make_crazy_lib(caminho):
    try:
        arquivo = open(caminho,'r')
        texto = ''
        for linha in arquivo:
            texto = texto + processador_linha(linha)
        arquivo.close()

        return texto
    except FileNotFoundError:
        print("Ooops, não encontrei o arquivo mencionado")
    except IsADirectoryError:
        print("Ei, isso é uma pasta e não um arquivo")
    except:
        print("Desculpa, não consegui abir", caminho)
def processador_linha(linha):
    linha_processada = ''

    palavras = linha.split()
    for palavra in palavras:
        if palavra.strip('.,;?/|:') in ['NOUN', 'ADJECTIVE', 'VERB_ING','VERB']:
            resposta = input('Escreva ' + palavra.strip('.,;?/|:') )
            if palavra[-1] in '.,;?/|:!':
                linha_processada = linha_processada + resposta + palavra[-1]+' '
            else:
                linha_processada = linha_processada + resposta + ' '
        else:
            linha_processada = linha_processada + palavra + ' '
    return linha_processada + '\n'
def save_crazy_lib(caminho, texto):
    try:
        arquivo = open(caminho, 'w')
        arquivo.write(texto)
        arquivo.close()
    except:
        print("Foi mal, não consegui criar", caminho)
def main():
    if len(sys.argv) != 2:
        print("crazy.pay <filename>")
    else: 
        caminho = 'lib.txt'
        lib = make_crazy_lib(caminho)
        if(lib != None):
            save_crazy_lib('crazy_' + caminho, lib)

if __name__ == '__main__':
    main()

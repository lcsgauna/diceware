from random import randrange
import json

filename = 'diceware.json'
dados = []
numero_de_palavras = 5 * 5

with open(filename,'r') as read_file:
    data = json.load(read_file)
    dict_data = dict(data)
    
def gerarNumeros(dados,numeroDePalavras):
    while(len(dados)!=numeroDePalavras):
        dados.append(randrange(1,7))
   
    strDados = ''.join(map(str,dados))
    return [strDados[i:i+5] for i in range(0,len(strDados),5)]

def gerarPalavras(palavras):
   return ''.join(map(str.capitalize,palavras))
    
numeros_gerados = gerarNumeros(dados,numero_de_palavras)
palavras_list = [dict_data.get(f'{numeros}') for numeros in numeros_gerados for keys in dict_data.keys() if numeros == keys ]
senha_gerada = gerarPalavras(palavras_list)

print(palavras_list)
print(senha_gerada)    


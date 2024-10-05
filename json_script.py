import json
#import pdb

keep_inserting = True

def insert_descricao() -> str:
    descricao = input("Insira a descrição do produto:")
    return descricao

def insert_valor() -> float:
    try:
        valor = float(input("Insira o valor do produto:"))
    except ValueError:
        print("Formato errado, tente novamente!")
        insert_valor()
    return valor

def insert_tipo_embalagem() -> str:
    tipo_embalagem = input("Insira o tipo de embalagem:")
    return tipo_embalagem

def inserting(json_length: int = 0):
    keep_inserting = eval(input("Deseja cadastrar um novo produto(True/False)?"))
    if json_length >= 5:
        return keep_inserting
    else:
        keep_inserting = True
        print("Não atingimos o ínimo de 5 inserções, continue a inserção")
        return keep_inserting

json_final = []
while keep_inserting:
    descricao = insert_descricao()
    valor = insert_valor()
    tipo_embalagem = insert_tipo_embalagem()
    imposto = lambda x: round(x * .18,2)
    temp_json = {"Descricao do produto": descricao,
                 "Valor": valor,
                 "Tipo de embalagem": tipo_embalagem,
                 "Imposto": imposto(valor)}
    json_final.append(temp_json)
    keep_inserting = inserting(json_length = len(json_final))
    #pdb.set_trace()


with open('1_5_arquivo_produto.json', 'w') as outfile:
    json.dump(json_final, outfile)
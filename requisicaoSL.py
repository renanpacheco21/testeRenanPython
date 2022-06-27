import json
from time import sleep

import requests

limit = 10 #limite por pagina
offset = 0 #inicio
pagina = 0
hasNext = True #paginas depois
listaAlterar = []

while hasNext:
    url = 'https://compras.betha.cloud/compras-services/api/formas-julgamento'
    lote = {}
    cabecalho = {
        'Authorization': 'Bearer c6171025-a595-45c1-9dbe-55b28e39622d'
    }

    resposta = requests.request("GET", url, headers=cabecalho, data=lote)
    resposta = resposta.json()
    #print(resposta)
    pagina = pagina + 1
    offset = limit * pagina
    hasNext = resposta['hasNext']

    for i in resposta['content']:
        if 'descricao' in i and i ['descricao'] == '15 dias':
            listaAlterar.append(i)


print(listaAlterar)
#
# listaLotes = []
#
# for j in listaAlterar:
#     url = 'https://compras.betha.cloud/compras-services/api/formas-julgamento'
#
#     j['descricao'] = '15 dias - Teste'
#     j.pop('version') #remover campo para envio
#     lote = json.dumps([{
#         'idIntegracao': 'teste123',
#         'conteudo': j
#     }])
#     cabecalho = {
#         'Authorization': 'Bearer c6171025-a595-45c1-9dbe-55b28e39622d',
#         'Content-Type': 'application/json'
#     }
#     resposta = requests.request("POST", url, headers=cabecalho, data=lote)
#     resposta = resposta.json()
#     #print(resposta)
#
#     if 'id' in resposta:
#         listaLotes.append(resposta['id'])
#     else:
#         print(f"Deu erro! {resposta['mensagem']}")
#
# print(listaLotes)
#
# for k in listaLotes:
#     situacao = 'AGUARDANDO_EXECUCAO'
#
#     while situacao in ('AGUARDANDO_EXECUCAO', 'EXECUTANDO'):
#         url = f'https://pessoal.cloud.betha.com.br/service-layer/v1/api/lote/lotes/{k}'
#         lote = {}
#         cabecalho = {
#             'Authorization': 'Bearer c6171025-a595-45c1-9dbe-55b28e39622d',
#             'Content-Type': 'application/json'
#         }
#
#         resposta = requests.request("GET", url, headers=cabecalho, data=lote)
#         resposta = resposta.json()
#         situacao = resposta['situacao']
#         print(situacao)
#         sleep(5) #intervalo de tempo de pesquisa -segundos-
#
# print(resposta['retorno'][0]['situacao'])
# print(resposta['retorno'][0]['mensagem'])
# '''
# Codigo que eu uso para enviar respotas manualmente p lucio
# '''

# import requests
# import json

# data = {
#     "identifier": '35611694000188',
#     "name": ' 49 educaçao'
# }
# print(data)
# json_data = json.dumps(data)
# url = "https://inscricao.anprotec.org.br/access/new_associate.php"
# response = requests.post(url, data=json_data)

# if response.status_code == 200:
#     print("JSON enviado com sucesso!")
#     print(response.text)
# else:
#     print("Erro ao enviar o JSON para a API.")
#     print("Código de status:", response.status_code)
#     print(response.text)
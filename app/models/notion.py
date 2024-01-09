from app.models.config import loadHeaderNotion
import requests
import json

class DatabaseNotion:
    def __init__(self, databaseId):
        self.databaseId = databaseId

    def get(self):
        url = f"https://api.notion.com/v1/databases/{self.databaseId}"

        response = requests.get(url, headers=loadHeaderNotion())
        json_data = json.loads(response.text)
        if response.status_code != 200:
            error = {
                "description":"Ocorreu um erro durante a execução da sua query",
                "status_code": response.status_code
            }
            raise Exception(error)
        
        return json_data

    def post(self, payload):
        has_more = True
        first_query = True
        results= []

        base_url = f'https://api.notion.com/v1/databases/{self.databaseId}/query'

        while(has_more):
            if not first_query:
                payload['start_cursor'] = start_cursor

            response = requests.post(base_url, json=payload, headers=loadHeaderNotion())

            # Lançar exceção caso ocorra um erro na solicitação HTTP
            if response.status_code != 200:
                error = {
                    "description":"Ocorreu um erro durante a execução da sua query",
                    "status_code": response.status_code,
                    "erro": response.text
                }
                raise Exception(error)

            try:
                json_data = json.loads(response.text)
                results.extend(json_data['results'])
                has_more = json_data['has_more']
                start_cursor = json_data['next_cursor']
                first_query = False

            except Exception as error:
                # Lançar exceção caso ocorra um erro na análise do JSON
                error = {
                    "description":"Erro na análise do JSON",
                    "status_code": 500
                }
                raise Exception(error)

        json_data['results'] = results

        return json_data

class NotionPage:
    def __init__(self, databaseId, pageId):
        self.databaseId = databaseId
        self.pageId = pageId

    def __repr__(self):
        if self.databaseId != '':
            return f"Database id is {self.databaseId}"
        else:
            return f"Page id is {self.pageId}"
    
    def get(self):
        url = f"https://api.notion.com/v1/pages/{self.pageId}"

        response = requests.get(url, headers=loadHeaderNotion())
        data = json.loads(response.text)

        return data
    
    def put(self, payload):
        url = f"https://api.notion.com/v1/pages/{self.pageId}"

        response = requests.patch(url, json=payload, headers=loadHeaderNotion())
        data = json.loads(response.text)

        return data
    
    def post(self, payload):
        url = "https://api.notion.com/v1/pages"
        payload['parent']['database_id'] = self.databaseId

        response = requests.post(url, json=payload, headers=loadHeaderNotion())
        data = json.loads(response.text)

        return data
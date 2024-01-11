from dotenv import load_dotenv
import pygsheets
import os

def load_environment_variables(variable_name):
    load_dotenv()
    LOADED_VARIABLE = os.getenv(variable_name)
    return LOADED_VARIABLE

def loadHeaderNotion():
    # Credenciais da API do Notion
    NOTION_SECRETS = load_environment_variables("NOTION_SECRETS_AMEDIR")
    
    headers = {
        "accept": "application/json",
        "Authorization":NOTION_SECRETS, 
        "Notion-Version": "2022-06-28"
    }

    return headers

def setFieldsNotion(data):
    field_extractors = {
        'rich_text': lambda result: result[0]['text']['content'] if result else None,
        'title': lambda result: result[0]['text']['content'] if result else None,
        'select': lambda result: result['name'] if result else None,
        'relation': lambda result: result,
        'url': lambda result: result,
        'multi_select': lambda result: result[0]['name'] if result else None,
        'number': lambda result: result,
        'email': lambda result: result,
        'phone_number': lambda result: result,
    }

    fields = {}
    fields["id"] = data["id"]
    for field_name, field_data in data['properties'].items():
        field_type = field_data['type']
        field_result = field_data[field_type]
        field_extractor = field_extractors.get(field_type)

        if field_extractor:
            fields[field_name] = field_extractor(field_result)

    return fields

"""
Posso usar o trecho de codigo abaixo se eu desejar 
armazenar a requisição em cache.
"""
# from cachetools import cached, TTLCache

# cache = TTLCache(maxsize=100, ttl=36000)

# @cached(cache)
# def get_sheets(page_name, sheet_key = os.getenv("ID_SHEETS_EMBARQUE") ):
#     load_dotenv()

#     gc = pygsheets.authorize(service_account_env_var="GOOGLE_CREDENTIALS_EMBARQUE")
#     sheet = gc.open_by_key(sheet_key)
#     worksheet = sheet.worksheet_by_title(page_name)
#     return worksheet

# def invalidate_cache(sheet_name):
#     cache.pop(sheet_name, None)
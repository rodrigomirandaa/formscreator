import json

def get_json_form():
    with open('app/data/form_dataNamedByEudes.json', encoding='utf-8') as f:
        data = json.load(f)
    
    return data
   
def serealizer_json_forms(form_fields):
    form_fields_serealizer = []
    total_questions = 0  # Variável para manter a contagem total de perguntas

    for category in form_fields:
        if category == "contact" or category == "dependent":
            for entry in form_fields[category]:
                form_fields_serealizer.extend(set_forms_fields_unique(category, entry, total_questions))
        elif category not in ["info", "contact", "dependent"]:
            form_fields_serealizer.extend(set_forms_fields_unique(category, form_fields[category], total_questions))
    
    return form_fields_serealizer

def set_forms_fields_unique(category, fields, total_questions):
    form_fields_serealizer = []

    for index, field in enumerate(fields):
        # Usando a contagem total de perguntas para gerar o ID único
        id = total_questions
        total_questions += 1  # Incrementando o total de perguntas para a próxima

        template_field = {
            "id": id,
            "Order": index,
            "category": category,
            "label": field,
            "condition": "",
            "type": "text",
            "required": False,
            "options": [],
            "description": ""
        }

        form_fields_serealizer.append(template_field)

    return form_fields_serealizer


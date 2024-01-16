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

# Está função padronizará o json no formato da Biblioteca Json Forms
def serialize_to_json_forms(form_fields):
    schema = {
        "type": "object",
        "properties": {}
    }

    uischema = {
        "type": "VerticalLayout",
        "elements": []
    }

    for category in form_fields:
        if category not in ["info"]:
            if isinstance(form_fields[category], list):
                # Handle arrays
                array_properties = {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {}
                    }
                }

                array_ui_element = {
                    "type": "Group",
                    "label": category,
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/" + category
                        }
                    ]
                }

                for entry in form_fields[category][0].keys():
                    array_properties["items"]["properties"][entry] = {"type": "string", "minLength": 3}

                schema["properties"][category] = array_properties
                uischema["elements"].append(array_ui_element)
            else:
                # Handle non-array categories
                category_properties = []
                for entry in form_fields[category]:
                    schema["properties"][entry] = {"type": "string", "minLength": 3}
                    category_properties.append({"type": "Control", "label": entry, "scope": "#/properties/" + entry})

                uischema["elements"].append({
                    "type": "Group",
                    "label": category,
                    "elements": category_properties
                })

    return {"schema": schema, "uischema": uischema}

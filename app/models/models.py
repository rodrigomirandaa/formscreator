from datetime import datetime
from app.models.notion import DatabaseNotion
from app.extensions import supabase
import json
import io

class Forms():
    def __init__(self, client_id, title, description, schema, uischema):
        self.client_id = client_id
        self.title = title
        self.description = description
        self.schema = schema
        self.uischema = uischema

    def __repr__(self):
        return '<Form {}>'.format(self.title)
    
    def serealizer(self):
        json_format = {
            "client_id": self.client_id,
            "title": self.title,
            "description": self.description,
            "schema": self.schema,
            "uischema": self.uischema
        }

        return json_format
    
    def send_json_to_supabase_bucket(self):
        file_object = io.BytesIO(json.dumps(self.serealizer()).encode())
        # Obtenha o conteúdo dos bytes
        file_content = file_object.getvalue()

        res = supabase.storage.from_("json_bucket").upload(
            file=file_content,
            path=f"schemas/{self.id}.json",
            file_options={"content-type": "application/json"}
        )

        return res

    def save(self):
        data, count = supabase.table('anprotec_clientes_forms').insert(self.serealizer()).execute()

        return data

    def save_notion(self):
        payload = {
            "properties": {
                "client_name": {
                    "title": [
                        {
                            "text": {
                                "content": "Ademir"
                            }
                        }
                    ]
                },
                "children": [{
                    "object": "block",
                    "type": "pdf",
                    "pdf": {
                        "type": "external",
                        "external": {
                        "url": "https://www.yourwebsite.dev/files/TestFile.pdf"
                        }
                    }
                    }
                ]
            }
        }
        conn = DatabaseNotion(databaseId="f6af625399864626834be3ec99927ed9")
        res = DatabaseNotion.post(payload=payload)

    # def delete(self):
    #     db_session.delete(self)
    #     db_session.commit()
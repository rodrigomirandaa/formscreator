from datetime import datetime
from app.api.questions.utils import get_json_form, serealizer_json_forms
from app.models.notion import DatabaseNotion
from app.extensions import supabase
import uuid
import json
import io

class Forms():
    def __init__(self, title, description, properties):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.properties = properties

    def __repr__(self):
        return '<Questions {}>'.format(self.title)
    
    def serealizer(self):
        form_data = {
            "id": self.id,
            "title": self.title,
            "description":self.description,
            "properties":self.properties
        }

        return form_data
    
    def send_json_to_supabase(self):
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
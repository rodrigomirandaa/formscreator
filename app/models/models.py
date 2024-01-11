from app.api.questions.utils import get_json_form, serealizer_json_forms
from app.models.notion import DatabaseNotion
import json

class Forms():
    def __init__(self, id, title, description, properties):
        self.id = id
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

    def delete(self):
        db_session.delete(self)
        db_session.commit()
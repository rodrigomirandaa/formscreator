from app.api.questions.utils import get_json_form, serealizer_json_forms
from flask import jsonify, make_response
from app.models.notion import DatabaseNotion
from app.api.questions import bp
import secrets
import json

@bp.route('/', methods=['GET'])
def index():
	data = get_json_form()
	properties = serealizer_json_forms(data)

	form_config = {
		"id": 0,
		"title": "My first form",
		"description":"My first form created by amedir",
		"properties":properties
	}
	
	return make_response(jsonify(form_config), 200)

@bp.route('client/<int:id>', methods=["GET"])
def get_client_questions(id):
	payload = {
		"page_size":100,
		"filter":{
			"property":"ID",
			"unique_id":{
				"equals":id
			}
		}
	}

	conn = DatabaseNotion(databaseId='f6af625399864626834be3ec99927ed9')
	res: dict = conn.post(payload=payload)

	return make_response(jsonify(res), 200)
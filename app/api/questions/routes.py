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

@bp.route('/<id>', methods=["GET"])
def get_client_questions(id):
	payload = {
		"page_size":100
	}
	# https://www.notion.so/rafaelalves/e59010d7871e46b79a71a8dc34c3e3f6?v=b3929fe9dd7c43e8be115cdd325fd5aa&pvs=4
	conn = DatabaseNotion(databaseId='79d17223-f72b-47fd-8aa3-291893c7c74e')
	res = conn.post(payload=payload)

	return make_response(jsonify(res.text), 200)
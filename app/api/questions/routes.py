from flask import jsonify, make_response
from app.api.questions import bp
from app.api.questions.utils import get_json_form, serealizer_json_forms
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

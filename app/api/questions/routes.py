from app.api.questions.utils import get_json_form, serialize_to_json_forms
from flask import jsonify, make_response, request
from app.models.notion import DatabaseNotion
from app.models.models import Forms
from app.extensions import supabase
from app.api.questions import bp

@bp.route('/<string:client_id>', methods=['GET'])
def get(client_id):
	data, count = supabase.table('anprotec_clientes_forms').select('*').eq('client_id', client_id).execute()

	return make_response(jsonify(data), 200)

@bp.route('/', methods=['POST'])
def post():
	dados = request.json

	json_data = get_json_form()
	result = serialize_to_json_forms(json_data)

	conn = Forms(title=dados["title"], description=dados["description"], client_id=dados["client_id"], schema=result["schema"], uischema=result["uischema"])
	response = conn.save()

	return make_response(jsonify(response), 200)

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
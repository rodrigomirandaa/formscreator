from app.api.questions.utils import get_json_form, serealizer_json_forms
from flask import jsonify, make_response
from app.models.models import Forms
from app.models.notion import DatabaseNotion
from app.api.questions import bp

@bp.route('/', methods=['GET'])
def get():
	data = get_json_form()
	properties = serealizer_json_forms(data)

	form = Forms(title="My first forms", description="This is my first form in supabase storage", properties=properties)
	response = form.send_json_to_supabase()

	return make_response(jsonify(response.text ), 200)

@bp.route('/<string:id>/', methods=['GET'])
def get_by_id(id):
	form = DatabaseNotion


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
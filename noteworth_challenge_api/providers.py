import functools
import itertools
import json
import pickle
import random
import string
import time

from flask import (
    abort, Blueprint, make_response, request, Response, url_for
)

from noteworth_challenge_api.auth import auth_check


bp = Blueprint('providers', __name__)

@bp.route('/providers', methods=["GET"])
def list() -> Response:
    # Fail modes
    behavior = random.choices(["PASS", "TIMEOUT", "ERROR", "BADDATA"], weights=(50, 10, 20, 20))
    if behavior[0] == "ERROR":
        return make_response("Internal Server Error - please try the request again", 500)
    elif behavior[0] == "TIMEOUT":
        time.sleep(30) # wait for 30 seconds
        return make_response("Request Timeout", 408)

    # check for appropriate headers
    valid = auth_check(request, "/providers")
    if valid.status_code != 200:
        return valid

    data = {}
    # TODO: move this serialization out from static file
    with open('data.json', 'rb') as f:
        data = json.load(f)
    
    providers_list = random.sample(data['practitioners'], 10)
    data['practitioners'] = providers_list
    body = json.dumps(data)

    #failure: incomplete data silently truncates response
    if behavior[0] == "BADDATA":
        body = body[:len(body)//2]
    return make_response(body, 200)

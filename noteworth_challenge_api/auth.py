import functools
import hashlib
import pickle
import random
import string
import time

from flask import (
    abort, Blueprint, make_response, request, Response, url_for
)

bp = Blueprint('auth', __name__)

@bp.route('/auth', methods=['GET'])
def create_token() -> Response:
    # Fail modes
    behavior = random.choices(["PASS", "TIMEOUT", "ERROR"], weights=(60, 30, 10))
    if behavior[0] == "ERROR":
        return make_response("Internal Server Error - please try the request again", 500)
    elif behavior[0] == "TIMEOUT":
        time.sleep(30) # wait for 30 seconds
        return make_response("Request Timeout", 408)

    letters = string.ascii_lowercase
    very_secure_token = {
        'token': ''.join(random.choice(letters) for i in range(8))
    }
    # saving the plain token is not the most secure, but acceptible here
    with open ('data.pickle', 'wb') as f:
        pickle.dump(very_secure_token, f, pickle.HIGHEST_PROTOCOL)

    response = make_response('token generated', 200)
    response.headers['Super-Secure-Token'] = very_secure_token['token']
    return response

def get_token() -> str:
    '''
    returns: token currently created in /auth
    '''
    token = ''
    try:
        with open('data.pickle', 'rb') as f:
            data = pickle.load(f)
            token = data['token']
    except FileNotFoundError:
        abort(Response('Error: No token created'))
    return token

def auth_check(request: request, url: str) -> Response:
    if request.headers.get('X-Request-Checksum') is None:
        return make_response("Unauthorized - Do you have a checksum in the header?", 401)

    # validate auth
    raw_string = f"{get_token()}{url}"
    expected = hashlib.sha256()
    expected.update(b"%b" % raw_string.encode('utf-8'))

    if request.headers.get('X-Request-Checksum') != expected.hexdigest():
        return make_response("Forbidden - checksum failed validation for this API", 403)
    return make_response("validated", 200)
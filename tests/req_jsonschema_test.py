import requests

from config import TYPICODE_SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages
from src.baseclasses.response_jsonschema import Response
from src.schemas.post_jsonschema import POST_SCHEMA


def test_getting_posts():
    r = requests.get(url=TYPICODE_SERVICE_URL)
    response = Response(r)
    response.assert_response_status_code(200).validate(POST_SCHEMA)
    response.validate(POST_SCHEMA)

import requests

from config import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages
from src.baseclasses.response_pydentic import Response
# from src.schemas.post_pydentic import POST_SCHEMA
from src.pydantic_schema.post import Post


def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_response_status_code(200).validate(Post)



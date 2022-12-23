import requests

from config import SERVICE_URL
from src.baseclasses.response_pydentic_assert import Response
from src.schemas.user import User


resp = requests.get(SERVICE_URL)

# print(resp.__getstate__())
# print(resp.url)

def test_getting_users_list():
    response = requests.get(SERVICE_URL)
    test_object = Response(response)
    test_object.assert_status_code(220).validate(User)


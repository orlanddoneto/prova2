import json
import unittest
from nose.tools import *
import requests


URL = "https://testapi.jasgme.com/sgme/api"

def auth_token():
    data = {
        "login": "orlando.neto@dellead.com",
        "password": "neto4256"
    }

    response = requests.post(f"{URL}/authenticate/login", json=data)
    assert_equal(response.status_code, 200)

    json_data = json.loads(response.content)
    return f"Bearer {json_data['token']}"

def get_company_id(header):
    response = requests.get(f"{URL}/companies", headers = header)
    assert_equal(response.status_code, 200)

    json_data = json.loads(response.content)
    first_element= json_data[0]
    id_company = first_element['id']

    return id_company
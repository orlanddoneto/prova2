import json
import unittest
from nose.tools import *
import requests

from utils.main_functions import *


class TestDashboardGoals(unittest.TestCase):
    def setUp(self):
        self.header = {'Authorization': auth_token()}

    def test_get_dashboard(self):
        id_company = get_company_id(self.header)
        params = {'idCompany': id_company}
        response = requests.get(f"{URL}/dashboard/goals/{id_company}", params=params, headers =self.header)
        assert_equal(response.status_code,200)

        json_data = json.loads(response.content)

        assert_in('breakevenPoint', json_data)
        assert_equal(type(json_data['breakevenPoint']),float)
        assert_equal(json_data['breakevenPoint'],0)

        assert_in('salesGoal',json_data)
        assert_equal(type(json_data['salesGoal']),float)
        assert_equal(json_data['salesGoal'],0)

        assert_in('totalTaxForSale',json_data)
        assert_equal(type(json_data['totalTaxForSale']),float)
        assert_equal(json_data['totalTaxForSale'],0)

        assert_in('unitBP',json_data)
        assert_equal(type(json_data['unitBP']),float)
        assert_equal(json_data['unitBP'], 0)

        assert_in('unitSG',json_data)
        assert_equal(type(json_data['unitSG']),float)
        assert_equal(json_data['unitSG'],0)
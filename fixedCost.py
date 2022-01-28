import json
import unittest
from nose.tools import *
import requests

from utils.main_functions import *


class TestFixedCost(unittest.TestCase):
    def setUp(self):
        self.header = {'Authorization': auth_token()}

    def test_get_dashboard(self):
        id_company = get_company_id(self.header)
        params = {'companyId': id_company}
        response = requests.get(f"{URL}/fixed-cost/{id_company}", params=params, headers =self.header)
        assert_equal(response.status_code,200)

        json_data = json.loads(response.content)

        edition = json_data['edition']
        assert_in('socialCharges_company',edition)
        assert_equal(type(edition['socialCharges_company']),float)

        assert_in('min_salary',edition)
        assert_equal(type(edition['min_salary']),float)

        assert_in('max_salary',edition)
        assert_equal(type(edition['max_salary']),float)


        fixedCost = json_data['fixedCost']
        assert_in('for_rent', fixedCost)
        assert_equal(type(fixedCost['for_rent']), float)

        assert_in('office_supplies', fixedCost)
        assert_equal(type(fixedCost['office_supplies']), float)


        salarys = json_data['salarys']
        for data in salarys:
            assert_in('id', data)
            assert_equal(type(data['id']), int)

            role = data['role']
            assert_in('id', role)
            assert_equal(type(role['id']), int)

            assert_in('name', role)
            assert_equal(type(role['name']), str)

            assert_in('value', data)
            assert_equal(type(data['value']), float)


        formulas = json_data['formulas']
        assert_in('sumOfRentFixedCosts', formulas)
        assert_equal(type(formulas['sumOfRentFixedCosts']),float)

        assert_in('sumSalaryFixedCosts', formulas)
        assert_equal(type(formulas['sumSalaryFixedCosts']), float)

        assert_in('sumOfSocialChargesFixedCosts', formulas)
        assert_equal(type(formulas['sumOfSocialChargesFixedCosts']), float)

        assert_in('otherFixedCosts', formulas)
        assert_equal(type(formulas['otherFixedCosts']), float)


        assert_in('paySalary', json_data)
        assert_equal(type(json_data['paySalary']), bool)

        assert_in('hasActionsPermission', json_data)
        assert_equal(type(json_data['hasActionsPermission']), bool)
import json
import unittest
from nose.tools import *
import requests

from utils.main_functions import *


class TestDashboardID(unittest.TestCase):
    def setUp(self):
        self.header = {'Authorization': auth_token()}

    def test_get_dashboard(self):
        id_company = get_company_id(self.header)
        params = {'companyID': id_company}
        response = requests.get(f"{URL}/dashboard/{id_company}", params=params, headers =self.header)
        assert_equal(response.status_code,200)

        json_data = json.loads(response.content)
        journeys = json_data['journeys']

        for data in journeys:
            assert_in('id', data)
            assert_equal(type(data['id']),int)

            assert_in('sort_order', data)
            assert_equal(type(data['sort_order']), int)

            assert_in('current', data)
            assert_equal(type(data['current']), bool)

            assert_in('open', data)
            assert_equal(type(data['open']), bool)


        goals = json_data['goals']

        assert_in('breakevenPoint', goals)
        assert_equal(type(goals['breakevenPoint']), float)

        assert_in('salesGoal', goals)
        assert_equal(type(goals['salesGoal']), float)

        assert_in('totalTaxForSale', goals)
        assert_equal(type(goals['totalTaxForSale']), float)

        assert_in('unitBP', goals)
        assert_equal(type(goals['unitBP']), float)

        assert_in('unitSG', goals)
        assert_equal(type(goals['unitSG']), float)


        progress = json_data['progress']

        assert_in('progressPlaning', progress)
        assert_equal(type(progress['progressPlaning']), float)

        assert_in('progressRH', progress)
        assert_equal(type(progress['progressRH']), float)

        assert_in('progressProduction', progress)
        assert_equal(type(progress['progressProduction']), int)

        assert_in('progressMarketing', progress)
        assert_equal(type(progress['progressMarketing']), int)

        assert_in('progressFinancial', progress)
        assert_equal(type(progress['progressFinancial']), float)


        saleDevolutionInfo = json_data['saleDevolutionInfo']

        assert_in('retired', saleDevolutionInfo)
        assert_equal(type(saleDevolutionInfo['retired']), int)

        assert_in('stock', saleDevolutionInfo)
        assert_equal(type(saleDevolutionInfo['stock']), int)


        totalProductsSelled = json_data['totalProductsSelled']
        assert_equal(type(totalProductsSelled), float)

        percentAveragePresence =json_data['percentAveragePresence']
        assert_equal(type(percentAveragePresence), float)

        formulas = json_data['formulas']
        assert_in('actionsProfitability', formulas)
        assert_equal(type(formulas['actionsProfitability']), float)

        assert_in('totalShareCapital', formulas)
        assert_equal(type(formulas['totalShareCapital']),float)

        assert_in('productionGoal',formulas)
        assert_equal(type(formulas['productionGoal']),float)

        assert_in('saleGoal', formulas)
        assert_equal(type(formulas['saleGoal']), float)


        dre1 = json_data['dre1']
        assert_in('provider', dre1)
        assert_equal(type(dre1['provider']),float)

        assert_in('income',dre1)
        assert_equal(type(dre1['income']),float)

        assert_in('sales',dre1)
        assert_equal(type(dre1['sales']), float)

        assert_in('rent', dre1)
        assert_equal(type(dre1['rent']), float)

        assert_in('taxForSales', dre1)
        assert_equal(type(dre1['taxForSales']),float)

        assert_in('socialCompanyCharges', dre1)
        assert_equal(type(dre1['socialCompanyCharges']), float)

        assert_in('socialEmployeeCharges',dre1)
        assert_equal(type(dre1['socialEmployeeCharges']),float)

        assert_in('comissions', dre1)
        assert_equal(type(dre1['comissions']), float)

        assert_in('netProfit',dre1)
        assert_equal(type(dre1['netProfit']),float)

        assert_in('taxes',dre1)
        assert_equal(type(dre1['taxes']), float)

        assert_in('finalProfit',dre1)
        assert_equal(type(dre1['finalProfit']),float)



        dre2 = json_data['dre2']
        assert_in('provider', dre2)
        assert_equal(type(dre2['provider']), float)

        assert_in('income', dre2)
        assert_equal(type(dre2['income']), float)

        assert_in('sales', dre2)
        assert_equal(type(dre2['sales']), float)

        assert_in('rent', dre2)
        assert_equal(type(dre2['rent']), float)

        assert_in('taxForSales', dre2)
        assert_equal(type(dre2['taxForSales']), float)

        assert_in('socialCompanyCharges', dre2)
        assert_equal(type(dre2['socialCompanyCharges']), float)

        assert_in('socialEmployeeCharges', dre2)
        assert_equal(type(dre2['socialEmployeeCharges']), float)

        assert_in('comissions', dre2)
        assert_equal(type(dre2['comissions']), float)

        assert_in('netProfit', dre2)
        assert_equal(type(dre2['netProfit']), float)

        assert_in('taxes', dre2)
        assert_equal(type(dre2['taxes']), float)

        assert_in('finalProfit', dre2)
        assert_equal(type(dre2['finalProfit']), float)














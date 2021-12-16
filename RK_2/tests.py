import unittest
import sys, os
sys.path.append(os.getcwd())
from main import *

one_to_many=[(d.name1,d.price,p.name)
        for p in providers
        for d in details
        if d.provider_id == p.id]

many_to_many_temp=[(p.name, dp.provider_id,dp.detail_id)
        for p in providers
        for dp in details_providers
        if p.id==dp.provider_id]

many_to_many=[(d.name1,d.price,provider_name)
        for provider_name, provider_id, detail_id in many_to_many_temp
        for d in details if d.id == detail_id]

class TestCost(unittest.TestCase):
    def test_sort_name(self):
        self.assertEqual(sort_name(one_to_many),  [('АвтоСпейс', ['сцепление', 'подвеска']), ('Автотрейд', ['маховик', 'поршень'])])
                         
    def test_sort_price(self):
        self.assertEqual(sort_price(one_to_many, providers), [('Автотрейд', 15000), ('АвтоСпейс', 14000), ('Favorit-auto', 1500)])
        
    def test_sort_provider(self):
        self.assertEqual(sort_provider(many_to_many), [('маховик', 2000, 'Favorit-auto'), ('поршень', 15000, 'Forum-Auto'), 
                                                       ('колодка', 1500, 'Forum-Auto'), ('маховик', 2000, 'Next-auto'), 
                                                       ('подвеска', 14000, 'Next-auto'), ('сцепление', 4000, 'АвтоСпейс'), 
                                                       ('поршень', 15000, 'Автотрейд'), ('сцепление', 4000, 'Гарант-Авто')])

if __name__ == "__main__":
    unittest.main()

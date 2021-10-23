# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests import Form
from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


#import unittest
#from odoo.tests import tagged

class TestPartner(TransactionCase):

    def test_name_search(self):
        """ Check name_search on partner, especially with domain based on auto_join
        user_ids field. Check specific SQL of name_search correctly handle joined tables. """
        values = {
            'name': 'Vlad the Impaler',
            'email': 'asd@gmail.com',
            'country_id': self.env.ref('base.co').id,
            'vat': '123456789',
            'vat_vd': '0',
        }
        test_partner = self.env['res.partner'].create(values)
        ns_name = tuple(set(i[0] for i in self.env['res.partner'].name_search('Vlad')))
        ns_vat = tuple(set(i[0] for i in self.env['res.partner'].name_search('1234567')))
        
        self.assertEqual(test_partner.id, ns_name[0])
        self.assertEqual(test_partner.id, ns_vat[0])


    def test_person_name(self):
        """
        Check person_name on partner
        """
        values = {
            'first_name': 'Juan',
            'middle_name': 'Alberto',
            'last_name': 'Gomez',
            'second_last_name': 'Mendoza',
            'email': 'asd@gmail.com',
            'country_id': self.env.ref('base.co').id,
            'vat': '123456789',
            'vat_vd': '0',
        }
        test_partner = self.env['res.partner'].person_name(values)
        self.assertEqual(test_partner['name'], 'Juan Alberto Gomez Mendoza')

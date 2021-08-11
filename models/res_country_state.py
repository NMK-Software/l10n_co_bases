# -*- coding: utf-8 -*-
# Copyright 2019 NMKSoftware
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields, api

class ResCountryState(models.Model):
    _inherit = 'res.country.state'

    postal_code = fields.Char(string=u'Postal code',)

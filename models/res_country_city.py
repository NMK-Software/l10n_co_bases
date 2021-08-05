# -*- coding: utf-8 -*-
# Copyright 2019 NMKSoftware
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields, api

class ResCountryCity(models.Model):
    _name = 'res.country.city'

    country_id = fields.Many2one('res.country', string="Country")
    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    state_id = fields.Many2one('res.country.state', string="State")
    postal_code = fields.Char(string=u'Postal code',)

    @api.multi
    def name_get(self):
        rec = []
        for recs in self:
            name = '%s / %s [%s]' % (recs.name or '', recs.state_id.name or '', recs.code or '')
            rec += [ (recs.id, name) ]
        return rec

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        """
        Se hereda metodo name search y se sobreescribe para hacer la busqueda 
        por el codigo de la ciudad
        """
        if not args:
            args = []
        args = args[:]
        ids = []
        if name:
            ids = self.search([('code', '=like', name + "%")] + args, limit=limit)
            if not ids:
                ids = self.search([('name', operator, name)] + args,limit=limit)
        else:
            ids = self.search(args, limit=100)

        if ids:
            return ids.name_get()
        return self.name_get()
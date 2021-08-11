# -*- coding: utf-8 -*-


from odoo import SUPERUSER_ID, api, fields, models, _

class AccountDebitConcept(models.Model):
    _name = 'account.debit_concept'
    _description = "Debit Note Concept"

    name = fields.Char(
        string='Descripcion',
        help='Descripcion del tipo del concepto de la Nota Debito',
    )
    code = fields.Char(
        string="Codigo",
        help='Codigo segun listado de valores de la DIAN',
    )
    active=fields.Boolean(string="Activo")
    state=fields.Selection([('working','En uso'),('discontinued','Vigencia Suspendida')],string="Estado",help="Estado del tipo concepto segun DIAN")

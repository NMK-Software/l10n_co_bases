# -*- coding: utf-8 -*-


from odoo import SUPERUSER_ID, api, fields, models, _

class AccountCreditConcept(models.Model):
    _name = 'account.credit_concept'
    _description = "Credit Note Concept"

    name = fields.Char(
        string='Descripcion',
        help='Descripcion del tipo del concepto de la Nota Credito',
    )
    code = fields.Char(
        string="Codigo",
        help='Codigo segun listado de valores de la DIAN',
    )
    active=fields.Boolean(string="Activo")
    state=fields.Selection([('working','En uso'),('discontinued','Vigencia Suspendida')],string="Estado",help="Estado del tipo de concepto segun DIAN")

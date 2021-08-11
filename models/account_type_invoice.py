# -*- coding: utf-8 -*-


from odoo import SUPERUSER_ID, api, fields, models, _

class AccoutTypeInvoice(models.Model):
    _name = 'account.type.invoice'
    _description = "Type invoice"

    name = fields.Char(
        string='Descripcion',
        help='Descripcion del tipo de factura',
    )
    code = fields.Char(
        string="Codigo",
        help='Codigo segun listado de valores de la DIAN',
    )
    active=fields.Boolean(string="Activo")
    state=fields.Selection([('working','En uso'),('discontinued','Vigencia Suspendida')],string="Estado",help="Estado del tipo de la factura segun DIAN")

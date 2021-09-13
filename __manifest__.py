# -*- coding: utf-8 -*-
# Copyright 2019 NMKSoftware
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Localizacion Base - Colombia',
    'summary': 'Localizacion Base - Colombia',
    'author': 'NMKSoftware',
    'maintainer': 'NMKSoftware',
    'website': '',
    'version': '11.0.1.0.0',
    'category': 'Localization',
    'depends': [
        'base',
        'account',
        'account_tax_python',
        'l10n_co',
        
    ],
    'data': [
        'data/res.country.city.csv',
        'data/res.bank.csv',
        'security/ir.model.access.csv',
        'data/res.ciiu.csv',
        'data/res_country_data.xml',
        'data/account_tax_group.xml',
        'data/account_tax_template.xml',
        'views/res_config_setting.xml',
        'views/res_ciiu_view.xml',
        'views/res_partner_view.xml',
        'views/res_company_view.xml',
        'views/res_country_view.xml',
        'views/account_tax_view.xml',
        'views/account_journal_view.xml',
        'views/product_category_view.xml',
        'views/res_country_city.xml',
        'views/account_invoice_view.xml',
        'views/menu.xml',
        'views/report_invoice_document.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application' : True,
}

# -*- coding: utf-8 -*-
{
    'name': "de01",

    'summary': """
        Quản lý lịch sử nhu cầu, chăm sóc KH và đơn hàng bán""",

    'description': """
        Quản lý lịch sử nhu cầu, chăm sóc KH và đơn hàng bán
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/crm_customer_request_view.xml',
        'views/crm_lead_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'sequence': 2
}

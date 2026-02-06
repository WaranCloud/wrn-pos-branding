# -*- coding: utf-8 -*-
{
    'name': 'WaranCloud POS Branding',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'summary': 'Rebranding Odoo POS to WaranCloud',
    'description': """
        This module replaces Odoo branding with WaranCloud in the Point of Sale interface,
        including window title, logos, favicons, and receipt footer.
    """,
    'author': 'WaranCloud',
    'website': 'https://www.warancloud.com',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_assets_index.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'wrn_pos_branding/static/src/app/**/*',
            'wrn_pos_branding/static/src/customer_display/**/*',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}

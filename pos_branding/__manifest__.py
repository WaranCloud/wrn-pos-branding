{
    'name': 'POS Branding (WaranCloud)',
    'version': '18.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'White-label Odoo POS with company and WaranCloud branding',
    'license': 'LGPL-3',
    'author': 'WaranCloud',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_branding/static/src/app/components/navbar/navbar.xml',
            'pos_branding/static/src/app/components/loader/loader.xml',
            'pos_branding/static/src/app/screens/saver_screen/saver_screen.xml',
            'pos_branding/static/src/app/screens/receipt_screen/receipt/order_receipt.xml',
            'pos_branding/static/src/scss/pos_branding.scss',
        ],
        'point_of_sale.customer_display_assets': [
            'pos_branding/static/src/customer_display/customer_display.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
}

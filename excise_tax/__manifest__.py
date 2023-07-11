# -*- coding: utf-8 -*-

{
    'name': 'Excise Tax on Purchase order',
    'version': '15.0.1.0.0',
    'summary': """Excise Tax on Purchase order""",
    'description': """Excise Tax on Purchase order""",
    'category': 'Purchase',
    'depends': ['base', 'purchase', 'account'],
    'author': "Sreerag",
    'data': [
        'data/excise_tax.xml',
        'views/purchase_order.xml'
    ],
    'assets': {
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}

# -*- coding: utf-8 -*-
{
    'name': 'Product Characteristics Page',
    'version': '1.0',
    'summary': 'Add a page to product module with a few new fields',
    'category': 'Product/Product',
    'author': 'Binhex',
    'depends': [
        'base',
        'product',
        'account'
        ],
    'data': [
        "security/ir.model.access.csv",
        "views/product_characteristics_views.xml"
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

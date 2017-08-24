# -*- coding: utf-8 -*-
# Copyright 2017 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Product Attribute Group',
    'summary': """
        Allows grouping of product attributes for easy addition
        to a product template""",
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Graeme Gellatly',
    'website': 'https://o4sb.com',
    'depends': [
        'product', 'sale', 'sales_team', 'stock'
    ],
    'data': [
        'security/product_attribute_group.xml',
        'views/product_attribute_group.xml',
        'views/product_template.xml',
    ],
    'demo': ['demo/product_demo.xml']
}

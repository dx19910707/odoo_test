# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        杜希的测试""",

    'description': """
        杜希的测试
    """,

    'author': "杜希",
    'website': "http://www.bilibili.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',  # 因为权限配置会使用到新配的分组，所以先加载security.xml文件
        'views/views.xml',
        'views/openacademy.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
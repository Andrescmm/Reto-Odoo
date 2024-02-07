# -*- coding: utf-8 -*-
{
    'name': "School",

    'summary': """  """,
    'author': "Andres Cusirramos Marquez Mares",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/student_view.xml',
        'views/subject_view.xml',
        'views/teacher_view.xml'
    ],
    
    'installable': True,
    'auto_install': False,
    'application': True,
}

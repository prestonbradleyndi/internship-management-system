{
    'name': 'Internship Portal',
    'version': '1.0.0',
    'category': 'Human Resources',
    'summary': 'Portal interface for interns',
    'description': """
        Internship Portal
        =================

        Provides a dedicated portal interface for interns to:
        - View internship information
        - View assigned tasks
        - View internship reports
        - View supervisor feedback
    """,

    'author': 'Preston Bradley Ndi',
    'license': 'LGPL-3',

    'depends': [
        'portal',
        'website',
        'internship_management',
    ],

    'data': [
        'views/portal_templates.xml',
    ],

    'installable': True,
    'application': False,
}
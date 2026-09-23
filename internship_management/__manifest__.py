{
    'name': 'Internship Management System',
    'version': '1.0.0',
    'category': 'Human Resources',
    'summary': 'Manage interns, internships, tasks, attendance, reports, evaluations and feedback',
    'description': """
        Internship Management System
        ============================

        A custom Odoo module for managing:

        - Interns
        - Internship programs
        - Supervisors
        - Tasks
        - Attendance
        - Internship reports
        - Evaluations
        - Feedback
        - User access and security
    """,
    'author': 'Preston Bradley Ndi',
    'license': 'LGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        # Security groups
        'security/security.xml',

        # Model access rights
        'security/ir.model.access.csv',

        # Record rules and additional access rights
        'security/ims_access_rules.xml',

        # Main IMS views
        'views/intern_views.xml',

        # User-related views
        'views/user_views.xml',

        # Supervisor management view
        'views/supervisor_views.xml',
    ],
    'installable': True,
    'application': True,
}
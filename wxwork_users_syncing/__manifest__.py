# -*- coding: utf-8 -*-
{
    "name": "Enterprise WeChat User Syncing",
    "author": "RStudio",
    "website": "",
    "sequence": 1,
    "installable": True,
    "application": True,
    "auto_install": False,
    "category": "wxwork",
    "version": "13.0.0.1",
    "summary": """
        Enterprise WeChat User Syncing
        """,
    "description": """


        """,
    "depends": [
        "base",
        "mail",
        "hr",
        # 'auth_oauth',
        "wxwork_base",
    ],
    "external_dependencies": {
        "python": [
            "numpy",
            "opencv-python",
        ],
    },
    "data": [
        "data/ir_cron_data.xml",
        "data/wxwork_data.xml",
        "views/ir_cron_views.xml",
        "wizard/wizard_wxwork_contacts_sync.xml",
        "wizard/wizard_wxwork_sync_user.xml",
        "views/hr_department_view.xml",
        "views/hr_employee_view.xml",
        "views/res_users_views.xml",
        "views/wxwork_contacts_views.xml",
        "views/res_config_settings_views.xml",
    ],
    "qweb": [
        "static/src/xml/*.xml",
    ],
}

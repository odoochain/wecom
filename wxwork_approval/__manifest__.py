# -*- coding: utf-8 -*-
{
    "name": "企业微信-审批",
    "author": "RStudio",
    "website": "",
    "sequence": 1,
    "installable": True,
    "application": True,
    "auto_install": False,
    "category": "企业微信",
    "version": "13.0.0.1",
    "summary": """
        获取企业微信审批记录
        """,
    "description": """
功能：
====================

        """,
    "depends": [
        # 'hr_attendance',
        # 'wxwork_users_syncing',
    ],
    "data": [
        # 'data/wxwork_data.xml',
        # 'views/res_config_settings_views.xml',
        # 'views/wxwork_attendance_views.xml',
    ],
    "qweb": [
        "static/src/xml/*.xml",
    ],
    "bootstrap": True,  # load translations for login screen
    # 'external_dependencies': {'python': ['skimage']},
}

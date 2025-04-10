# © 2025 Joullutfi - Test Module
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Test Web Feature",
    "summary": "Testmodule voor het experimenteren met Odoo backend functionaliteit",
    "license": "AGPL-3",
    "version": "16.0.0.1.0",
    "website": "https://github.com/joullutfi/test",
    "author": "Joullutfi",
    "depends": ["web"],
    "excludes": ["web_enterprise"],
    "installable": True,
    "assets": {
        "web.test_web_assets_common": [
            ("prepend", "test_web/static/src/scss/test_variables.scss"),
        ],
        "web.test_web_assets_backend": [
            ("prepend", "test_web/static/src/scss/test_variables.scss"),
        ],
        "web.assets_backend": [
            "test_web/static/src/js/test_feature.esm.js",
        ],
    },
    "data": [
        "views/test_users_views.xml",
    ],
}

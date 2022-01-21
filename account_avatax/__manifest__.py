{
    "name": "Avalara Avatax Connector",
    "version": "15.0.1.0.1",
    "author": "Open Source Integrators, Fabrice Henrion,"
    "Sodexis, Odoo Community Association (OCA)",
    "summary": "Automatic Tax application using the Avalara Avatax Service",
    "license": "AGPL-3",
    "category": "Accounting",
    "website": "https://github.com/OCA/account-fiscal-rule",
    "depends": ["account", "sale_stock", "base_geolocalize"],
    "data": [
        "security/avalara_salestax_security.xml",
        "security/ir.model.access.csv",
        "data/avalara_salestax_data.xml",
        "data/avalara_salestax_exemptions.xml",
        "wizard/avalara_get_company_code_view.xml",
        "wizard/avalara_salestax_address_validate_view.xml",
        "wizard/avalara_salestax_ping_view.xml",
        "views/avalara_salestax_view.xml",
        "views/partner_view.xml",
        "views/product_view.xml",
        "views/account_move_action.xml",
        "views/account_move_view.xml",
        "views/account_tax_view.xml",
        "views/account_fiscal_position_view.xml",
    ],
    "demo": ["demo/avatax_demo.xml"],
    "images": ["static/description/avatax_icon.png"],
    "installable": True,
    "application": True,
    "external_dependencies": {"python": ["Avalara"]},
    "development_status": "Production/Stable",
    "maintainers": ["dreispt"],
}

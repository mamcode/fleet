# Copyright 2021 - TODAY, Escodoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Fleet Vehicle Model Parts and Services",
    "summary": """
        Extend Fleet Module to enable associate parts and services
        compatible with the vehicle model.""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Escodoo,Odoo Community Association (OCA)",
    "maintainers": ["marcelsavegnago"],
    "website": "https://github.com/OCA/fleet",
    "images": ["static/description/banner.png"],
    "category": "Human Resources/Fleet",
    "depends": ["fleet", "product"],
    "data": [
        "views/product_template.xml",
        "views/product_product.xml",
        "views/fleet_vehicle_model.xml",
    ],
}

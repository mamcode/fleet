# Copyright 2021 - TODAY, Escodoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Fleet Vehicle Inspection Repair',
    'summary': """
        Generate repair order from fleet vehicle inspection""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Escodoo,Odoo Community Association (OCA)',
    'category': 'Human Resources/Fleet',
    'maintainers': ['marcelsavegnago'],
    'images': ['static/description/banner.png'],
    'website': 'https://github.com/OCA/fleet',
    'depends': [
        'fleet_vehicle_inspection_item_compatible_product',
        'account',
        'web_domain_field',

    ],
    'data': [
        'security/fleet_vehicle_inspection_repair_line.xml',
        'views/fleet_vehicle_inspection_repair_line.xml',
        'views/fleet_vehicle_inspection.xml',
        'views/fleet_vehicle_inspection_line.xml',
    ],
}

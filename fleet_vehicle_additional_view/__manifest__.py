# Copyright 2021 - TODAY, Escodoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Fleet Vehicle Additional View',
    'summary': """
        TThis module extends the fleet management functionality. Adds other
        vehicle views.""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'category': 'Human Resources/Fleet',
    'author': 'Escodoo,Odoo Community Association (OCA)',
    'maintainers': ['marcelsavegnago'],
    'images': ['static/description/banner.png'],
    'website': 'https://github.com/OCA/fleet',
    'depends': [
        'fleet',
    ],
    'data': [
        'views/fleet_vehicle.xml',
    ],
}

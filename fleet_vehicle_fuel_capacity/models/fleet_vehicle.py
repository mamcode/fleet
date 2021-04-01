# Copyright 2021 - TODAY, Marcel Savegnago
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FleetVehicle(models.Model):

    _inherit = 'fleet.vehicle'

    fuel_capacity = fields.Float(
        string='Fuel Capacity (L)',
        track_visibility='onchange'
    )

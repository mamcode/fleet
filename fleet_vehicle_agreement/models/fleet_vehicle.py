# Copyright 2021 - TODAY, Marcel Savegnago <marcel.savegnago@escodoo.com.br>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FleetVehicle(models.Model):

    _inherit = "fleet.vehicle"

    agreement_ids = fields.Many2many(
        comodel_name="agreement",
        relation="fleet_vehicle_agreement_rel",
        column1="vehicle_id",
        column2="agreement_id",
        string="Agreements",
        domain=[],
        context={},
        help="Agreements",
    )

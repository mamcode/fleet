# Copyright 2021 - TODAY, Marcel Savegnago <marcel.savegnago@escodoo.com.br>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FleetVehicleModel(models.Model):

    _inherit = "fleet.vehicle.model"

    product_ids = fields.Many2many(
        "product.product",
        "fleet_vehicle_model_product_rel",
        "model_id",
        "product_id",
        "Vehicle Parts/Services",
        domain=[("vehicle_part_ok", "=", True)],
        help="Compatible Parts/Services",
    )

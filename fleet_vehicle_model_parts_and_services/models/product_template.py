# Copyright 2021 - TODAY, Marcel Savegnago <marcel.savegnago@escodoo.com.br>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    fleet_ok = fields.Boolean("Can be Vehicle Part/Service")

    part_vehicle_model_ids = fields.Many2many(
        "fleet.vehicle.model",
        "fleet_vehicle_model_product_part_rel",
        "product_id",
        "model_id",
        "Vehicle Models",
    )

    service_vehicle_model_ids = fields.Many2many(
        "fleet.vehicle.model",
        "fleet_vehicle_model_product_service_rel",
        "product_id",
        "model_id",
        "Vehicle Models",
    )

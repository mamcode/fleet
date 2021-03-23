# Copyright 2021 - TODAY, Marcel Savegnago <marcel.savegnago@escodoo.com.br>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FleetVehicleModel(models.Model):

    _inherit = "fleet.vehicle.model"

    part_ids = fields.Many2many(
        "product.product",
        "fleet_vehicle_model_parts",
        "model_id",
        "product_id",
        "Vehicle Parts",
        domain=["&", ("fleet_ok", "=", True), ("type", "in", ["consu", "product"])],
        required=True,
        help="Vehicle Model Compatible Parts",
    )

    service_ids = fields.Many2many(
        "product.product",
        "fleet_vehicle_model_product_services",
        "model_id",
        "product_id",
        "Vehicle Services",
        domain=["&", ("fleet_ok", "=", True), ("type", "=", "service")],
        required=True,
        help="Vehicle Model Compatible Services",
    )

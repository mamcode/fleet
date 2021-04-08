# Copyright 2021 - TODAY, Marcel Savegnago <marcel.savegnago@escodoo.com.br>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class FleetVehicleInspection(models.Model):

    _inherit = 'fleet.vehicle.inspection'

    repair_product_ids = fields.One2many(
        'fleet.vehicle.inspection.repair.line',
        'inspection_id',
        string='Inspection Repair Products',
        readonly=True,
    )

    amount_total = fields.Float('Total', compute='_amount_total', store=True)

    @api.one
    @api.depends('repair_product_ids.price_subtotal', 'repair_product_ids.product_id')
    def _amount_total(self):
        total = sum(repair_product_id.price_subtotal for repair_product_id in self.repair_product_ids)
        self.amount_total = total

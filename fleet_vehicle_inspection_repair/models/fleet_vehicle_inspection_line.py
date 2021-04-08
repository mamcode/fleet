# Copyright 2021 - TODAY, Marcel Savegnago <marcel.savegnago@escodoo.com.br>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class FleetVehicleInspectionLine(models.Model):

    _inherit = 'fleet.vehicle.inspection.line'

    repair_product_ids = fields.One2many(
        'fleet.vehicle.inspection.repair.line', 'inspection_line_id',
        string='Inspection Repair Products',
    )

    amount_total = fields.Float('Total', compute='_amount_total', store=True)

    # @api.one
    # @api.depends('operations.price_subtotal', 'invoice_method', 'fees_lines.price_subtotal', 'pricelist_id.currency_id')
    # def _amount_untaxed(self):
    #     total = sum(operation.price_subtotal for operation in self.operations)
    #     total += sum(fee.price_subtotal for fee in self.fees_lines)
    #     self.amount_untaxed = self.pricelist_id.currency_id.round(total)

    # @api.one
    # @api.depends('operations.price_unit', 'operations.product_uom_qty', 'operations.product_id',
    #              'fees_lines.price_unit', 'fees_lines.product_uom_qty', 'fees_lines.product_id',
    #              'pricelist_id.currency_id', 'partner_id')
    # def _amount_tax(self):
    #     val = 0.0
    #     for operation in self.operations:
    #         if operation.tax_id:
    #             tax_calculate = operation.tax_id.compute_all(operation.price_unit, self.pricelist_id.currency_id,
    #                                                          operation.product_uom_qty, operation.product_id,
    #                                                          self.partner_id)
    #             for c in tax_calculate['taxes']:
    #                 val += c['amount']
    #     for fee in self.fees_lines:
    #         if fee.tax_id:
    #             tax_calculate = fee.tax_id.compute_all(fee.price_unit, self.pricelist_id.currency_id,
    #                                                    fee.product_uom_qty, fee.product_id, self.partner_id)
    #             for c in tax_calculate['taxes']:
    #                 val += c['amount']
    #     self.amount_tax = val

    @api.one
    @api.depends('repair_product_ids.price_subtotal', 'repair_product_ids.product_id')
    def _amount_total(self):
        total = sum(repair_product_id.price_subtotal for repair_product_id in self.repair_product_ids)
        self.amount_total = total

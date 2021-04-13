# Copyright 2021 - TODAY, Marcel Savegnago <marcel.savegnago@escodoo.com.br>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import json

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp


class FleetVehicleInspectionRepairLine(models.Model):
    _name = 'fleet.vehicle.inspection.repair.line'
    _description = 'Fleet Vehicle Inspection Repair Line'

    inspection_id = fields.Many2one(
        'fleet.vehicle.inspection',
        string='Inspection Reference',
        required=True,
        ondelete='cascade',
        index=True)

    inspection_line_id = fields.Many2one(
        'fleet.vehicle.inspection.line',
        string='Inspection Line Reference',
        required=True,
        domain="[('inspection_id', '=', inspection_id)]",
        ondelete='cascade',
        index=True)

    product_id_domain = fields.Char(
        compute="_compute_product_id_domain",
        readonly=True,
        store=False,
    )

    product_id = fields.Many2one(
        'product.product',
        'Product',
        required=True,
        context={'default_is_fleet_vehicle_product': True},
        help='Products/Services',
    )

    categ_id = fields.Many2one(related='product_id.categ_id', help="Product Category",
                               readonly=True)

    type = fields.Selection(related='product_id.type', help="Product Type",
                            readonly=True)

    product_uom = fields.Many2one(related='product_id.uom_id', help="Product UoM",
                                  readonly=True)

    product_uom_qty = fields.Float(
        'Quantity', default=1.0,
        digits=dp.get_precision('Product Unit of Measure'), required=True)

    pricelist_id = fields.Many2one(
        'product.pricelist', 'Pricelist',
        default=lambda self: self.env['product.pricelist'].search([], limit=1).id,
        help='Pricelist of the selected partner.')

    price_unit = fields.Float('Unit Price', required=True, digits=dp.get_precision('Product Price'))

    price_subtotal = fields.Float(
        'Subtotal',
        compute='_compute_price_subtotal',
        store=True,
        digits=0)

    tax_id = fields.Many2many(
        'account.tax', 'repair_operation_line_tax', 'repair_operation_line_id', 'tax_id', 'Taxes')

    @api.one
    @api.depends('price_unit', 'product_uom_qty', 'product_id', )
    def _compute_price_subtotal(self):
        taxes = self.tax_id.compute_all(
            self.price_unit,
            self.pricelist_id.currency_id,
            self.product_uom_qty,
            self.product_id,
            self.inspection_id.driver_id)
        self.price_subtotal = taxes['total_excluded']

    @api.multi
    @api.depends('inspection_id', 'inspection_line_id', )
    def _compute_product_id_domain(self):
        for rec in self:
            model_compatible_product_ids = \
                rec.inspection_id.vehicle_id.model_id.compatible_product_ids
            inspection_line_compatible_product_ids = \
                rec.inspection_line_id.inspection_item_id.compatible_product_ids
            product_ids = \
                model_compatible_product_ids & inspection_line_compatible_product_ids
            rec.product_id_domain = json.dumps([
                ('is_fleet_vehicle_product', '=', True),
                ('id', 'in', product_ids.ids)
            ])

    @api.onchange('inspection_id', 'inspection_line_id', 'product_id')
    def _onchange_inspection_or_inspection_line(self):
        self._compute_product_id_domain()

    @api.onchange('product_id')
    def _onchange_product_id(self):
        partner = self.inspection_id.driver_id
        pricelist = self.pricelist_id
        # pricelist = partner.property_product_pricelist or False
        if pricelist and self.product_id:
            price = pricelist.get_product_price(
                self.product_id,
                self.product_uom_qty,
                partner,
                uom_id=self.product_uom.id
            )
            if price is False:
                warning = {
                    'title': _('No valid pricelist line found.'),
                    'message':
                        _(
                            "Couldn't find a pricelist line matching this product"
                            "and quantity. You have to change either the product,"
                            "the quantity or the pricelist.")}
                return {'warning': warning}
            else:
                self.price_unit = price

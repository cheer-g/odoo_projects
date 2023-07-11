# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    excise_tax = fields.Float("Excise Tax", default=0.0,
                              help="Manually enter the excise tax for the "
                                   "product")

    @api.depends('product_qty', 'price_unit', 'taxes_id', 'excise_tax')
    def _compute_amount(self):
        for line in self:
            taxes = line.taxes_id.compute_all(
                **line._prepare_compute_all_values())

            # # Adding the Excise Tax values
            excise_tax_id = self.env.ref('excise_tax.purchase_excise_tax')
            excise_tax_id.amount = line.excise_tax
            line.write({
                'taxes_id': [(3, excise_tax_id.id)]
            })
            line.write({
                'taxes_id': [(4, excise_tax_id.id)]
            })

            line.update({
                'price_tax': sum(
                    t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })

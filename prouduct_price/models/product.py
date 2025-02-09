from odoo import models, fields, api

class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    fixed_price = fields.Float(string='Fixed Price')


class ProductProduct(models.Model):
    _inherit = 'product.product'

    fixed_price = fields.Float(string='Fixed Price', compute="_compute_fixed_price", store=True)
    pricelist_item_ids = fields.One2many('product.pricelist.item', 'product_id', string="Pricelist Items")  # ربط عناصر قائمة الأسعار

    @api.depends('pricelist_item_ids.fixed_price')
    def _compute_fixed_price(self):
        for record in self:
            fixed_price = 0.0
            for item in record.pricelist_item_ids:
                if item.fixed_price:
                    fixed_price = item.fixed_price
                    break
            record.fixed_price = fixed_price
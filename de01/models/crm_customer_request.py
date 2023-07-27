from odoo import models, fields


class Customer(models.Model):
    _name = 'crm.customer.request'
    _description = 'Nhu cau khach hang /Customer Request'

    product_id = fields.Many2one(comodel_name='product.template', string='Product', required=1)
    opportunity_id = fields.Many2one(comodel_name='crm.lead', string='Opportunity', required=1)
    date = fields.Date(string='Request Date', default=fields.Date.today)
    description = fields.Char(string='Description')
    qty = fields.Float(string='Quantity', default=1)

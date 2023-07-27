from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    request_ids = fields.One2many(comodel_name='crm.customer.request', inverse_name='opportunity_id', string='Request')
    doanh_so = fields.Float(string='Doanh Số', compute='tong_doanh_so')
    gia_tri_mong_doi = fields.Char(string='Giá trị Doanh thu mong đợi', compute='gia_tri_doanh_thu')

    @api.depends('request_ids.qty')
    def tong_doanh_so(self):
        for rec in self:
            total_qty = 0
            for record in rec.request_ids:
                total_qty += record.qty
            rec.doanh_so = total_qty

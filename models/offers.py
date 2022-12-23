from odoo import models, fields, _, api
from dateutil.relativedelta import relativedelta


class Offers(models.Model):
    _name = 'estate.property.offer'

    price = fields.Monetary(string=_('Price'), currency_field='currency_id')
    status = fields.Selection([('accepted','Accepted'), ('refused','Refused')], copy=False)
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property')
    currency_id = fields.Many2one('res.currency', string="Currency", default=lambda self: self.env.ref('base.VND').id)
    validity = fields.Integer(string=_('Validity (days)'), default = 7)
    date_deadline = fields.Date(string=_('Date Deadline'), compute='compute_deadline', store=True)

    @api.depends('validity')
    def compute_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)

    def confirm_button(self):
        for record in self:
            record.status = 'accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer = record.partner_id

    def reject_button(self):
        for record in self:
            record.status = 'refused'
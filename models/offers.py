from odoo import models, fields, _


class Offers(models.Model):
    _name = 'estate.property.offer'

    price = fields.Monetary(string=_('Price'), currency_field='currency_id')
    status = fields.Selection([('accepted','Accepted'), ('refused','Refused')], copy=False)
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property')
    currency_id = fields.Many2one('res.currency', string="Currency", default=lambda self: self.env.ref('base.VND').id)

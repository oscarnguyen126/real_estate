from odoo import fields, models, _
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string=_('Name'), required=True)
    description = fields.Text(string=_('Description'))
    postcode =  fields.Char(string=_('Postcode'))
    date_availability = fields.Date(string=_('Date Availability'), default=lambda self: fields.Datetime.now() + relativedelta(months=3))
    expected_price = fields.Monetary(string=_('Expected Price'), currency_field='currency_id', requỉed=True)
    selling_price = fields.Monetary(string=_('Selling Price'), currency_field='currency_id')
    bedrooms = fields.Integer(string=_('Bedrooms'), default=2)
    living_area = fields.Integer(string=_('Living area'))
    facades = fields.Integer(string=_('Facades'))
    garage = fields.Boolean(string=_('Garage'))
    garden = fields.Boolean(string=_('Garden'))
    garden_area = fields.Integer(string=_('Garden Area'))
    garden_orientation = fields.Selection([('north', 'North'),('south', 'South'),('east', 'East'), ('west', 'West')], string=_('Garden Orientation'))
    currency_id = fields.Many2one('res.currency', string="Currency", default=lambda self: self.env.ref('base.VND').id)
    active = fields.Boolean(default=False)
    state = fields.Selection([('new', 'New'), ('offer received', 'Offer Received'), ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')], required=True, copy=False, default='new')
    property_type_id = fields.Many2one('estate.property.type')
    salesperson = fields.Many2one('res.users', string=_('Salesman'), default=lambda self:self.env.user)
    buyer = fields.Many2one('res.partner')
    tag_ids = fields.Many2many('estate.property.tag','estate_property_tags_rel','estate_property_id','estate_property_tag_id')
    offer_ids = fields.One2many('estate.property.offer', 'property_id')

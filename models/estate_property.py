from odoo import fields, models, _, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError, UserError


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
    total_area = fields.Integer(string=_('Total area'), compute='compute_area', store=True)
    best_price = fields.Monetary(string=_('Best price'), currency_field='currency_id', compute='compute_best_price', store=True)

    @api.depends('living_area', 'garden_area')
    def compute_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids')
    def compute_best_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped('price'))

    @api.onchange('garden')
    def onchange_area_and_orientation(self):
        for record in self:
            if record.garden is True:
                record.garden_area = 10
                record.garden_orientation = 'north'

    def sold_button(self):
        for record in self:
            if record.state == 'canceled':
                raise UserError('Canceled property cannot be sold')
            record.state = 'sold'
    def cancel_button(self):
        for record in self:
            if record.state == 'sold':
                raise UserError('Sold property cannot be canceled')
            record.state = 'canceled'
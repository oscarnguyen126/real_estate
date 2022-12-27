from odoo import models, fields, _,  api
from odoo.exceptions import ValidationError, UserError


class Type(models.Model):
    _name = 'estate.property.type'
    _order = 'name'

    name = fields.Char(string=_('Type'), required=True)
    estate_ids = fields.One2many('estate.property', 'property_type_id')
    offer_ids = fields.One2many('estate.property.offer', 'property_type_id')
    offer_count = fields.Integer()

    @api.constrains('name')
    def constrains_name(self):
        for record in self:
            names = self.env['estate.property.type'].search([('name', '=', record.name), ('id', '!=', record.id)])
            if names:
                if len(names) > 0:
                    raise ValidationError('The property type must be unique')

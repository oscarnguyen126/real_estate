from odoo import models, fields, _


class Type(models.Model):
    _name = 'estate.property.type'

    name = fields.Char(string=_('Type'))
    estate_ids = fields.One2many('estate.property', 'property_type_id')

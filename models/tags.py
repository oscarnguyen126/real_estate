from odoo import models, fields, _, api
from odoo.exceptions import ValidationError, UserError


class Tags(models.Model):
    _name = 'estate.property.tag'
    _order = 'name'

    name = fields.Char(string=_('Tag'), required=True)
    color = fields.Integer()

    @api.constrains('name')
    def constrains_name(self):
        for record in self:
            names = self.env['estate.property.tag'].search([('name', '=', record.name), ('id', '!=', record.id)])
            if names:
                if len(names) > 0:
                    raise ValidationError('The property tag must be unique')
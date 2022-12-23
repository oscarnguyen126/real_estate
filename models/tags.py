from odoo import models, fields, _


class Tags(models.Model):
    _name = 'estate.property.tag'

    name = fields.Char(string=_('Tag'), required=True)

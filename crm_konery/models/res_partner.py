from odoo import _, api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    vat = fields.Char(required=True)
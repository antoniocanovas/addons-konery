from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    crm_user_id = fields.Many2one('res.users', string='CRM Salesman',
                                  related='opportunity_id.user_id', readonly=False,
                                  domain="['&', ('share', '=', False), ('company_ids', 'in', user_company_ids)]",
                                  check_company=True, index=True, tracking=True)
    crm_team_id = fields.Many2one('crm.team', string='CRM Team', related='opportunity_id.team_id', readonly=False)
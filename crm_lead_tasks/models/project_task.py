from odoo import _, api, fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    lead_id = fields.Many2one('crm.lead', string="Lead", store=True)

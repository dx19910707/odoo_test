from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean("指导员", default=False)

    session_ids = fields.Many2many('openacademy.session', string="出席的sessions", readonly=True)


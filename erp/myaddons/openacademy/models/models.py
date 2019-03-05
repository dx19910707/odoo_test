# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Courses'

    name = fields.Char(string='课程标题', required=True)
    description = fields.Text(string='课程描述')


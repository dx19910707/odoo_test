# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'
    _description = '课程'

    name = fields.Char(string='课程标题', required=True)
    description = fields.Text(string='课程描述')


class Session(models.Model):
    _name = 'openacademy.session'
    _description = '学期'

    name = fields.Char(string='学期', required=True)
    start_date = fields.Date(string='开始日期')
    duration = fields.Float(digits=(6,2), help="本学期的持续时间", string='本学期的持续时间')
    seats = fields.Integer(string='本学期的座位数')

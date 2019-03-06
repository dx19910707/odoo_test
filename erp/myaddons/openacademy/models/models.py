# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'
    _description = '课程'

    name = fields.Char(string='课程标题', required=True)
    description = fields.Text(string='课程描述')
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="负责人", index=True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string='Sessions')


class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'session'

    name = fields.Char(string='session', required=True)
    start_date = fields.Date(string='开始日期')
    duration = fields.Float(digits=(6,2), help="持续时间", string='持续时间')
    seats = fields.Integer(string='座位数')
    instructor_id = fields.Many2one('res.partner', string="指导员")
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="课程", required=True)
    attendee_ids = fields.Many2many('res.partner', string="参加人员")

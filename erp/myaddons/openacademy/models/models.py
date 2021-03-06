# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Course(models.Model):
    _name = 'openacademy.course'
    _description = '课程'

    name = fields.Char(string='课程标题', required=True)
    description = fields.Text(string='课程描述')
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="负责人", index=True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string='Sessions')

    _sql_constraints = [
        ("name_description_check",
         "CHECK(name != description)",
         "课程名称和课程描述不能相同"),
        ("name_unique",
         "UNIQUE(name)",
         "已存在相同名称的课程")
    ]

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u'%{} - 复制'.format(self.name))])
        if not copied_count:
            new_name = '{} - 复制'.format(self.name)
        else:
            new_name = '{} - 复制({})'.format(self.name, copied_count)
        default['name'] = new_name
        return super(Course, self).copy(default)

class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'session'

    name = fields.Char(string='session', required=True)
    start_date = fields.Date(string='开始日期', default=fields.Date.today)
    duration = fields.Float(digits=(6,2), help="持续时间", string='持续时间')
    seats = fields.Integer(string='座位数')
    active = fields.Boolean(default=True)
    instructor_id = fields.Many2one('res.partner', string="指导员")
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="课程", required=True)
    attendee_ids = fields.Many2many('res.partner', string="参加人员")
    taken_seats = fields.Float(string='位置占用百分比', compute='_compute_taken_seats')

    @api.depends('seats', 'attendee_ids')
    def _compute_taken_seats(self):
        for item in self:
            if not item.seats:
                item.taken_seats = 0
            else:
                item.taken_seats = 100 * len(item.attendee_ids) / item.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_vaild_seats(self):
        if self.seats < 0:
            return {
                'warning':{
                    'title': "参数错误",
                    'message': "座位数必须是大于等于0的整数"
                }
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning':{
                    'title': "参数错误",
                    'message': "座位数不能小于出席人数"
                }
            }

    @api.constrains('instructor_id', 'attendee_ids')
    def _chech_instructor_not_in_attendees(self):
        if self.instructor_id and self.instructor_id in self.attendee_ids:
            raise exceptions.ValidationError('指导员不能参加这门session')

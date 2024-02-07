# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolTeacher(models.Model):
    
    _name = 'school.teacher'
    
    name = fields.Char(string="Nombre", required=True)
    profile = fields.Text(string="Perfil")
    subjects_ids = fields.One2many('school.subject', 'teacher_id', string="Materias", readonly=True)

    
    
    

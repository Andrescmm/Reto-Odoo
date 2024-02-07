# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolSubject(models.Model):
    
    _name = 'school.subject'
    
    name = fields.Char(string="Nombre", required=True)
    credits = fields.Integer(string="Creditos", required=True)
    max_students = fields.Integer(string="Maximo de Estudiantes", required=True)
    active = fields.Boolean(string="Active", default=True)
    students_ids = fields.Many2many('school.student', string="Estudiantes")
    teacher_id = fields.Many2one('school.teacher', string="Maestros")
    modality = fields.Selection(
        [('presencial', 'Presencial'), 
         ('virtual', 'Virtual')], 
        string="Modalidad", required=True)
    
    
    @api.constrains('students_ids')
    def check_max_students(self):
        for subject in self:
            if len(subject.students_ids) > subject.max_students:
                raise models.ValidationError("No se puede agregar mas estudiantes a la materia %s" % subject.name)
    

    
    

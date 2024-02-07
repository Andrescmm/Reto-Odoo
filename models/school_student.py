# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import models, fields, api


class SchoolStudent(models.Model):
    
    _name = 'school.student'
    
    name = fields.Char(string="Nombre", required=True)
    birthdate = fields.Date(string="Dia de Nacimiento", required=True)
    age = fields.Integer(string="Edad", compute="_compute_age")
    born_city = fields.Char(string="Ciudad de Nacimiento")
    doc_number = fields.Char(string="Numero de Documento", required=True)
    final_exam_grade = fields.Float(string="Calificación Final", required=True)
    subject_ids = fields.Many2many('school.subject', string="Materias")
    doc_type = fields.Selection(
        [('dni', 'DNI'), 
         ('ce', 'Carnet Extrajeria'), 
         ('pa', 'Pasaporte')], 
        string="Tipo de Documento", required=True)
    
    

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                birth_date = fields.Date.from_string(record.birthdate)
                today_date = fields.Date.from_string(fields.Date.today())
                delta = today_date - birth_date
                record.age = delta.days / 365
            else:
                record.age = 0.0 
    
    

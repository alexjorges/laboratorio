from odoo import models, fields, api

class Tecnico(models.Model):
    _name = 'laboratorio.tecnico'
    imagen = fields.Binary('foto')
    codigo = fields.Integer('Codigo Del tecnico', required=True)
    nombre = fields.Char('Nombre Del Tecnico', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    fecha = fields.Date(string='Fecha De Nacimiento', default=lambda s: fields.Date.context_today(s))
    cp = fields.Integer('Codigo Postal', required=True)
    direccion = fields.Char('Direccion', required=True)


    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res
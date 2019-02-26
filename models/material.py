from odoo import models, fields, api

class Material(models.Model):
    _name = 'laboratorio.material'
    tipo = fields.Char('Tipo De Material', required=True)
    codigo = fields.Integer('Codigo', required=True)
    cantidad = fields.Integer('cantidad', required=True)


    def name_get(self):
        res = []
        for record in self:
            tipo = record.tipo
            res.append((record.id, tipo))
        return res
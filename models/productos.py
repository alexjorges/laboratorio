from odoo import models, fields, api

class Productos(models.Model):
    _name = 'laboratorio.productos'
    codigo = fields.Integer('Codigo', required=True)
    nombre = fields.Char('Nombre Del Producto', required=True)
    cantidad = fields.Integer('Cantidad', required=True)

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res
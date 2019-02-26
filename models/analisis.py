from odoo import models, fields, api

class Analisis(models.Model):
    _name = 'laboratorio.analisis'
    tipo = fields.Char('Tipo de Analisis', required=True)
    codigo = fields.Integer('Codigo', required=True)
    material = fields.Many2many('laboratorio.material', string='Material')
    productos = fields.Many2many('laboratorio.productos', string='Productos')
    tecnico = fields.Many2one('laboratorio.tecnico', 'Tecnico')
    cliente = fields.Many2one('laboratorio.cliente', 'Cliente')
    resultado = fields.Char('Resultado del analisis', required=True);

    def name_get(self):
        res = []
        for record in self:
            tipo = record.tipo
            res.append((record.id, tipo))
        return res
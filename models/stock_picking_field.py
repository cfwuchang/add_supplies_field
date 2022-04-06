from odoo import api, fields, models, tools, _

class StockPickingField(models.Model):
    _inherit = 'stock.picking'

    x_department = fields.Many2one('hr.department',string=u'部门' )

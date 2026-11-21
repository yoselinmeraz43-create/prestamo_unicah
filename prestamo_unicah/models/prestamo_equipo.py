
from odoo import fields, models


class PrestamoEquipo(models.Model):
    _name = "prestamo.equipo"
    _description = "Equipo para préstamo"

    name = fields.Char(string="Nombre", required=True)

    codigo = fields.Char(
        string="Código de inventario",
        required=True,
        copy=False
    )

    categoria = fields.Selection(
        [
            ("laptop", "Laptop"),
            ("proyector", "Proyector"),
            ("audio", "Audio"),
            ("laboratorio", "Laboratorio"),
        ],
        string="Categoría",
        required=True,
        default="laptop",
    )

    estado = fields.Selection(
        [
            ("disponible", "Disponible"),
            ("prestado", "Prestado"),
            ("mantenimiento", "En mantenimiento"),
        ],
        string="Estado",
        required=True,
        default="disponible",
    )

    notas = fields.Text(string="Notas")

    active = fields.Boolean(string="Activo", default=True)

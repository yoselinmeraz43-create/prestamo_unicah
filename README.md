# Yoselin Grisel Solis

**Numero de cuenta:** 1522200600307

## Respuestas

### 1. Que pasa si arrastra una tarjeta del kanban a otra columna? Por que?

Cuando arrastro una tarjeta de una columna a otra, cambia la etapa o el estado en el que se encuentra el registro. Esto sucede porque cada columna representa una etapa diferente del proceso y Odoo guarda automaticamente el cambio realizado.

### 2. El campo prestamo_ids se agrego a res.partner. Se crea una columna nueva en la tabla de contactos? Explique.

No, no se crea una columna nueva en la tabla de contactos. Esto se debe a que `prestamo_ids` es un campo de tipo One2many, que permite relacionar un contacto con varios registros de prestamos. La relacion se almacena mediante el campo Many2one que existe en el modelo de prestamos, por lo que no es necesario crear una columna adicional en la tabla de contactos.
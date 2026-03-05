# Copyright (c) 2026, red and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Alimento(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		descrição: DF.Data | None
		nome: DF.Data
		observação: DF.Data | None
		tipo_materia_prima: DF.Literal["Teste"]
		unidade_medida: DF.Literal["kg", "g", "L", "mL", "unidade"]
	# end: auto-generated types

	pass

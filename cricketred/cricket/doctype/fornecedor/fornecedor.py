# Copyright (c) 2026, red and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Fornecedor(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		email: DF.Data | None
		enabled: DF.Check
		localidade: DF.Data | None
		morada: DF.SmallText | None
		nif: DF.Data
		nome_fiscal: DF.Data
		telefone: DF.Data | None
		website: DF.Data | None
	# end: auto-generated types

	pass

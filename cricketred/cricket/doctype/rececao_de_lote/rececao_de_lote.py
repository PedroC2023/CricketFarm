# Copyright (c) 2026, red and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RececaodeLote(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		data_rececao: DF.Date
		enabled: DF.Check
		fornecedor: DF.Link
	# end: auto-generated types

	pass

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Item Label",
			"category": "Modules",
			"color": "red",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"disable_after_onboard": 1,
			"label": _("Item Label"),
			"description": "Barcode Label for Custom Items",
			"onboard_present": 1
		}
	]

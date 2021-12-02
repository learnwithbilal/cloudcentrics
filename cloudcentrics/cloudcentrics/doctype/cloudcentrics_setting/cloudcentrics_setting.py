# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import cint
from cloudcentrics.api import get_frappe_version


class CloudcentricsSetting(Document):
    def validate(self):
        if cint(get_frappe_version()) >= 13:
            if self.cloudcentrics_app_name:
                frappe.db.set_value(
                    "System Settings", "System Settings", "app_name", self.cloudcentrics_app_name)
            else:
                if "erpnext" in frappe.get_installed_apps():
                    frappe.db.set_value(
                        "System Settings", "System Settings", "app_name", "ERPNext")
                else:
                    frappe.db.set_value(
                        "System Settings", "System Settings", "app_name", "Frappe")

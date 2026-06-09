import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate, today


class InvitationCode(Document):
    def autoname(self):
        self.code = self.generate_unique_code()
        self.name = self.code

    def before_insert(self):
        if not self.status:
            self.status = "Available"

    def validate(self):
        self.validate_valid_until()

    def generate_unique_code(self):
        for _ in range(10):
            code = f"INV-{frappe.generate_hash(length=8).upper()}"

            if not frappe.db.exists("Invitation Code", code):
                return code

        frappe.throw(_("Unable to generate a unique invitation code. Please try again."))

    def validate_valid_until(self):
        if self.is_new() and self.valid_until:
            if getdate(self.valid_until) < getdate(today()):
                frappe.throw(_("Valid Until date cannot be in the past."))

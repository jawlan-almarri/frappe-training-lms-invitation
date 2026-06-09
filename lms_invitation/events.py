import frappe
from frappe import _
from frappe.utils import getdate, today


def validate_student_enrollment(doc, method=None):
    if not getattr(doc, "invitation_code", None):
        return

    invitation_code = frappe.get_doc("Invitation Code", doc.invitation_code)

    if invitation_code.course != doc.course:
        frappe.throw(
            _("The selected Invitation Code does not belong to the selected Course.")
        )

    if invitation_code.status != "Available":
        frappe.throw(
            _("The selected Invitation Code is not available.")
        )

    if invitation_code.valid_until and getdate(invitation_code.valid_until) < getdate(today()):
        frappe.throw(
            _("The selected Invitation Code has expired.")
        )


def mark_invitation_code_as_used(doc, method=None):
    if not getattr(doc, "invitation_code", None):
        return

    invitation_code = frappe.get_doc("Invitation Code", doc.invitation_code)

    if invitation_code.status == "Available":
        frappe.db.set_value(
            "Invitation Code",
            doc.invitation_code,
            "status",
            "Used"
        )

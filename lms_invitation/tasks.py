import frappe
from frappe.utils import today


def expire_invitation_codes():
    expired_codes = frappe.get_all(
        "Invitation Code",
        filters={
            "status": "Available",
            "valid_until": ["<", today()],
        },
        pluck="name",
    )

    for code in expired_codes:
        frappe.db.set_value(
            "Invitation Code",
            code,
            "status",
            "Expired"
        )

import frappe
from frappe import _


def before_install():
    """Run before installation"""
    # Check for dependencies
    check_dependencies()


def check_dependencies():
    """Check if required apps are installed."""
    missing = []
    installed = frappe.get_installed_apps()
    if not installed or "erpnext" not in installed:
        missing.append("erpnext")
    if "hrms" not in installed:
        missing.append("hrms")

    if missing:
        frappe.throw(_("Cannot install this app. Missing required app(s): {}").format(", ".join(missing)))

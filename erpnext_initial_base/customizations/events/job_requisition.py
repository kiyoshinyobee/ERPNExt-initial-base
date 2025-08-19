import frappe

def set_requested_by(doc, method):
    """ set requested_by field to the current user if not set """
    """ to covering some conditions if field  perm level is set higher than 0 and user doesn't have write permission """
    meta = frappe.get_meta(doc.doctype)
    df = meta.get_field("requested_by")
    if getattr(df, "ignore_user_permissions", 0):
        if doc.get("requested_by"):
            return
        else:
            emp_id = frappe.get_value(
                "Employee",
                {"user_id": frappe.session.user, "status": "Active"},
                "name"
            )
            if emp_id:
                doc.requested_by = emp_id


def run_all_before_validate(doc, method):
    """ Run all hooks before validate """
    hooks = [
        set_requested_by,
        # add more before validate methods here
    ]
    for hook in hooks:
        hook(doc, method)

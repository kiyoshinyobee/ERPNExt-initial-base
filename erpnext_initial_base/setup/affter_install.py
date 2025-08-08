import frappe

def after_install():
    """Run before migration"""
    # Remove all role profiles
    remove_all_role_profiles()
    # disabled all roles except specified ones
    update_role_status()
    # remove gender except male and female
    update_gender_list()


def remove_all_role_profiles():
    """Remove all role profiles except specified ones."""
    names_to_remove = ["Accounts", "HR", "Inventory", "Manufacturing", "Purchase", "Sales"]
    frappe.db.delete("Role Profile", {"name": ["in", names_to_remove]})


def update_role_status():
    """Disable all roles except specified ones, but only if currently enabled."""
    excluded_roles = ["Administrator", "All", "Guest", "Desk User", "System Manager", "Script Manager"]
    frappe.db.set_value(
        "Role",
        {
            "name": ["not in", excluded_roles],
            "disabled": 0
        },
        "disabled",
        1,
        update_modified=False
    )


def update_gender_list():
    """Remove all records from Gender except 'Male' and 'Female'."""
    frappe.db.delete("Gender", {"gender": ["not in", ["Male", "Female"]]})

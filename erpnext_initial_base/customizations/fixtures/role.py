# pre-defined custom role
pre_defined_roles = [
    # staffing plan
    "HR-Staffing Plan (Viewer)",
    "HR-Staffing Plan (Creator)",
    "HR-Staffing Plan (Editor)",
    "HR-Staffing Plan (Approver)",
    "HR-Staffing Plan (Amender)",

    # job requisition
    "HR-Job Requisition (Viewer)",
    "HR-Job Requisition (Creator)",
    "HR-Job Requisition (Approver)",
    "HR-Job Requisition (Editor)",
    "HR-Job Requisition (Lv1-Read Only)",
    "HR-Job Requisition (Lv1-Read Write)",

    # job opening
    "HR-Job Opening (viewer)",
    "HR-Job Opening (creator)",

    # job applicant
    "HR-Job Applicant (Viewer)",
    "HR-Job Applicant (Creator)",

    # job offer

    # employee referral
    "HR-Employee Referral (Viewer)",
    "HR-Employee Referral (Creator)",
]

role_fixtures = [
    {
        "dt": "Role",
        "filters": [
            ["is_custom", "=", 1],
            ["name", "in", pre_defined_roles],
        ],
    },
]

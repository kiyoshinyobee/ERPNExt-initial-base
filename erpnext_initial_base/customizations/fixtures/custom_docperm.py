from .role import pre_defined_roles

# pre-defined custom role profile assignment
custom_docperm_fixtures = [
    {
        "dt": "Custom DocPerm",
        "filters": [
            ["role", "in", pre_defined_roles]
        ],
    },
]

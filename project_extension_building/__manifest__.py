# Copyright 2018 Mikel Arregi Etxaniz - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Project extension building",
    "version": "11.0.1.0.0",
    "license": "AGPL-3",
    "summary": """Add link to center data""",
    "author":  "AvanzOSC",
    "website": "http://www.avanzosc.es",
    "category": "Project",
    "depends": [
        "project",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/project_project_view.xml",
        "views/work_type_view.xml",
    ],
    "installable": True,
}

# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Character Curriculum Map / Annual Syllabus - Operating Unit",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": (
        "OpenSynergy Indonesia, "
        "PT. Simetri Sinergi Indonesia, "
        "Odoo Community Association (OCA)"
    ),
    "license": "AGPL-3",
    "installable": True,
    "application": False,
    "depends": [
        "ssi_school_character_curriculum",
        "ssi_operating_unit_mixin",
        "web_tour",
    ],
    "data": [
        # Security - shared "Operating Unit" group + Manager tier wiring
        "security/res_groups/school_character_curriculum.xml",
        # Security - transactional (school_character_curriculum)
        "security/ir_rule/school_character_curriculum.xml",
        # Views
        "views/school_character_curriculum.xml",
        "views/assets.xml",
    ],
    "demo": [],
}

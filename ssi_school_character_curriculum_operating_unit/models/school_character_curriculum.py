# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class SchoolCharacterCurriculum(models.Model):  # pylint: disable=too-few-public-methods
    """
    Extends Character Curriculum Map / Annual Syllabus with single
    operating unit support, restricting each character curriculum map
    document to one operating unit.
    """

    _name = "school_character_curriculum"
    _inherit = [
        "school_character_curriculum",
        "mixin.single_operating_unit",
    ]

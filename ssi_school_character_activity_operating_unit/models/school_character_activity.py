# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class SchoolCharacterActivity(models.Model):  # pylint: disable=too-few-public-methods
    """
    Extends Character Learning Activity with single operating unit support,
    restricting each character learning activity document to one operating
    unit.
    """

    _name = "school_character_activity"
    _inherit = [
        "school_character_activity",
        "mixin.single_operating_unit",
    ]

# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class SchoolCharacterGrowthReport(
    models.Model
):  # pylint: disable=too-few-public-methods
    """
    Extends Character Growth Report with single operating unit support,
    restricting each character growth report document to one operating
    unit.
    """

    _name = "school_character_growth_report"
    _inherit = [
        "school_character_growth_report",
        "mixin.single_operating_unit",
    ]

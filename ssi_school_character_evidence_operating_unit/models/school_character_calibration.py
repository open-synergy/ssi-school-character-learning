# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class SchoolCharacterCalibration(
    models.Model
):  # pylint: disable=too-few-public-methods
    """
    Extends Character Teacher Calibration with single operating unit support,
    restricting each teacher calibration session to one operating unit.
    """

    _name = "school_character_calibration"
    _inherit = [
        "school_character_calibration",
        "mixin.single_operating_unit",
    ]

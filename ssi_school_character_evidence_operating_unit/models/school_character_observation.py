# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class SchoolCharacterObservation(
    models.Model
):  # pylint: disable=too-few-public-methods
    """
    Extends Character Observation with single operating unit support,
    restricting each character observation document to one operating unit.
    """

    _name = "school_character_observation"
    _inherit = [
        "school_character_observation",
        "mixin.single_operating_unit",
    ]

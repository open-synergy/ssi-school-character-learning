# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SchoolCharacterCalibrationRating(models.Model):
    """
    Represents a single rating line of a Teacher Calibration session (ICLAD
    v2.3 Bab 18): the scale level that one participant assigned to one
    calibrated anchor example. Comparing the levels assigned by the different
    participants to the same anchor is what yields the session's inter-rater
    agreement.
    """

    _name = "school_character_calibration.rating"
    _description = "Character Teacher Calibration Rating"
    _order = "calibration_id, anchor_id, id"

    calibration_id = fields.Many2one(
        string="# Calibration",
        comodel_name="school_character_calibration",
        required=True,
        ondelete="cascade",
        help="The calibration session this rating line belongs to.",
    )
    participant_id = fields.Many2one(
        string="Participant",
        comodel_name="school_teacher",
        required=False,
        help="The teacher who gave this rating.",
    )
    anchor_id = fields.Many2one(
        string="Anchor",
        comodel_name="school_character_anchor",
        required=False,
        help="The calibrated anchor example that was rated.",
    )
    assigned_level_id = fields.Many2one(
        string="Assigned Level",
        comodel_name="school_character_level",
        required=False,
        help=(
            "The scale level this participant assigned to the anchor example, "
            "from the configured character scale."
        ),
    )

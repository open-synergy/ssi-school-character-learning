# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SchoolCharacterAnchor(models.Model):  # pylint: disable=too-few-public-methods
    """
    Represents a calibrated Anchor example, per the ICLAD v2.3 assessment
    calibration section (Bab 18.3): a concrete, agreed-upon sample of
    performance pinned to a specific construct and level, used to keep
    assessors calibrated when they score real evidence. Anchors are master
    data so each school builds and maintains its own calibration set.
    """

    _name = "school_character_anchor"
    _inherit = ["mixin.master_data"]
    _description = "Character Anchor"

    construct_id = fields.Many2one(
        string="Construct",
        comodel_name="school_character_construct",
        required=True,
        ondelete="cascade",
        help="Construct this anchor example calibrates.",
    )
    level_id = fields.Many2one(
        string="Level",
        comodel_name="school_character_level",
        required=True,
        help="Scale level this anchor example represents.",
    )
    grade_type_id = fields.Many2one(
        string="Grade Type",
        comodel_name="school_grade_type",
        help="Optional education level (grade type) this anchor example is "
        "calibrated for.",
    )
    sample_text = fields.Text(
        string="Sample",
        help="The concrete sample of performance that anchors this construct "
        "at this level.",
    )
    source_type = fields.Selection(
        string="Source Type",
        selection=[
            ("observation", "Observation"),
            ("artifact", "Artifact/Work Product"),
            ("self_report", "Self Report"),
            ("peer_report", "Peer Report"),
            ("teacher_report", "Teacher Report"),
        ],
        help="Kind of evidence this anchor sample was drawn from. The values "
        "mirror the evidence source types used when recording real character "
        "evidence, so anchors and evidence stay comparable.",
    )

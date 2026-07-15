# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SchoolCharacterGrowthReportLine(models.Model):
    """
    Represents a single per-construct growth line of a Character Growth Report
    (ICLAD v2.3 Growth Profile, Bab 21). Each line records, for one character
    construct, the level the student achieved on the configured scale, the
    growth narrative describing how the student grew, the feedforward next step
    to pursue, and the character evidence entries that support the line.

    DATA GOVERNANCE BOUNDARY (ICLAD Bab 17 & Bab 14): the only admissible
    evidence source on this line is legitimate character evidence
    (``evidence_ids``). The narrative and next-step fields are free-text growth
    language with no fixed labels or scores. This line holds NO relation to any
    discipline, counseling, psychological-test, or safeguarding record.
    """

    _name = "school_character_growth_report.line"
    _description = "Character Growth Report Line"
    _order = "report_id, id"

    report_id = fields.Many2one(
        string="# Growth Report",
        comodel_name="school_character_growth_report",
        required=True,
        ondelete="cascade",
        help="The character growth report document this line belongs to.",
    )
    construct_id = fields.Many2one(
        string="Construct",
        comodel_name="school_character_construct",
        required=True,
        help="The character construct this growth line profiles.",
    )
    level_id = fields.Many2one(
        string="Achieved Level",
        comodel_name="school_character_level",
        required=False,
        help=(
            "The scale level the student achieved for this construct, taken "
            "from the configured character scale. Never hardcoded."
        ),
    )
    narrative = fields.Text(
        string="Growth Narrative",
        required=False,
        help=(
            "The formative narrative describing how the student grew on this "
            "construct, phrased as growth language (ICLAD Bab 14.4). Free text "
            "with no fixed labels or scores."
        ),
    )
    next_step = fields.Text(
        string="Next Step",
        required=False,
        help=(
            "The feedforward next step for the student to pursue on this "
            "construct, phrased as growth language."
        ),
    )
    evidence_ids = fields.Many2many(
        string="Evidence Entries",
        comodel_name="school_character_observation.evidence",
        relation="rel_character_growth_report_line_2_evidence",
        column1="line_id",
        column2="evidence_id",
        help=(
            "The character evidence entries that support this growth line, "
            "drawn only from legitimate character observations (the sole "
            "admissible evidence source)."
        ),
    )
    evidence_count = fields.Integer(
        string="Evidence Count",
        compute="_compute_evidence_count",
        store=True,
        help="Number of evidence entries linked to this growth line.",
    )

    @api.depends("evidence_ids")
    def _compute_evidence_count(self):
        for record in self:
            record.evidence_count = len(record.evidence_ids)

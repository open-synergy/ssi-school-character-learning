# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SchoolCharacterIndicator(models.Model):  # pylint: disable=too-few-public-methods
    """
    Represents a developmental Indicator, an observable behaviour that
    evidences a Character Construct (or one of its sub-constructs), per the
    ICLAD v2.3 assessment section (Bab 8). An indicator may be positive (a
    behaviour to look for) or a non-indicator (a behaviour that must NOT be
    read as evidence of the construct). The cognitive-demand tags (RBT, DOK,
    SOLO) reference standard, subject-neutral learning taxonomies so the
    indicator can be calibrated without hard-coding any school's values.
    """

    _name = "school_character_indicator"
    _inherit = [
        "mixin.master_data",
        "school_character_code_constraint_mixin",
    ]
    _description = "Character Indicator"

    construct_id = fields.Many2one(
        string="Construct",
        comodel_name="school_character_construct",
        required=True,
        ondelete="cascade",
        help="Construct this indicator provides evidence for.",
    )
    subconstruct_id = fields.Many2one(
        string="Sub-construct",
        comodel_name="school_character_subconstruct",
        help="Optional sub-construct this indicator provides evidence for, "
        "when the indicator targets a specific facet of the construct.",
    )
    grade_type_id = fields.Many2one(
        string="Grade Type",
        comodel_name="school_grade_type",
        help="Optional education level (grade type) this indicator is "
        "calibrated for, e.g. an indicator worded for a particular stage of "
        "schooling.",
    )
    grade_id = fields.Many2one(
        string="Grade",
        comodel_name="school_grade",
        help="Optional grade this indicator is calibrated for, when it is "
        "specific to a single grade rather than a whole grade type.",
    )
    indicator_type = fields.Selection(
        string="Indicator Type",
        selection=[
            ("positive", "Positive Indicator"),
            ("non_indicator", "Non-indicator"),
        ],
        default="positive",
        help="Whether this is a Positive Indicator (a behaviour that counts "
        "as evidence of the construct) or a Non-indicator (a behaviour that "
        "must explicitly NOT be read as evidence of the construct).",
    )
    rbt_level = fields.Selection(
        string="RBT Level",
        selection=[
            ("remember", "Remember"),
            ("understand", "Understand"),
            ("apply", "Apply"),
            ("analyze", "Analyze"),
            ("evaluate", "Evaluate"),
            ("create", "Create"),
        ],
        help="Cognitive level of this indicator on the Revised Bloom's "
        "Taxonomy (ICLAD Bab 8).",
    )
    dok_level = fields.Selection(
        string="DOK Level",
        selection=[
            ("1", "DOK 1 - Recall"),
            ("2", "DOK 2 - Skill/Concept"),
            ("3", "DOK 3 - Strategic Thinking"),
            ("4", "DOK 4 - Extended Thinking"),
        ],
        help="Depth of Knowledge level of this indicator (ICLAD Bab 8).",
    )
    solo_level = fields.Selection(
        string="SOLO Level",
        selection=[
            ("prestructural", "Prestructural"),
            ("unistructural", "Unistructural"),
            ("multistructural", "Multistructural"),
            ("relational", "Relational"),
            ("extended_abstract", "Extended Abstract"),
        ],
        help="Structure of the Observed Learning Outcome (SOLO taxonomy) "
        "level of this indicator (ICLAD Bab 8).",
    )
    description = fields.Text(
        string="Description",
        help="Full wording of the observable behaviour that this indicator "
        "describes.",
    )

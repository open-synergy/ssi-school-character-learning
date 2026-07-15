# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SchoolCharacterActivityAlignment(models.Model):
    """
    Represents a single alignment-gate line of a Character Learning Activity
    (ICLAD Bab 8). Each line keeps the learning objective (RBT), the
    delivered activity (DOK), the planned evidence, the success rubric (SOLO),
    and the feedback plan aligned to one behavioral indicator, so that what is
    taught, what is done, and what is evidenced remain consistent.
    """

    _name = "school_character_activity.alignment"
    _description = "Character Learning Activity Alignment Gate"

    activity_id = fields.Many2one(
        string="# Activity",
        comodel_name="school_character_activity",
        required=True,
        ondelete="cascade",
        help="The character learning activity document this line belongs to.",
    )
    activity_construct_id = fields.Many2one(
        string="Activity Construct",
        comodel_name="school_character_construct",
        related="activity_id.construct_id",
        store=False,
        help=(
            "The construct of the parent activity, used to restrict the "
            "indicator choices on this line to that construct."
        ),
    )
    indicator_id = fields.Many2one(
        string="Indicator",
        comodel_name="school_character_indicator",
        required=False,
        help=(
            "The behavioral indicator that this alignment line observes as "
            "evidence of the construct."
        ),
    )
    objective_rbt = fields.Text(
        string="Objective (RBT)",
        help=(
            "The learning objective for this line, phrased on the Revised "
            "Bloom's Taxonomy (the intended thinking level)."
        ),
    )
    activity_dok = fields.Text(
        string="Activity (DOK)",
        help=(
            "The activity to be delivered for this line, described at its "
            "Depth of Knowledge (the actual cognitive demand)."
        ),
    )
    planned_evidence = fields.Text(
        string="Planned Evidence",
        help=(
            "The evidence the activity is planned to produce (work product, "
            "observation, artifact) that shows the objective was met."
        ),
    )
    solo_rubric = fields.Text(
        string="SOLO Rubric",
        help=(
            "The success criteria / rubric phrased on the SOLO taxonomy used "
            "to judge the quality of the evidence for this line."
        ),
    )
    feedback_plan = fields.Text(
        string="Feedback Plan",
        help=(
            "How feedback will be given to the learner on this line to close "
            "the learning loop."
        ),
    )

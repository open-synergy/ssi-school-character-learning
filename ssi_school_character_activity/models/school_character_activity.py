# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import date as datetime_date

from odoo import fields, models

from odoo.addons.ssi_decorator import ssi_decorator


class SchoolCharacterActivity(models.Model):
    """
    Represents a Character Learning Activity document: the learning-design
    cycle and the delivered activity used as a practice arena for character
    formation (ICLAD Design Cycle, Bab 8 & Bab 10). One document unites the
    learning objective (RBT) with the delivered activity (DOK), the planned
    evidence and success criteria (SOLO), and the feedback plan, all tied to
    a character construct/arena/method and (optionally) to a Character
    Curriculum Map.

    This is a transactional document with a full approval workflow:
    Draft -> Confirm -> Approve -> Open -> Done / Cancel. The concrete
    objective, activity, and cognitive-demand levels (RBT/DOK/SOLO) are
    filled in per school by the user; nothing is hardcoded. This document
    deliberately does NOT link to any discipline or counseling data (data
    governance boundary).
    """

    _name = "school_character_activity"
    _inherit = [
        "mixin.transaction_cancel",
        "mixin.transaction_done",
        "mixin.transaction_open",
        "mixin.transaction_confirm",
    ]
    _description = "Character Learning Activity"

    # Multiple Approval Attribute
    _approval_from_state = "draft"
    _approval_to_state = "open"
    _approval_state = "confirm"
    _after_approved_method = "action_open"

    # Attributes related to add element on view automatically
    _automatically_insert_view_element = True
    _automatically_insert_open_policy_fields = False
    _automatically_insert_open_button = False

    _statusbar_visible_label = "draft,confirm,open,done"
    _policy_field_order = [
        "confirm_ok",
        "approve_ok",
        "reject_ok",
        "restart_approval_ok",
        "done_ok",
        "cancel_ok",
        "restart_ok",
        "manual_number_ok",
    ]
    _header_button_order = [
        "action_confirm",
        "action_approve_approval",
        "action_reject_approval",
        "%(ssi_transaction_cancel_mixin.base_select_cancel_reason_action)d",
        "action_done",
        "action_restart",
    ]

    # Attributes related to add element on search view automatically
    _state_filter_order = [
        "dom_draft",
        "dom_confirm",
        "dom_reject",
        "dom_open",
        "dom_done",
        "dom_cancel",
    ]

    # Sequence attribute
    _create_sequence_state = "open"

    date = fields.Date(
        string="Document Date",
        default=lambda self: datetime_date.today(),
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help="The date this Character Learning Activity document was drawn up.",
    )
    date_end = fields.Date(
        string="End Date",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "The date the delivered activity ends. Leave empty for a "
            "single-session activity."
        ),
    )
    curriculum_id = fields.Many2one(
        string="Curriculum Map",
        comodel_name="school_character_curriculum",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "The Character Curriculum Map this activity delivers on. Optional: "
            "an activity may be designed independently of a formal map."
        ),
    )
    construct_id = fields.Many2one(
        string="Construct",
        comodel_name="school_character_construct",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help="The character construct this learning activity develops.",
    )
    subconstruct_id = fields.Many2one(
        string="Sub-construct",
        comodel_name="school_character_subconstruct",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "The specific sub-construct this activity targets, when the design "
            "is more granular than the construct itself."
        ),
    )
    arena_id = fields.Many2one(
        string="Arena",
        comodel_name="school_character_arena",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "The arena/program (e.g. classroom, project, live-in) that hosts "
            "this activity as a practice ground for the construct."
        ),
    )
    method_id = fields.Many2one(
        string="Method",
        comodel_name="school_character_method",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help="The character-development method applied in this activity.",
    )
    grade_class_id = fields.Many2one(
        string="Grade Class",
        comodel_name="school_grade_class",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help="The homeroom class that carries out this learning activity.",
    )
    teacher_id = fields.Many2one(
        string="Teacher",
        comodel_name="school_teacher",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help="The teacher who designs and facilitates this learning activity.",
    )
    objective = fields.Text(
        string="Learning Objective (RBT)",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "The learning objective for this activity, phrased on the Revised "
            "Bloom's Taxonomy (ICLAD Bab 8)."
        ),
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
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "Cognitive level of the objective on the Revised Bloom's Taxonomy "
            "(ICLAD Bab 8)."
        ),
    )
    dok_level = fields.Selection(
        string="DOK Level",
        selection=[
            ("1", "DOK 1 - Recall"),
            ("2", "DOK 2 - Skill/Concept"),
            ("3", "DOK 3 - Strategic Thinking"),
            ("4", "DOK 4 - Extended Thinking"),
        ],
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=("Depth of Knowledge level of the delivered activity (ICLAD Bab 8)."),
    )
    solo_target = fields.Selection(
        string="SOLO Target",
        selection=[
            ("prestructural", "Prestructural"),
            ("unistructural", "Unistructural"),
            ("multistructural", "Multistructural"),
            ("relational", "Relational"),
            ("extended_abstract", "Extended Abstract"),
        ],
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "The target Structure of the Observed Learning Outcome (SOLO "
            "taxonomy) that the planned evidence should reach (ICLAD Bab 8)."
        ),
    )
    description = fields.Text(
        string="Description",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help="Free-text description of the delivered learning activity.",
    )
    alignment_ids = fields.One2many(
        string="Alignment Gate",
        comodel_name="school_character_activity.alignment",
        inverse_name="activity_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "The RBT-DOK-SOLO alignment-gate lines (ICLAD Bab 8): for each "
            "objective, the activity, planned evidence, success rubric, and "
            "feedback plan that keep objective, activity, and evidence aligned."
        ),
    )

    @ssi_decorator.insert_on_form_view()
    def _insert_form_element(self, view_arch):
        if self._automatically_insert_view_element:
            view_arch = self._reconfigure_statusbar_visible(view_arch)
        return view_arch

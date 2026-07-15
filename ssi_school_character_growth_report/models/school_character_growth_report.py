# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

from odoo.addons.ssi_decorator import ssi_decorator


class SchoolCharacterGrowthReport(models.Model):
    """
    Represents a Character Growth Profile / Report document: the formative,
    narrative growth report of one student's character for one academic term
    (ICLAD v2.3 Reporting, Bab 14 & Growth Profile, Bab 21). The header gathers
    the student, the academic year and term, the homeroom teacher, the learning
    pathway, and the calibration session that validates the scoring, together
    with an overall narrative. Per-construct detail (the achieved level, the
    growth narrative, the feedforward next step, and the linked evidence) is
    kept on the report lines.

    This is a transactional document with a full approval workflow:
    Draft -> Confirm -> Approve -> Open -> Done / Cancel. Levels and narrative
    are configured per school; nothing is hardcoded. The report is deliberately
    NON-labeling, NON-ranking, and carries no moral score.

    DATA GOVERNANCE BOUNDARY (ICLAD Bab 17 & Bab 14): this report holds NO link
    to any discipline, counseling, psychological-test, or safeguarding record.
    Its only admissible evidence source is the legitimate character evidence
    linked through the report lines' evidence entries. The narrative fields are
    free-text "growth language" (ICLAD Bab 14.4) with no fixed labels or scores.
    """

    _name = "school_character_growth_report"
    _inherit = [
        "mixin.transaction_cancel",
        "mixin.transaction_done",
        "mixin.transaction_open",
        "mixin.transaction_confirm",
    ]
    _description = "Character Growth Report"

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
        default=lambda self: fields.Date.context_today(self),
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help="The date this Character Growth Report document was drawn up.",
    )
    student_id = fields.Many2one(
        string="Student",
        comodel_name="school_student",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help="The student whose character growth this report profiles.",
    )
    academic_year_id = fields.Many2one(
        string="Academic Year",
        comodel_name="school_academic_year",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help="The academic year this growth report covers.",
    )
    academic_term_id = fields.Many2one(
        string="Academic Term",
        comodel_name="school_academic_term",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help="The academic term this growth report covers.",
    )
    homeroom_teacher_id = fields.Many2one(
        string="Homeroom Teacher",
        comodel_name="school_teacher",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help="The homeroom teacher who compiles this growth report.",
    )
    pathway = fields.Selection(
        string="Pathway",
        selection=[
            ("lite", "Lite"),
            ("core", "Core"),
            ("full", "Full"),
        ],
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "The character-learning pathway (lite/core/full) this report is "
            "compiled at, chosen per school."
        ),
    )
    calibration_id = fields.Many2one(
        string="Calibration",
        comodel_name="school_character_calibration",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "The teacher calibration session that validates the scoring behind "
            "this report, kept as a validation reference."
        ),
    )
    overall_narrative = fields.Text(
        string="Overall Narrative",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "The overall, formative growth narrative for the student across "
            "this term, phrased as growth language (ICLAD Bab 14.4). Free text "
            "with no fixed labels or scores."
        ),
    )
    line_ids = fields.One2many(
        string="Growth Lines",
        comodel_name="school_character_growth_report.line",
        inverse_name="report_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "The per-construct growth lines: for each construct the achieved "
            "level, the growth narrative, the feedforward next step, and the "
            "linked character evidence."
        ),
    )

    @ssi_decorator.insert_on_form_view()
    def _insert_form_element(self, view_arch):
        if self._automatically_insert_view_element:
            view_arch = self._reconfigure_statusbar_visible(view_arch)
        return view_arch

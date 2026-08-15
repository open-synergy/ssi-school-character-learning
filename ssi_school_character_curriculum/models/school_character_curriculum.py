# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import date as datetime_date

from odoo import api, fields, models

from odoo.addons.ssi_decorator import ssi_decorator


class SchoolCharacterCurriculum(models.Model):
    """
    Represents a Character Curriculum Map / Annual Syllabus document: the
    planning artifact that maps character constructs (from the Character
    Framework master data) to priority arenas/programs and learning
    outcomes (Capaian Pembelajaran) for a given academic year, term, and
    grade/class. It is the "Character Curriculum Map & Annual Syllabus"
    described by ICLAD (Design Cycle and the Lite/Core/Full pathway).

    This is a transactional document with a full approval workflow:
    Draft -> Confirm -> Approve -> Open -> Done / Cancel. The concrete
    mapping (which construct goes to which arena, target level, and
    learning outcome) is configured per school by the user; nothing is
    hardcoded. This document deliberately does NOT link to any discipline
    or counseling data (data governance boundary).
    """

    _name = "school_character_curriculum"
    _inherit = [
        "mixin.transaction_cancel",
        "mixin.transaction_done",
        "mixin.transaction_open",
        "mixin.transaction_confirm",
    ]
    _description = "Character Curriculum Map / Annual Syllabus"

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
        help="The date this Character Curriculum Map document was drawn up.",
    )
    academic_year_id = fields.Many2one(
        string="Academic Year",
        comodel_name="school_academic_year",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help="The academic year this character curriculum map applies to.",
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
        help=(
            "The academic term/semester this character curriculum map "
            "applies to. Leave empty for a whole-year map."
        ),
    )
    school_id = fields.Many2one(
        string="School",
        comodel_name="school",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help="The school this character curriculum map applies to.",
    )
    grade_id = fields.Many2one(
        string="Grade",
        comodel_name="school_grade",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help="The grade/level this character curriculum map targets.",
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
        help=(
            "The specific homeroom class this character curriculum map "
            "targets. Leave empty for a grade-wide map."
        ),
    )
    profile_id = fields.Many2one(
        string="Character Profile",
        comodel_name="school_character_profile",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "The character profile (framework of constructs) this map is "
            "derived from."
        ),
    )
    pathway = fields.Selection(
        string="Pathway",
        selection=[
            ("lite", "Lite"),
            ("core", "Core"),
            ("full", "Full"),
        ],
        default="core",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "Implementation pathway of this character curriculum map "
            "(ICLAD Lite/Core/Full), reflecting the depth and coverage "
            "the school commits to for the period."
        ),
    )
    line_ids = fields.One2many(
        string="Curriculum Lines",
        comodel_name="school_character_curriculum.line",
        inverse_name="curriculum_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "The construct-to-arena mapping lines of this character "
            "curriculum map: for each prioritized construct, the arena/"
            "program, method, target level, and learning outcome."
        ),
    )

    @ssi_decorator.insert_on_form_view()
    def _insert_form_element(self, view_arch):
        if self._automatically_insert_view_element:
            view_arch = self._reconfigure_statusbar_visible(view_arch)
        return view_arch

    @api.model
    def _get_policy_field(self):
        """Register this model's policy fields for ``mixin.policy``.

        ``open_ok`` (from ``mixin.transaction_open``) must be listed
        here too, alongside the existing ``_policy_field_order``.

        :return: the base policy fields of the standard four-mixin
            workflow combo
        """
        res = super()._get_policy_field()
        policy_field = [
            "confirm_ok",
            "approve_ok",
            "reject_ok",
            "restart_approval_ok",
            "done_ok",
            "cancel_ok",
            "restart_ok",
            "manual_number_ok",
            "open_ok",
        ]
        res += policy_field
        return res

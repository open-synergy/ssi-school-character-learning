# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models

from odoo.addons.ssi_decorator import ssi_decorator


class SchoolCharacterCalibration(models.Model):
    """
    Represents a Teacher Calibration session document (ICLAD v2.3 assessment
    calibration section, Bab 18): a working session in which several teachers
    independently rate the same set of calibrated anchor examples, so that
    inter-rater reliability can be measured and kept high before real
    character evidence is scored.

    Each session records which constructs it covers, which teachers took part,
    which anchor examples were rated, and the level each participant assigned
    to each anchor (the rating lines). The overall agreement result (e.g. the
    percentage of ratings within one level of each other) is recorded on the
    header.

    This is a transactional document with a full approval workflow:
    Draft -> Confirm -> Approve -> Open -> Done / Cancel. Levels come from the
    configured character scale; nothing is hardcoded. The session holds NO
    link to any discipline or counseling data (data governance boundary,
    ICLAD Bab 17).
    """

    _name = "school_character_calibration"
    _inherit = [
        "mixin.transaction_cancel",
        "mixin.transaction_done",
        "mixin.transaction_open",
        "mixin.transaction_confirm",
    ]
    _description = "Character Teacher Calibration"

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
        help="The date this teacher calibration session took place.",
    )
    construct_ids = fields.Many2many(
        string="Constructs",
        comodel_name="school_character_construct",
        relation="rel_character_calibration_2_construct",
        column1="calibration_id",
        column2="construct_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help="The character constructs whose scoring this session calibrates.",
    )
    participant_ids = fields.Many2many(
        string="Participants",
        comodel_name="school_teacher",
        relation="rel_character_calibration_2_participant",
        column1="calibration_id",
        column2="teacher_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help="The teachers who took part in this calibration session.",
    )
    anchor_ids = fields.Many2many(
        string="Anchors",
        comodel_name="school_character_anchor",
        relation="rel_character_calibration_2_anchor",
        column1="calibration_id",
        column2="anchor_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "The calibrated anchor examples that participants rated during "
            "this session."
        ),
    )
    agreement_result = fields.Char(
        string="Agreement Result",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "The overall agreement result of this session, e.g. the percentage "
            "of ratings within one level of each other (inter-rater "
            "reliability)."
        ),
    )
    notes = fields.Text(
        string="Notes",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help="Free-text notes and follow-up agreements from this session.",
    )
    rating_ids = fields.One2many(
        string="Ratings",
        comodel_name="school_character_calibration.rating",
        inverse_name="calibration_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "The rating lines of this session: the level each participant "
            "assigned to each anchor example."
        ),
    )
    rating_count = fields.Integer(
        string="Rating Count",
        compute="_compute_rating_count",
        store=True,
        help="Number of rating lines recorded in this session.",
    )

    @api.depends("rating_ids")
    def _compute_rating_count(self):
        """Count the rating lines recorded in this session.

        :return: nothing, writes ``rating_count`` on each record
        """
        for record in self:
            record.rating_count = len(record.rating_ids)

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

# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models

from odoo.addons.ssi_decorator import ssi_decorator


class SchoolCharacterObservation(models.Model):
    """
    Represents a Character Observation document: the header that gathers the
    structured, behaviour-based evidence recorded for one student against one
    character construct within an academic term (ICLAD v2.3 Evidence System,
    Bab 11 & Bab 12). Each observation carries a set of evidence entries, each
    of which is a single observed behaviour with its source type, evidence
    quality, and the scale level it is matched to.

    This is a transactional document with a full approval workflow:
    Draft -> Confirm -> Approve -> Open -> Done / Cancel. A provisional level
    can be assigned from the configured character scale; nothing is hardcoded.

    DATA GOVERNANCE BOUNDARY (ICLAD Bab 17): this document deliberately holds
    NO link to any discipline, counseling, or safeguarding record. Only
    legitimate character evidence (observation, reflection, artifact, peer,
    self, parent, community) is admissible; rumor, impression, counseling
    notes, psychological test results, and punishment data must NOT be
    recorded as character evidence.
    """

    _name = "school_character_observation"
    _inherit = [
        "mixin.transaction_cancel",
        "mixin.transaction_done",
        "mixin.transaction_open",
        "mixin.transaction_confirm",
    ]
    _description = "Character Observation"

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
        help="The date this Character Observation document was drawn up.",
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
        help="The student whose character this observation is about.",
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
        help="The character construct being observed and evidenced.",
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
            "The specific sub-construct being observed, when the observation "
            "targets a facet more granular than the construct itself."
        ),
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
        help="The academic year this observation belongs to.",
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
        help="The academic term this observation belongs to.",
    )
    provisional_level_id = fields.Many2one(
        string="Provisional Level",
        comodel_name="school_character_level",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "The provisional scale level assigned to the student for this "
            "construct on the basis of the evidence gathered. Taken from the "
            "configured character scale; never hardcoded."
        ),
    )
    summary = fields.Text(
        string="Summary",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "A narrative summary of the character evidence gathered for this "
            "student and construct across the term."
        ),
    )
    evidence_ids = fields.One2many(
        string="Evidence Entries",
        comodel_name="school_character_observation.evidence",
        inverse_name="observation_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        help=(
            "The individual evidence entries that make up this observation: "
            "each is a single observed behaviour with its source type, "
            "evidence quality, and matched scale level."
        ),
    )
    evidence_count = fields.Integer(
        string="Evidence Count",
        compute="_compute_evidence_count",
        store=True,
        help="Number of evidence entries recorded on this observation.",
    )

    @api.depends("evidence_ids")
    def _compute_evidence_count(self):
        for record in self:
            record.evidence_count = len(record.evidence_ids)

    @ssi_decorator.insert_on_form_view()
    def _insert_form_element(self, view_arch):
        if self._automatically_insert_view_element:
            view_arch = self._reconfigure_statusbar_visible(view_arch)
        return view_arch

# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SchoolCharacterObservationEvidence(models.Model):
    """
    Represents a single evidence entry of a Character Observation (ICLAD v2.3
    Evidence System, Bab 11 & Bab 12). Each entry records one concrete,
    observed behaviour, tied to the arena and (optionally) the activity in
    which it happened, the observer, the behavioural indicator it evidences,
    the kind of source it was drawn from, its evidence quality, and the scale
    level it is matched to.

    A student's own reflection is recorded here as an ordinary evidence entry
    with ``source_type = 'reflection'`` -- there is no separate sensitive
    store.

    DATA GOVERNANCE BOUNDARY (ICLAD Bab 17):

    * ``source_type`` is restricted to legitimate character-evidence sources
      (observation, reflection, artifact, peer, self, parent, community).
    * ``evidence_quality`` carries an ``invalid`` tier that documents,
      explicitly, that rumor, impression, counseling notes, psychological
      test results, and punishment data must NOT be used as character
      evidence. Such an entry may be saved to document the exclusion, but it
      never becomes valid evidence.
    * This model holds NO relation to any discipline, counseling, or
      safeguarding record.
    """

    _name = "school_character_observation.evidence"
    _description = "Character Observation Evidence Entry"
    _order = "observation_id, date, id"

    observation_id = fields.Many2one(
        string="# Observation",
        comodel_name="school_character_observation",
        required=True,
        ondelete="cascade",
        help="The character observation document this evidence entry belongs to.",
    )
    date = fields.Date(
        string="Date",
        required=True,
        help="The date on which the behaviour was observed.",
    )
    activity_id = fields.Many2one(
        string="Activity",
        comodel_name="school_character_activity",
        required=False,
        help=(
            "The character learning activity during which the behaviour was "
            "observed, when the evidence comes from a designed activity."
        ),
    )
    arena_id = fields.Many2one(
        string="Arena",
        comodel_name="school_character_arena",
        required=False,
        help=(
            "The arena/program (e.g. classroom, project, live-in) in which the "
            "behaviour was observed."
        ),
    )
    indicator_id = fields.Many2one(
        string="Indicator",
        comodel_name="school_character_indicator",
        required=False,
        help=(
            "The behavioural indicator that this evidence entry provides "
            "evidence for."
        ),
    )
    observer_id = fields.Many2one(
        string="Observer",
        comodel_name="school_teacher",
        required=False,
        help="The teacher who observed and recorded this behaviour.",
    )
    context = fields.Char(
        string="Context",
        required=False,
        help=(
            "Short note on the situation/context in which the behaviour " "occurred."
        ),
    )
    observed_behavior = fields.Text(
        string="Observed Behavior",
        required=False,
        help=(
            "Description of the concrete behaviour that was actually observed "
            "-- what the student did, phrased factually."
        ),
    )
    source_type = fields.Selection(
        string="Source Type",
        selection=[
            ("observation", "Observation"),
            ("reflection", "Reflection"),
            ("artifact", "Artifact/Work Product"),
            ("peer", "Peer Report"),
            ("self", "Self Report"),
            ("parent", "Parent Report"),
            ("community", "Community Report"),
        ],
        required=False,
        help=(
            "The kind of legitimate source this evidence was drawn from. A "
            "student's own reflection is recorded as 'Reflection'. Only these "
            "sources are admissible as character evidence (ICLAD Bab 17)."
        ),
    )
    evidence_quality = fields.Selection(
        string="Evidence Quality",
        selection=[
            ("invalid", "Invalid (Not Admissible)"),
            ("weak", "Weak"),
            ("sufficient", "Sufficient"),
            ("good", "Good"),
            ("strong", "Strong"),
        ],
        required=False,
        help=(
            "The quality tier of this evidence. The 'Invalid (Not Admissible)' "
            "tier documents that the material -- e.g. rumor, impression, "
            "counseling notes, psychological test results, or punishment data "
            "-- must NOT be used as character evidence (ICLAD Bab 17); it may "
            "be recorded only to make that exclusion explicit."
        ),
    )
    matched_level_id = fields.Many2one(
        string="Matched Level",
        comodel_name="school_character_level",
        required=False,
        help=(
            "The scale level this piece of evidence is matched to, from the "
            "configured character scale. Never hardcoded."
        ),
    )
    attachment_ids = fields.Many2many(
        string="Attachments",
        comodel_name="ir.attachment",
        relation="rel_character_observation_evidence_2_attachment",
        column1="evidence_id",
        column2="attachment_id",
        help=(
            "Supporting artifacts for this evidence entry (work products, "
            "photos of the behaviour's output, etc.)."
        ),
    )

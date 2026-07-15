# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SchoolCharacterProfile(models.Model):  # pylint: disable=too-few-public-methods
    """
    Represents a Character Profile, the top-level container of a school's
    set of core character values, per the ICLAD v2.3 construct architecture
    (Bab 6). A profile groups the constructs a school commits to forming.
    It is generic: the actual values are entered as data, never hard-coded,
    so the module stays universal in method while contextual in values.
    """

    _name = "school_character_profile"
    _inherit = ["mixin.master_data"]
    _description = "Character Profile"

    school_id = fields.Many2one(
        string="School",
        comodel_name="school",
        help="School this character profile belongs to. Optional: a profile "
        "may be defined at foundation level and shared across schools, or "
        "scoped to a single school.",
    )
    description = fields.Text(
        string="Description",
        help="Narrative description of this character profile and the intent "
        "behind the set of values it groups.",
    )
    construct_ids = fields.One2many(
        string="Constructs",
        comodel_name="school_character_construct",
        inverse_name="profile_id",
        help="Character constructs that make up this profile.",
    )

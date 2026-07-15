# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SchoolCharacterScale(models.Model):  # pylint: disable=too-few-public-methods
    """
    Represents a rating/level scale used to assess a character construct
    (the container of an ordered set of School Character Levels, per the
    ICLAD v2.3 construct architecture, Bab 6). A scale is deliberately kept
    generic: each school configures its own levels (for example a multi-level
    mastery scale, or a short status scale) instead of any scale being
    hard-coded, so the same module serves every school context.
    """

    _name = "school_character_scale"
    _inherit = ["mixin.master_data"]
    _description = "Character Scale"

    level_ids = fields.One2many(
        string="Levels",
        comodel_name="school_character_level",
        inverse_name="scale_id",
        help="Ordered set of levels that make up this scale. Each level is "
        "a School Character Level record ordered by its Sequence.",
    )

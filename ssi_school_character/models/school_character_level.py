# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SchoolCharacterLevel(models.Model):  # pylint: disable=too-few-public-methods
    """
    Represents a single level (a rung) within a School Character Scale, per
    the ICLAD v2.3 construct architecture (Bab 6). Levels are ordered by
    their Sequence in ascending order, from the least to the most advanced.
    The concrete labels of each level (for example a four-level mastery
    progression, or a status scale) are configured as data, never hard-coded
    in this module.
    """

    _name = "school_character_level"
    _inherit = ["mixin.master_data"]
    _description = "Character Level"
    _order = "scale_id, sequence, id"

    scale_id = fields.Many2one(
        string="Scale",
        comodel_name="school_character_scale",
        required=True,
        ondelete="cascade",
        help="Scale this level belongs to. A level cannot exist without a " "scale.",
    )
    sequence = fields.Integer(
        string="Sequence",
        default=10,
        required=True,
        help="Ascending order of this level within its scale: a lower value "
        "means a less advanced level and a higher value a more advanced one "
        "(levels are shown and evaluated from the lowest sequence up).",
    )
    description = fields.Text(
        string="Description",
        help="Narrative description of what this level represents within its "
        "scale, i.e. the qualities a learner shows to be placed at this "
        "level.",
    )

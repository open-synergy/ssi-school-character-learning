# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SchoolCharacterRubric(models.Model):  # pylint: disable=too-few-public-methods
    """
    Represents a Rubric for assessing a Character Construct against a scale,
    per the ICLAD v2.3 assessment section (Bab 8). A rubric ties a construct
    to a scale and holds one descriptor per level of that scale, describing
    what performance at each level looks like.
    """

    _name = "school_character_rubric"
    _inherit = ["mixin.master_data"]
    _description = "Character Rubric"

    construct_id = fields.Many2one(
        string="Construct",
        comodel_name="school_character_construct",
        required=True,
        ondelete="cascade",
        help="Construct this rubric assesses.",
    )
    scale_id = fields.Many2one(
        string="Scale",
        comodel_name="school_character_scale",
        required=True,
        help="Scale this rubric is built on; each descriptor line maps to a "
        "level of this scale.",
    )
    descriptor_ids = fields.One2many(
        string="Descriptors",
        comodel_name="school_character_rubric.descriptor",
        inverse_name="rubric_id",
        help="One descriptor per level of the scale, describing what "
        "performance at that level looks like.",
    )

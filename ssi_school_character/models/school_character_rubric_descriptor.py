# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SchoolCharacterRubricDescriptor(
    models.Model
):  # pylint: disable=too-few-public-methods
    """
    Represents one descriptor line of a Character Rubric: the criteria that
    describe performance at a single level of the rubric's scale, per the
    ICLAD v2.3 assessment section (Bab 8). A descriptor cannot exist without
    its parent rubric, so it is a child model, not master data.
    """

    _name = "school_character_rubric.descriptor"
    _description = "Character Rubric - Descriptor"
    _order = "rubric_id, level_id, id"

    rubric_id = fields.Many2one(
        string="# Rubric",
        comodel_name="school_character_rubric",
        required=True,
        ondelete="cascade",
        help="Rubric this descriptor belongs to.",
    )
    level_id = fields.Many2one(
        string="Level",
        comodel_name="school_character_level",
        required=True,
        help="Scale level this descriptor describes.",
    )
    descriptor = fields.Text(
        string="Descriptor",
        help="Description of what performance at this level looks like.",
    )
    criteria = fields.Text(
        string="Criteria",
        help="Concrete, observable criteria used to decide whether a learner "
        "is at this level.",
    )

# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SchoolCharacterSubconstruct(
    models.Model
):  # pylint: disable=too-few-public-methods
    """
    Represents a Sub-construct, a finer-grained facet of a Character
    Construct, per the ICLAD v2.3 construct architecture (Bab 6). A
    sub-construct decomposes a construct into narrower, still-observable
    parts so that indicators can be defined against each of them.
    """

    _name = "school_character_subconstruct"
    _inherit = [
        "mixin.master_data",
        "school_character_code_constraint_mixin",
    ]
    _description = "Character Sub-construct"

    construct_id = fields.Many2one(
        string="Construct",
        comodel_name="school_character_construct",
        required=True,
        ondelete="cascade",
        help="Construct this sub-construct decomposes.",
    )
    definition = fields.Text(
        string="Definition",
        help="Precise definition of this sub-construct as a narrower facet "
        "of its parent construct.",
    )

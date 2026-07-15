# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SchoolCharacterConstruct(models.Model):  # pylint: disable=too-few-public-methods
    """
    Represents a Character Construct, a single, clearly-defined character
    trait a school aims to form, per the ICLAD v2.3 construct architecture
    (Bab 6). A construct is defined precisely (its Definition) and bounded
    (its Boundary Statement, Bab 6.2, stating what the construct is NOT) so
    that assessment stays valid. Constructs belong to a profile, may be
    grouped in a family, are assessed against a scale, and are taught with
    one or more methods. Everything is configured as data to stay neutral.
    """

    _name = "school_character_construct"
    _inherit = ["mixin.master_data"]
    _description = "Character Construct"

    profile_id = fields.Many2one(
        string="Profile",
        comodel_name="school_character_profile",
        help="Character profile this construct belongs to.",
    )
    family_id = fields.Many2one(
        string="Family",
        comodel_name="school_character_family",
        help="Family this construct is grouped under, used to report and "
        "analyse related constructs together.",
    )
    scale_id = fields.Many2one(
        string="Scale",
        comodel_name="school_character_scale",
        help="Default scale used to assess this construct.",
    )
    definition = fields.Text(
        string="Definition",
        help="Precise definition of the construct: the observable trait or "
        "disposition the school intends to form and assess.",
    )
    boundary_statement = fields.Text(
        string="Boundary Statement",
        help="Statement of what this construct is NOT (ICLAD Bab 6.2), used "
        "to keep the construct distinct from neighbouring constructs and to "
        "protect the validity of its assessment.",
    )
    method_ids = fields.Many2many(
        string="Methods",
        comodel_name="school_character_method",
        relation="rel_character_construct_2_method",
        column1="construct_id",
        column2="method_id",
        help="Pedagogical methods used to teach, practise, and habituate "
        "this construct.",
    )
    subconstruct_ids = fields.One2many(
        string="Sub-constructs",
        comodel_name="school_character_subconstruct",
        inverse_name="construct_id",
        help="Sub-constructs that decompose this construct into finer parts.",
    )

# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SchoolCharacterFamily(models.Model):  # pylint: disable=too-few-public-methods
    """
    Represents a family/grouping of related character constructs, per the
    ICLAD v2.3 construct architecture (Bab 6). A family gathers constructs
    that share a common theme so they can be reported and analysed together.
    Families are modelled as master data (not a fixed Selection) so each
    school can define its own grouping without touching code.
    """

    _name = "school_character_family"
    _inherit = ["mixin.master_data"]
    _description = "Character Family"

    description = fields.Text(
        string="Description",
        help="Narrative description of the common theme shared by the "
        "constructs grouped in this family.",
    )

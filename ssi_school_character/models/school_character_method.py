# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SchoolCharacterMethod(models.Model):  # pylint: disable=too-few-public-methods
    """
    Represents a pedagogical method in the school's character-learning
    repertoire, per the ICLAD v2.3 pedagogy section (Bab 9): the concrete
    ways a character construct is taught, practised, and habituated (for
    example modelling, guided reflection, or service learning). Methods are
    master data so each school configures its own repertoire.
    """

    _name = "school_character_method"
    _inherit = ["mixin.master_data"]
    _description = "Character Method"

    description = fields.Text(
        string="Description",
        help="Narrative description of how this pedagogical method is " "carried out.",
    )
    suitable_for = fields.Text(
        string="Suitable For",
        help="Guidance on the situations, developmental stages, or construct "
        "types this method is most appropriate for.",
    )

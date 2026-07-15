# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SchoolCharacterArena(models.Model):  # pylint: disable=too-few-public-methods
    """
    Represents a learning arena/program in which character is formed and
    observed, per the ICLAD v2.3 construct architecture (Bab 6.2): the
    setting where a construct is lived out, such as intracurricular lessons,
    co-curricular or extracurricular activities, the school culture, or the
    homeroom. Arenas are master data so each school defines its own.
    """

    _name = "school_character_arena"
    _inherit = ["mixin.master_data"]
    _description = "Character Arena"

    arena_type = fields.Selection(
        string="Arena Type",
        selection=[
            ("intracurricular", "Intracurricular"),
            ("cocurricular", "Co-curricular"),
            ("extracurricular", "Extracurricular"),
            ("school_culture", "School Culture"),
            ("homeroom", "Homeroom"),
        ],
        help="Kind of learning setting this arena represents: "
        "Intracurricular = within subject lessons, "
        "Co-curricular = activities tied to the curriculum, "
        "Extracurricular = activities outside the curriculum, "
        "School Culture = the day-to-day habits and norms of the school, "
        "Homeroom = the homeroom/guidance setting.",
    )
    description = fields.Text(
        string="Description",
        help="Narrative description of this learning arena and how character "
        "is formed and observed within it.",
    )

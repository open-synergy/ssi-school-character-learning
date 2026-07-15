# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SchoolCharacterCurriculumLine(models.Model):
    """
    Represents a single mapping line of a Character Curriculum Map: one
    prioritized character construct paired with the arena/program where it
    will be developed, the method used, the target mastery level, the
    delivery track, the learning outcome (Capaian Pembelajaran), and the
    behavioral indicators used to observe it. All references point at the
    Character Framework master data, so the mapping stays fully
    configurable per school.
    """

    _name = "school_character_curriculum.line"
    _description = "Character Curriculum Map Line"

    curriculum_id = fields.Many2one(
        string="# Curriculum Map",
        comodel_name="school_character_curriculum",
        required=True,
        ondelete="cascade",
        help="The character curriculum map document this line belongs to.",
    )
    construct_id = fields.Many2one(
        string="Construct",
        comodel_name="school_character_construct",
        required=True,
        help="The character construct prioritized on this mapping line.",
    )
    construct_scale_id = fields.Many2one(
        string="Construct Scale",
        comodel_name="school_character_scale",
        related="construct_id.scale_id",
        store=False,
        help=(
            "The mastery scale of the selected construct, used to restrict "
            "the Target Level choices to levels of that scale."
        ),
    )
    subconstruct_id = fields.Many2one(
        string="Sub-construct",
        comodel_name="school_character_subconstruct",
        help=(
            "The specific sub-construct addressed on this line, when the "
            "mapping is more granular than the construct itself."
        ),
    )
    arena_id = fields.Many2one(
        string="Arena",
        comodel_name="school_character_arena",
        help=(
            "The arena/program (e.g. classroom, school culture, project) "
            "where this construct is developed."
        ),
    )
    method_id = fields.Many2one(
        string="Method",
        comodel_name="school_character_method",
        help="The character-development method applied on this line.",
    )
    target_level_id = fields.Many2one(
        string="Target Level",
        comodel_name="school_character_level",
        help=(
            "The target mastery level to be reached for this construct in "
            "the period, taken from the construct's own mastery scale."
        ),
    )
    track = fields.Selection(
        string="Track",
        selection=[
            ("intracurricular", "Intracurricular"),
            ("student_affairs", "Student Affairs"),
        ],
        help=(
            "The delivery track through which this construct is developed: "
            "intracurricular (in-class) or student affairs (co-curricular)."
        ),
    )
    capaian = fields.Text(
        string="Learning Outcome",
        help=(
            "The learning outcome / Capaian Pembelajaran (CP) statement "
            "for this construct in the period."
        ),
    )
    indicator_ids = fields.Many2many(
        string="Indicators",
        comodel_name="school_character_indicator",
        relation="rel_school_character_curriculum_line_2_indicator",
        column1="line_id",
        column2="indicator_id",
        help=(
            "The behavioral indicators used to observe progress on this "
            "construct for the period."
        ),
    )

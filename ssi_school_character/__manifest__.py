# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "School Character Learning",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    # pylint: disable=line-too-long
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia, Odoo Community Association (OCA)",  # noqa: B950
    # pylint: enable=line-too-long
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "ssi_school",
        "ssi_master_data_mixin",
        "ssi_m2o_configurator_mixin",
        "ssi_localdict_mixin",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir_model_access/school_character_scale.xml",
        "security/ir_model_access/school_character_level.xml",
        "security/ir_model_access/school_character_family.xml",
        "security/ir_model_access/school_character_method.xml",
        "security/ir_model_access/school_character_arena.xml",
        "security/ir_model_access/school_character_profile.xml",
        "security/ir_model_access/school_character_construct.xml",
        "security/ir_model_access/school_character_subconstruct.xml",
        "security/ir_model_access/school_character_indicator.xml",
        "security/ir_model_access/school_character_rubric.xml",
        "security/ir_model_access/school_character_anchor.xml",
        "menu.xml",
        "views/school_character_scale.xml",
        "views/school_character_level.xml",
        "views/school_character_family.xml",
        "views/school_character_method.xml",
        "views/school_character_arena.xml",
        "views/school_character_profile.xml",
        "views/school_character_construct.xml",
        "views/school_character_subconstruct.xml",
        "views/school_character_indicator.xml",
        "views/school_character_rubric.xml",
        "views/school_character_anchor.xml",
    ],
    "demo": [
        "demo/school_character_demo.xml",
    ],
}

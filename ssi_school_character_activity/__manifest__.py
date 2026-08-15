# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Character Learning Activity",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    # pylint: disable=line-too-long
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia, Odoo Community Association (OCA)",  # noqa: B950
    # pylint: enable=line-too-long
    "license": "AGPL-3",
    "installable": True,
    "application": False,
    "depends": [
        "ssi_school_character",
        "ssi_school_character_curriculum",
        "ssi_transaction_confirm_mixin",
        "ssi_transaction_open_mixin",
        "ssi_transaction_done_mixin",
        "ssi_transaction_cancel_mixin",
        "ssi_m2o_configurator_mixin",
        "ssi_localdict_mixin",
        "web_tour",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir_model_access/school_character_activity.xml",
        "security/ir_model_access/school_character_activity_alignment.xml",
        "security/ir_rule/school_character_activity.xml",
        "ir_sequence/school_character_activity.xml",
        "sequence_template/school_character_activity.xml",
        "approval_template/school_character_activity.xml",
        "policy_template/school_character_activity.xml",
        "menu.xml",
        "views/school_character_activity.xml",
        "views/assets.xml",
    ],
    "demo": [
        "demo/school_character_activity_demo.xml",
    ],
}

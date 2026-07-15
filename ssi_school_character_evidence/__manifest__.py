# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Character Observation & Teacher Calibration",
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
        "ssi_school_character_activity",
        "ssi_transaction_confirm_mixin",
        "ssi_transaction_open_mixin",
        "ssi_transaction_done_mixin",
        "ssi_transaction_cancel_mixin",
        "ssi_m2o_configurator_mixin",
        "ssi_localdict_mixin",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir_model_access/school_character_observation.xml",
        "security/ir_model_access/school_character_observation_evidence.xml",
        "security/ir_model_access/school_character_calibration.xml",
        "security/ir_model_access/school_character_calibration_rating.xml",
        "security/ir_rule/school_character_observation.xml",
        "security/ir_rule/school_character_calibration.xml",
        "ir_sequence/school_character_observation.xml",
        "ir_sequence/school_character_calibration.xml",
        "sequence_template/school_character_observation.xml",
        "sequence_template/school_character_calibration.xml",
        "policy_template/school_character_observation.xml",
        "policy_template/school_character_calibration.xml",
        "approval_template/school_character_observation.xml",
        "approval_template/school_character_calibration.xml",
        "menu.xml",
        "views/school_character_observation.xml",
        "views/school_character_calibration.xml",
    ],
    "demo": [
        "demo/school_character_evidence_demo.xml",
    ],
}

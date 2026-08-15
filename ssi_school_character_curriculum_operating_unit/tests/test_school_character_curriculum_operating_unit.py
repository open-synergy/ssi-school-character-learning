# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestSchoolCharacterCurriculumOperatingUnit(
    YamlTransactionCase
):  # pylint: disable=too-few-public-methods
    """Test the Operating Unit field on Character Curriculum Map."""

    def test_school_character_curriculum_operating_unit(self):
        """Run the operating unit scenario YAML for the curriculum."""
        self.run_yaml_scenario(
            "test_data_school_character_curriculum_operating_unit.yaml"
        )

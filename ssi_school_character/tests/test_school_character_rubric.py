# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestSchoolCharacterRubric(YamlTransactionCase):
    """YAML scenario runner for ``school_character_rubric``."""

    def test_school_character_rubric(self):
        """Run the ``school_character_rubric`` YAML scenario."""
        self.run_yaml_scenario("test_data_school_character_rubric.yaml")

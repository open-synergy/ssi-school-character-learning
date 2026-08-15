# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestSchoolCharacterActivity(YamlTransactionCase):
    """Run the YAML scenarios for ``school_character_activity``."""

    def test_school_character_activity(self):
        """Run the full create/confirm/approve/done/cancel scenarios."""
        self.run_yaml_scenario("test_data_school_character_activity.yaml")

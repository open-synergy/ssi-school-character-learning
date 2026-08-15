# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestSchoolCharacterGrowthReportOperatingUnit(
    YamlTransactionCase
):  # pylint: disable=too-few-public-methods
    """Run the YAML scenarios for the growth report OU glue."""

    def test_school_character_growth_report_operating_unit(self):
        """Run the single Operating Unit scenario for the model."""
        self.run_yaml_scenario(
            "test_data_school_character_growth_report_operating_unit.yaml"
        )

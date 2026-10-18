# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestSchoolCharacterFamilyAccess(YamlTransactionCase):
    """Scenario tests for the ``school_character_family`` group."""

    def test_school_character_family_access(self):
        """Run the configurator-group access scenarios.

        Covers the positive path (a member of
        ``school_character_family_group`` can create, write and unlink) and
        the negative path (an internal user holding only the workflow
        ``school_character_user_group`` is rejected on create, write and
        unlink, while read still works).
        """
        self.run_yaml_scenario("test_data_school_character_family_access.yaml")

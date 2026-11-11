# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestSchoolCharacterDisplayName(YamlTransactionCase):
    """Display name and code search of sub-construct and indicator."""

    def setUp(self):
        """Create a construct, a sub-construct and an indicator.

        :return: nothing
        """
        super().setUp()
        env = self.env
        self.construct = env["school_character_construct"].create(
            {"name": "Construct DN", "code": "CON-DN1"}
        )
        self.subconstruct = env["school_character_subconstruct"].create(
            {
                "name": "Sub A",
                "code": "SC-T1",
                "construct_id": self.construct.id,
            }
        )
        self.indicator = env["school_character_indicator"].create(
            {
                "name": "Indicator A",
                "code": "IND-T1",
                "construct_id": self.construct.id,
                "subconstruct_id": self.subconstruct.id,
            }
        )

    def _found_ids(self, record, term):
        """Return the ids found by ``name_search`` on the record's model.

        :param record: Record whose model is searched.
        :param term: Text passed to ``name_search``.
        :return: List of matching record ids.
        :rtype: list[int]
        """
        return [rid for rid, _name in record.name_search(term)]

    def test_subconstruct_display_name(self):
        """Check ``name_get`` of a sub-construct shows its code.

        Pure Python because of trigger ``P1`` (return value of
        ``name_get``) and limitations ``L-01`` and ``L-02``.

        :return: nothing
        """
        self.assertEqual(self.subconstruct.name_get()[0][1], "[SC-T1] Sub A")

    def test_indicator_display_name(self):
        """Check ``name_get`` of an indicator shows its code.

        Pure Python because of trigger ``P1`` (return value of
        ``name_get``) and limitations ``L-01`` and ``L-02``.

        :return: nothing
        """
        self.assertEqual(self.indicator.name_get()[0][1], "[IND-T1] Indicator A")

    def test_subconstruct_name_search(self):
        """Check a sub-construct is found by code and by name part.

        Pure Python because of trigger ``P1`` (return value of
        ``name_search``) and limitations ``L-01`` and ``L-02``.

        :return: nothing
        """
        self.assertIn(self.subconstruct.id, self._found_ids(self.subconstruct, "SC-T1"))
        self.assertIn(self.subconstruct.id, self._found_ids(self.subconstruct, "Sub"))

    def test_indicator_name_search(self):
        """Check an indicator is found by code and by name part.

        Pure Python because of trigger ``P1`` (return value of
        ``name_search``) and limitations ``L-01`` and ``L-02``.

        :return: nothing
        """
        self.assertIn(self.indicator.id, self._found_ids(self.indicator, "IND-T1"))
        self.assertIn(self.indicator.id, self._found_ids(self.indicator, "Indicator"))

    def test_name_search_no_match(self):
        """Check a text matching neither code nor name finds nothing.

        Pure Python because of trigger ``P1`` (return value of
        ``name_search``) and limitations ``L-01`` and ``L-02``.

        :return: nothing
        """
        self.assertNotIn(
            self.subconstruct.id, self._found_ids(self.subconstruct, "ZZZ-NOPE")
        )
        self.assertNotIn(self.indicator.id, self._found_ids(self.indicator, "ZZZ-NOPE"))

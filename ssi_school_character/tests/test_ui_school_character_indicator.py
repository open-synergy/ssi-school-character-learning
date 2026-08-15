# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiSchoolCharacterIndicator(HttpSavepointCase):
    """Tour tests for the ``school_character_indicator`` work
    instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the fixtures required by the indicator tours."""
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        cls.construct = cls.env["school_character_construct"].create(
            {"name": "Tour Indicator Construct", "code": "TOUR-IND-CON"}
        )
        cls.indicator_edit = cls.env["school_character_indicator"].create(
            {
                "name": "Tour Indicator Edit",
                "code": "TOUR-IND-EDIT",
                "construct_id": cls.construct.id,
            }
        )
        cls.indicator_delete = cls.env["school_character_indicator"].create(
            {
                "name": "Tour Indicator Delete",
                "code": "TOUR-IND-DEL",
                "construct_id": cls.construct.id,
            }
        )
        cls.indicator_deactivate = cls.env["school_character_indicator"].create(
            {
                "name": "Tour Indicator Deactivate",
                "code": "TOUR-IND-DEACT",
                "construct_id": cls.construct.id,
            }
        )
        cls.indicator_activate = cls.env["school_character_indicator"].create(
            {
                "name": "Tour Indicator Activate",
                "code": "TOUR-IND-ACT",
                "construct_id": cls.construct.id,
                "active": False,
            }
        )

    def test_create(self):
        """Run the create tour for ``school_character_indicator``.

        IK: docs/school_character_indicator/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_school_character_indicator_create",
            login="admin",
        )

    def test_edit(self):
        """Run the edit tour for ``school_character_indicator``.

        IK: docs/school_character_indicator/02-edit.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_school_character_indicator_edit",
            login="admin",
        )

    def test_delete(self):
        """Run the delete tour for ``school_character_indicator``.

        IK: docs/school_character_indicator/03-delete.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_school_character_indicator_delete",
            login="admin",
        )

    def test_deactivate(self):
        """Run the deactivate tour for ``school_character_indicator``.

        IK: docs/school_character_indicator/04-deactivate.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_school_character_indicator_deactivate",
            login="admin",
        )

    def test_activate(self):
        """Run the activate tour for ``school_character_indicator``.

        IK: docs/school_character_indicator/05-activate.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_school_character_indicator_activate",
            login="admin",
        )

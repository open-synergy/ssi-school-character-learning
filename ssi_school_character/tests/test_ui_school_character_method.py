# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiSchoolCharacterMethod(HttpSavepointCase):
    """Tour tests for the ``school_character_method`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the fixtures required by the method tours."""
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        cls.rec_edit = cls.env["school_character_method"].create(
            {
                "name": "Tour Method Edit",
                "code": "TOUR-MTH-EDIT",
            }
        )
        cls.rec_delete = cls.env["school_character_method"].create(
            {
                "name": "Tour Method Delete",
                "code": "TOUR-MTH-DEL",
            }
        )
        cls.rec_deactivate = cls.env["school_character_method"].create(
            {
                "name": "Tour Method Deactivate",
                "code": "TOUR-MTH-DEACT",
            }
        )
        cls.rec_activate = cls.env["school_character_method"].create(
            {
                "name": "Tour Method Activate",
                "code": "TOUR-MTH-ACT",
                "active": False,
            }
        )

    def test_create(self):
        """Run the create tour for ``school_character_method``.

        IK: docs/school_character_method/01-create.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_method_create", login="admin"
        )

    def test_edit(self):
        """Run the edit tour for ``school_character_method``.

        IK: docs/school_character_method/02-edit.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_method_edit", login="admin"
        )

    def test_delete(self):
        """Run the delete tour for ``school_character_method``.

        IK: docs/school_character_method/03-delete.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_method_delete", login="admin"
        )

    def test_deactivate(self):
        """Run the deactivate tour for ``school_character_method``.

        IK: docs/school_character_method/04-deactivate.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_school_character_method_deactivate",
            login="admin",
        )

    def test_activate(self):
        """Run the activate tour for ``school_character_method``.

        IK: docs/school_character_method/05-activate.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_school_character_method_activate",
            login="admin",
        )

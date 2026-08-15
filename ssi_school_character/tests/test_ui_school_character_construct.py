# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiSchoolCharacterConstruct(HttpSavepointCase):
    """Tour tests for the ``school_character_construct`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the fixtures required by the construct tours."""
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        cls.rec_edit = cls.env["school_character_construct"].create(
            {
                "name": "Tour Construct Edit",
                "code": "TOUR-CON-EDIT",
            }
        )
        cls.rec_delete = cls.env["school_character_construct"].create(
            {
                "name": "Tour Construct Delete",
                "code": "TOUR-CON-DEL",
            }
        )
        cls.rec_deactivate = cls.env["school_character_construct"].create(
            {
                "name": "Tour Construct Deactivate",
                "code": "TOUR-CON-DEACT",
            }
        )
        cls.rec_activate = cls.env["school_character_construct"].create(
            {
                "name": "Tour Construct Activate",
                "code": "TOUR-CON-ACT",
                "active": False,
            }
        )

    def test_create(self):
        """Run the create tour for ``school_character_construct``.

        IK: docs/school_character_construct/01-create.md
        """
        self.start_tour("/web", "ssi_school_character_school_character_construct_create", login="admin")

    def test_edit(self):
        """Run the edit tour for ``school_character_construct``.

        IK: docs/school_character_construct/02-edit.md
        """
        self.start_tour("/web", "ssi_school_character_school_character_construct_edit", login="admin")

    def test_delete(self):
        """Run the delete tour for ``school_character_construct``.

        IK: docs/school_character_construct/03-delete.md
        """
        self.start_tour("/web", "ssi_school_character_school_character_construct_delete", login="admin")

    def test_deactivate(self):
        """Run the deactivate tour for ``school_character_construct``.

        IK: docs/school_character_construct/04-deactivate.md
        """
        self.start_tour("/web", "ssi_school_character_school_character_construct_deactivate", login="admin")

    def test_activate(self):
        """Run the activate tour for ``school_character_construct``.

        IK: docs/school_character_construct/05-activate.md
        """
        self.start_tour("/web", "ssi_school_character_school_character_construct_activate", login="admin")

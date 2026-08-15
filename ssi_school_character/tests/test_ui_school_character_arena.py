# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiSchoolCharacterArena(HttpSavepointCase):
    """Tour tests for the ``school_character_arena`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the fixtures required by the arena tours."""
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        cls.rec_edit = cls.env["school_character_arena"].create(
            {
                "name": "Tour Arena Edit",
                "code": "TOUR-ARN-EDIT",
            }
        )
        cls.rec_delete = cls.env["school_character_arena"].create(
            {
                "name": "Tour Arena Delete",
                "code": "TOUR-ARN-DEL",
            }
        )
        cls.rec_deactivate = cls.env["school_character_arena"].create(
            {
                "name": "Tour Arena Deactivate",
                "code": "TOUR-ARN-DEACT",
            }
        )
        cls.rec_activate = cls.env["school_character_arena"].create(
            {
                "name": "Tour Arena Activate",
                "code": "TOUR-ARN-ACT",
                "active": False,
            }
        )

    def test_create(self):
        """Run the create tour for ``school_character_arena``.

        IK: docs/school_character_arena/01-create.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_arena_create", login="admin"
        )

    def test_edit(self):
        """Run the edit tour for ``school_character_arena``.

        IK: docs/school_character_arena/02-edit.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_arena_edit", login="admin"
        )

    def test_delete(self):
        """Run the delete tour for ``school_character_arena``.

        IK: docs/school_character_arena/03-delete.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_arena_delete", login="admin"
        )

    def test_deactivate(self):
        """Run the deactivate tour for ``school_character_arena``.

        IK: docs/school_character_arena/04-deactivate.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_arena_deactivate", login="admin"
        )

    def test_activate(self):
        """Run the activate tour for ``school_character_arena``.

        IK: docs/school_character_arena/05-activate.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_arena_activate", login="admin"
        )

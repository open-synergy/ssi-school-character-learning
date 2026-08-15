# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiSchoolCharacterLevel(HttpSavepointCase):
    """Tour tests for the ``school_character_level`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the fixtures required by the level tours."""
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        cls.scale = cls.env["school_character_scale"].create(
            {"name": "Tour Level Scale", "code": "TOUR-LVL-SCL"}
        )
        cls.level_edit = cls.env["school_character_level"].create(
            {
                "name": "Tour Level Edit",
                "code": "TOUR-LVL-EDIT",
                "scale_id": cls.scale.id,
            }
        )
        cls.level_delete = cls.env["school_character_level"].create(
            {
                "name": "Tour Level Delete",
                "code": "TOUR-LVL-DEL",
                "scale_id": cls.scale.id,
            }
        )
        cls.level_deactivate = cls.env["school_character_level"].create(
            {
                "name": "Tour Level Deactivate",
                "code": "TOUR-LVL-DEACT",
                "scale_id": cls.scale.id,
            }
        )
        cls.level_activate = cls.env["school_character_level"].create(
            {
                "name": "Tour Level Activate",
                "code": "TOUR-LVL-ACT",
                "scale_id": cls.scale.id,
                "active": False,
            }
        )

    def test_create(self):
        """Run the create tour for ``school_character_level``.

        IK: docs/school_character_level/01-create.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_level_create", login="admin"
        )

    def test_edit(self):
        """Run the edit tour for ``school_character_level``.

        IK: docs/school_character_level/02-edit.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_level_edit", login="admin"
        )

    def test_delete(self):
        """Run the delete tour for ``school_character_level``.

        IK: docs/school_character_level/03-delete.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_level_delete", login="admin"
        )

    def test_deactivate(self):
        """Run the deactivate tour for ``school_character_level``.

        IK: docs/school_character_level/04-deactivate.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_school_character_level_deactivate",
            login="admin",
        )

    def test_activate(self):
        """Run the activate tour for ``school_character_level``.

        IK: docs/school_character_level/05-activate.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_school_character_level_activate",
            login="admin",
        )

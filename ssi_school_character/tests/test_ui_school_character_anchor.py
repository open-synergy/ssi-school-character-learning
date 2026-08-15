# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiSchoolCharacterAnchor(HttpSavepointCase):
    """Tour tests for the ``school_character_anchor`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the fixtures required by the anchor tours."""
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        cls.construct = cls.env["school_character_construct"].create(
            {
                "name": "Tour Anchor Construct",
                "code": "TOUR-ANC-CON",
            }
        )
        cls.level = cls.env["school_character_level"].create(
            {
                "name": "Tour Anchor Level",
                "code": "TOUR-ANC-LVL",
            }
        )
        cls.anchor_edit = cls.env["school_character_anchor"].create(
            {
                "name": "Tour Anchor Edit",
                "code": "TOUR-ANC-EDIT",
                "construct_id": cls.construct.id,
                "level_id": cls.level.id,
            }
        )
        cls.anchor_delete = cls.env["school_character_anchor"].create(
            {
                "name": "Tour Anchor Delete",
                "code": "TOUR-ANC-DEL",
                "construct_id": cls.construct.id,
                "level_id": cls.level.id,
            }
        )
        cls.anchor_deactivate = cls.env["school_character_anchor"].create(
            {
                "name": "Tour Anchor Deactivate",
                "code": "TOUR-ANC-DEACT",
                "construct_id": cls.construct.id,
                "level_id": cls.level.id,
            }
        )
        cls.anchor_activate = cls.env["school_character_anchor"].create(
            {
                "name": "Tour Anchor Activate",
                "code": "TOUR-ANC-ACT",
                "construct_id": cls.construct.id,
                "level_id": cls.level.id,
                "active": False,
            }
        )

    def test_create(self):
        """Run the create tour for ``school_character_anchor``.

        IK: docs/school_character_anchor/01-create.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_anchor_create", login="admin"
        )

    def test_edit(self):
        """Run the edit tour for ``school_character_anchor``.

        IK: docs/school_character_anchor/02-edit.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_anchor_edit", login="admin"
        )

    def test_delete(self):
        """Run the delete tour for ``school_character_anchor``.

        IK: docs/school_character_anchor/03-delete.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_anchor_delete", login="admin"
        )

    def test_deactivate(self):
        """Run the deactivate tour for ``school_character_anchor``.

        IK: docs/school_character_anchor/04-deactivate.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_anchor_deactivate", login="admin"
        )

    def test_activate(self):
        """Run the activate tour for ``school_character_anchor``.

        IK: docs/school_character_anchor/05-activate.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_anchor_activate", login="admin"
        )

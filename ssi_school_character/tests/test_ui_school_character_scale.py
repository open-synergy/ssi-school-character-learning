# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiSchoolCharacterScale(HttpSavepointCase):
    """Tour tests for the ``school_character_scale`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the fixtures required by the scale tours."""
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        cls.scale_edit = cls.env["school_character_scale"].create(
            {"name": "Tour Scale Edit", "code": "TOUR-SCL-EDIT"}
        )
        cls.scale_delete = cls.env["school_character_scale"].create(
            {"name": "Tour Scale Delete", "code": "TOUR-SCL-DEL"}
        )
        cls.scale_deactivate = cls.env["school_character_scale"].create(
            {"name": "Tour Scale Deactivate", "code": "TOUR-SCL-DEACT"}
        )
        cls.scale_activate = cls.env["school_character_scale"].create(
            {
                "name": "Tour Scale Activate",
                "code": "TOUR-SCL-ACT",
                "active": False,
            }
        )

    def test_create(self):
        """Run the create tour for ``school_character_scale``.

        IK: docs/school_character_scale/01-create.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_scale_create", login="admin"
        )

    def test_edit(self):
        """Run the edit tour for ``school_character_scale``.

        IK: docs/school_character_scale/02-edit.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_scale_edit", login="admin"
        )

    def test_delete(self):
        """Run the delete tour for ``school_character_scale``.

        IK: docs/school_character_scale/03-delete.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_scale_delete", login="admin"
        )

    def test_deactivate(self):
        """Run the deactivate tour for ``school_character_scale``.

        IK: docs/school_character_scale/04-deactivate.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_scale_deactivate", login="admin"
        )

    def test_activate(self):
        """Run the activate tour for ``school_character_scale``.

        IK: docs/school_character_scale/05-activate.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_scale_activate", login="admin"
        )

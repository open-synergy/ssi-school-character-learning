# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiSchoolCharacterProfile(HttpSavepointCase):
    """Tour tests for the ``school_character_profile`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the fixtures required by the profile tours."""
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        cls.rec_edit = cls.env["school_character_profile"].create(
            {
                "name": "Tour Profile Edit",
                "code": "TOUR-PRO-EDIT",
            }
        )
        cls.rec_delete = cls.env["school_character_profile"].create(
            {
                "name": "Tour Profile Delete",
                "code": "TOUR-PRO-DEL",
            }
        )
        cls.rec_deactivate = cls.env["school_character_profile"].create(
            {
                "name": "Tour Profile Deactivate",
                "code": "TOUR-PRO-DEACT",
            }
        )
        cls.rec_activate = cls.env["school_character_profile"].create(
            {
                "name": "Tour Profile Activate",
                "code": "TOUR-PRO-ACT",
                "active": False,
            }
        )

    def test_create(self):
        """Run the create tour for ``school_character_profile``.

        IK: docs/school_character_profile/01-create.md
        """
        self.start_tour("/web", "ssi_school_character_school_character_profile_create", login="admin")

    def test_edit(self):
        """Run the edit tour for ``school_character_profile``.

        IK: docs/school_character_profile/02-edit.md
        """
        self.start_tour("/web", "ssi_school_character_school_character_profile_edit", login="admin")

    def test_delete(self):
        """Run the delete tour for ``school_character_profile``.

        IK: docs/school_character_profile/03-delete.md
        """
        self.start_tour("/web", "ssi_school_character_school_character_profile_delete", login="admin")

    def test_deactivate(self):
        """Run the deactivate tour for ``school_character_profile``.

        IK: docs/school_character_profile/04-deactivate.md
        """
        self.start_tour("/web", "ssi_school_character_school_character_profile_deactivate", login="admin")

    def test_activate(self):
        """Run the activate tour for ``school_character_profile``.

        IK: docs/school_character_profile/05-activate.md
        """
        self.start_tour("/web", "ssi_school_character_school_character_profile_activate", login="admin")

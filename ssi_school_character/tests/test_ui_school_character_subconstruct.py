# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiSchoolCharacterSubconstruct(HttpSavepointCase):
    """Tour tests for the ``school_character_subconstruct`` work
    instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the fixtures required by the sub-construct tours."""
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        cls.construct = cls.env["school_character_construct"].create(
            {"name": "Tour Subconstruct Construct", "code": "TOUR-SUB-CON"}
        )
        cls.subconstruct_edit = cls.env["school_character_subconstruct"].create(
            {
                "name": "Tour Subconstruct Edit",
                "code": "TOUR-SUB-EDIT",
                "construct_id": cls.construct.id,
            }
        )
        cls.subconstruct_delete = cls.env["school_character_subconstruct"].create(
            {
                "name": "Tour Subconstruct Delete",
                "code": "TOUR-SUB-DEL",
                "construct_id": cls.construct.id,
            }
        )
        cls.subconstruct_deactivate = cls.env["school_character_subconstruct"].create(
            {
                "name": "Tour Subconstruct Deactivate",
                "code": "TOUR-SUB-DEACT",
                "construct_id": cls.construct.id,
            }
        )
        cls.subconstruct_activate = cls.env["school_character_subconstruct"].create(
            {
                "name": "Tour Subconstruct Activate",
                "code": "TOUR-SUB-ACT",
                "construct_id": cls.construct.id,
                "active": False,
            }
        )

    def test_create(self):
        """Run the create tour for ``school_character_subconstruct``.

        IK: docs/school_character_subconstruct/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_school_character_subconstruct_create",
            login="admin",
        )

    def test_edit(self):
        """Run the edit tour for ``school_character_subconstruct``.

        IK: docs/school_character_subconstruct/02-edit.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_school_character_subconstruct_edit",
            login="admin",
        )

    def test_delete(self):
        """Run the delete tour for ``school_character_subconstruct``.

        IK: docs/school_character_subconstruct/03-delete.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_school_character_subconstruct_delete",
            login="admin",
        )

    def test_deactivate(self):
        """Run the deactivate tour for ``school_character_subconstruct``.

        IK: docs/school_character_subconstruct/04-deactivate.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_school_character_subconstruct_deactivate",
            login="admin",
        )

    def test_activate(self):
        """Run the activate tour for ``school_character_subconstruct``.

        IK: docs/school_character_subconstruct/05-activate.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_school_character_subconstruct_activate",
            login="admin",
        )

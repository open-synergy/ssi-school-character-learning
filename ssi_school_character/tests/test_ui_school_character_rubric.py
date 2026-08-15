# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiSchoolCharacterRubric(HttpSavepointCase):
    """Tour tests for the ``school_character_rubric`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the fixtures required by the rubric tours."""
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        cls.construct = cls.env["school_character_construct"].create(
            {"name": "Tour Rubric Construct", "code": "TOUR-RUB-CON"}
        )
        cls.scale = cls.env["school_character_scale"].create(
            {"name": "Tour Rubric Scale", "code": "TOUR-RUB-SCALE"}
        )
        cls.rec_edit = cls.env["school_character_rubric"].create(
            {
                "name": "Tour Rubric Edit",
                "code": "TOUR-RUB-EDIT",
                "construct_id": cls.construct.id,
                "scale_id": cls.scale.id,
            }
        )
        cls.rec_delete = cls.env["school_character_rubric"].create(
            {
                "name": "Tour Rubric Delete",
                "code": "TOUR-RUB-DEL",
                "construct_id": cls.construct.id,
                "scale_id": cls.scale.id,
            }
        )
        cls.rec_deactivate = cls.env["school_character_rubric"].create(
            {
                "name": "Tour Rubric Deactivate",
                "code": "TOUR-RUB-DEACT",
                "construct_id": cls.construct.id,
                "scale_id": cls.scale.id,
            }
        )
        cls.rec_activate = cls.env["school_character_rubric"].create(
            {
                "name": "Tour Rubric Activate",
                "code": "TOUR-RUB-ACT",
                "construct_id": cls.construct.id,
                "scale_id": cls.scale.id,
                "active": False,
            }
        )

    def test_create(self):
        """Run the create tour for ``school_character_rubric``.

        IK: docs/school_character_rubric/01-create.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_rubric_create",
            login="admin",
        )

    def test_edit(self):
        """Run the edit tour for ``school_character_rubric``.

        IK: docs/school_character_rubric/02-edit.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_rubric_edit",
            login="admin",
        )

    def test_delete(self):
        """Run the delete tour for ``school_character_rubric``.

        IK: docs/school_character_rubric/03-delete.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_rubric_delete",
            login="admin",
        )

    def test_deactivate(self):
        """Run the deactivate tour for ``school_character_rubric``.

        IK: docs/school_character_rubric/04-deactivate.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_rubric_deactivate",
            login="admin",
        )

    def test_activate(self):
        """Run the activate tour for ``school_character_rubric``.

        IK: docs/school_character_rubric/05-activate.md
        """
        self.start_tour(
            "/web", "ssi_school_character_school_character_rubric_activate",
            login="admin",
        )

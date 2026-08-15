# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase -- NOT HttpCase. See structure-and-runner.md "Base class".
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiSchoolCharacterCurriculum(HttpSavepointCase):
    """Tour tests for the ``school_character_curriculum`` work

    instructions.
    """

    @classmethod
    def _create_curriculum(cls, suffix, year_name):
        """Create one draft curriculum map owned by the tour's admin.

        :param suffix: unique suffix used for the backing academic year
            code.
        :param year_name: unique academic year name, used by tours to
            find this record's row in the list view.
        :return: the created ``school_character_curriculum`` record.
        """
        year = cls.env["school_academic_year"].create(
            {
                "name": year_name,
                "code": "TOUR-CUR-%s" % suffix,
                "date_start": "2026-01-01",
                "date_end": "2026-12-31",
            }
        )
        return cls.env["school_character_curriculum"].create(
            {
                "academic_year_id": year.id,
                "profile_id": cls.profile.id,
                "user_id": cls.admin.id,
            }
        )

    @classmethod
    def setUpClass(cls):
        """Create the master data and per-tour fixture curriculum maps.

        ``user_id`` is explicit on every record: ``cls.env`` runs as
        SUPERUSER, and the internal-user record rule would otherwise
        hide these fixtures from the tour's admin session.
        """
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        cls.profile = cls.env["school_character_profile"].create(
            {"name": "TOUR Curriculum Profile", "code": "TOUR-CUR-PROFILE"}
        )
        cls.cancel_reason = cls.env["base.cancel_reason"].create(
            {
                "name": "TOUR Curriculum Cancel Reason",
                "code": "TOUR-CUR-CANCEL",
                "global_use": True,
            }
        )

        # 01-create / 02-edit / 03-delete / 10-cancel: draft is enough.
        cls.cur_create = cls._create_curriculum("01", "TOUR Curriculum Year 01")
        cls.cur_edit = cls._create_curriculum("02", "TOUR Curriculum Year 02")
        cls.cur_delete = cls._create_curriculum("03", "TOUR Curriculum Year 03")
        cls.cur_cancel = cls._create_curriculum("10", "TOUR Curriculum Year 10")

        # 04-confirm: draft is enough, tour itself performs the confirm.
        cls.cur_confirm = cls._create_curriculum("04", "TOUR Curriculum Year 04")

        # 05-approve / 06-reject: pre-drive to "confirm" as admin.
        cls.cur_approve = cls._create_curriculum("05", "TOUR Curriculum Year 05")
        cls.cur_approve.with_user(cls.admin).action_confirm()
        cls.cur_reject = cls._create_curriculum("06", "TOUR Curriculum Year 06")
        cls.cur_reject.with_user(cls.admin).action_confirm()

        # 09-finish: pre-drive all the way to "open".
        cls.cur_finish = cls._create_curriculum("09", "TOUR Curriculum Year 09")
        cls.cur_finish.with_user(cls.admin).action_confirm()
        cls.cur_finish.with_user(cls.admin).action_approve_approval()

        # 12-restart: pre-drive to "cancel".
        cls.cur_restart = cls._create_curriculum("12", "TOUR Curriculum Year 12")
        cls.cur_restart.with_user(cls.admin).action_cancel()

    def test_create(self):
        """Run the create tour for ``school_character_curriculum``.

        IK: docs/school_character_curriculum/01-create.md
        """
        self.start_tour("/web", "ssi_school_character_curriculum_create", login="admin")

    def test_edit(self):
        """Run the edit tour for ``school_character_curriculum``.

        IK: docs/school_character_curriculum/02-edit.md
        """
        self.start_tour("/web", "ssi_school_character_curriculum_edit", login="admin")

    def test_delete(self):
        """Run the delete tour for ``school_character_curriculum``.

        IK: docs/school_character_curriculum/03-delete.md
        """
        self.start_tour("/web", "ssi_school_character_curriculum_delete", login="admin")

    def test_confirm(self):
        """Run the confirm tour for ``school_character_curriculum``.

        IK: docs/school_character_curriculum/04-confirm.md
        """
        self.start_tour(
            "/web", "ssi_school_character_curriculum_confirm", login="admin"
        )

    def test_approve(self):
        """Run the approve tour for ``school_character_curriculum``.

        IK: docs/school_character_curriculum/05-approve.md
        """
        self.start_tour(
            "/web", "ssi_school_character_curriculum_approve", login="admin"
        )

    def test_reject(self):
        """Run the reject tour for ``school_character_curriculum``.

        IK: docs/school_character_curriculum/06-reject.md
        """
        self.start_tour("/web", "ssi_school_character_curriculum_reject", login="admin")

    def test_finish(self):
        """Run the finish (Done) tour for ``school_character_curriculum``.

        IK: docs/school_character_curriculum/09-finish.md
        """
        self.start_tour("/web", "ssi_school_character_curriculum_finish", login="admin")

    def test_cancel(self):
        """Run the cancel tour for ``school_character_curriculum``.

        IK: docs/school_character_curriculum/10-cancel.md
        """
        self.start_tour("/web", "ssi_school_character_curriculum_cancel", login="admin")

    def test_restart(self):
        """Run the restart tour for ``school_character_curriculum``.

        IK: docs/school_character_curriculum/12-restart.md
        """
        self.start_tour(
            "/web", "ssi_school_character_curriculum_restart", login="admin"
        )

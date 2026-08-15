# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase -- NOT HttpCase. See structure-and-runner.md "Base class".
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiSchoolCharacterGrowthReport(HttpSavepointCase):
    """Tour tests for the ``school_character_growth_report`` work

    instructions.
    """

    @classmethod
    def _create_report(cls, suffix, student_name):
        """Create one draft growth report owned by the tour's admin.

        :param suffix: unique suffix used for the backing student code.
        :param student_name: unique student name, used by tours to find
            this record's row in the list view.
        :return: the created ``school_character_growth_report`` record.
        """
        contact = cls.env["res.partner"].create({"name": student_name})
        student = cls.env["school_student"].create(
            {
                "name": student_name,
                "code": "TOUR-GRP-%s" % suffix,
                "contact_id": contact.id,
                "school_id": cls.school.id,
            }
        )
        return cls.env["school_character_growth_report"].create(
            {
                "student_id": student.id,
                "user_id": cls.admin.id,
            }
        )

    @classmethod
    def setUpClass(cls):
        """Create the master data and per-tour fixture reports.

        ``user_id`` is explicit on every record: ``cls.env`` runs as
        SUPERUSER, and the internal-user record rule would otherwise
        hide these fixtures from the tour's admin session.
        """
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        grade_type = cls.env["school_grade_type"].create(
            {"name": "TOUR Growth Grade Type", "code": "TOUR-GRP-GT"}
        )
        cls.school = cls.env["school"].create(
            {
                "name": "TOUR Growth School",
                "code": "TOUR-GRP-SCH",
                "grade_type_id": grade_type.id,
            }
        )
        cls.cancel_reason = cls.env["base.cancel_reason"].create(
            {
                "name": "TOUR Growth Cancel Reason",
                "code": "TOUR-GRP-CANCEL",
                "global_use": True,
            }
        )

        # 01-create / 02-edit / 03-delete / 10-cancel: draft is enough.
        cls.rep_create = cls._create_report("01", "TOUR Growth Student 01")
        cls.rep_edit = cls._create_report("02", "TOUR Growth Student 02")
        cls.rep_delete = cls._create_report("03", "TOUR Growth Student 03")
        cls.rep_cancel = cls._create_report("10", "TOUR Growth Student 10")

        # 04-confirm: draft is enough, tour itself performs the confirm.
        cls.rep_confirm = cls._create_report("04", "TOUR Growth Student 04")

        # 05-approve / 06-reject: pre-drive to "confirm" as admin.
        cls.rep_approve = cls._create_report("05", "TOUR Growth Student 05")
        cls.rep_approve.with_user(cls.admin).action_confirm()
        cls.rep_reject = cls._create_report("06", "TOUR Growth Student 06")
        cls.rep_reject.with_user(cls.admin).action_confirm()

        # 09-finish: pre-drive all the way to "open".
        cls.rep_finish = cls._create_report("09", "TOUR Growth Student 09")
        cls.rep_finish.with_user(cls.admin).action_confirm()
        cls.rep_finish.with_user(cls.admin).action_approve_approval()

        # 12-restart: pre-drive to "cancel".
        cls.rep_restart = cls._create_report("12", "TOUR Growth Student 12")
        cls.rep_restart.with_user(cls.admin).action_cancel()

    def test_create(self):
        """Run the create tour for ``school_character_growth_report``.

        IK: docs/school_character_growth_report/01-create.md
        """
        self.start_tour(
            "/web", "ssi_school_character_growth_report_create", login="admin"
        )

    def test_edit(self):
        """Run the edit tour for ``school_character_growth_report``.

        IK: docs/school_character_growth_report/02-edit.md
        """
        self.start_tour(
            "/web", "ssi_school_character_growth_report_edit", login="admin"
        )

    def test_delete(self):
        """Run the delete tour for ``school_character_growth_report``.

        IK: docs/school_character_growth_report/03-delete.md
        """
        self.start_tour(
            "/web", "ssi_school_character_growth_report_delete", login="admin"
        )

    def test_confirm(self):
        """Run the confirm tour for ``school_character_growth_report``.

        IK: docs/school_character_growth_report/04-confirm.md
        """
        self.start_tour(
            "/web", "ssi_school_character_growth_report_confirm", login="admin"
        )

    def test_approve(self):
        """Run the approve tour for ``school_character_growth_report``.

        IK: docs/school_character_growth_report/05-approve.md
        """
        self.start_tour(
            "/web", "ssi_school_character_growth_report_approve", login="admin"
        )

    def test_reject(self):
        """Run the reject tour for ``school_character_growth_report``.

        IK: docs/school_character_growth_report/06-reject.md
        """
        self.start_tour(
            "/web", "ssi_school_character_growth_report_reject", login="admin"
        )

    def test_finish(self):
        """Run the finish (Done) tour for ``school_character_growth_report``.

        IK: docs/school_character_growth_report/09-finish.md
        """
        self.start_tour(
            "/web", "ssi_school_character_growth_report_finish", login="admin"
        )

    def test_cancel(self):
        """Run the cancel tour for ``school_character_growth_report``.

        IK: docs/school_character_growth_report/10-cancel.md
        """
        self.start_tour(
            "/web", "ssi_school_character_growth_report_cancel", login="admin"
        )

    def test_restart(self):
        """Run the restart tour for ``school_character_growth_report``.

        IK: docs/school_character_growth_report/12-restart.md
        """
        self.start_tour(
            "/web", "ssi_school_character_growth_report_restart", login="admin"
        )

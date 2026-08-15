# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase -- NOT HttpCase. See structure-and-runner.md "Base class".
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiSchoolCharacterActivity(HttpSavepointCase):
    """Tour tests for the ``school_character_activity`` work instructions."""

    @classmethod
    def _create_activity(cls, suffix, construct_name):
        """Create one draft activity owned by the tour's admin user.

        :param suffix: unique suffix used for the backing construct code.
        :param construct_name: unique construct name, used by tours to
            find this record's row in the list view.
        :return: the created ``school_character_activity`` record.
        """
        construct = cls.env["school_character_construct"].create(
            {
                "name": construct_name,
                "code": "TOUR-ACT-%s" % suffix,
                "profile_id": cls.profile.id,
            }
        )
        return cls.env["school_character_activity"].create(
            {
                "construct_id": construct.id,
                "user_id": cls.admin.id,
            }
        )

    @classmethod
    def setUpClass(cls):
        """Create the master data and per-tour fixture activities.

        user_id is explicit on every record: cls.env runs as SUPERUSER,
        and the ``school_character_activity_internal_user_rule`` record
        rule would otherwise hide these fixtures from the tour's admin
        session.
        """
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        cls.profile = cls.env["school_character_profile"].create(
            {"name": "TOUR Activity Profile", "code": "TOUR-ACT-PROFILE"}
        )
        cls.cancel_reason = cls.env["base.cancel_reason"].create(
            {
                "name": "TOUR Activity Cancel Reason",
                "code": "TOUR-ACT-CANCEL",
                "global_use": True,
            }
        )

        # 01-create / 02-edit / 03-delete / 10-cancel: draft is enough.
        cls.act_create = cls._create_activity("01", "TOUR Activity Construct 01")
        cls.act_edit = cls._create_activity("02", "TOUR Activity Construct 02")
        cls.act_delete = cls._create_activity("03", "TOUR Activity Construct 03")
        cls.act_cancel = cls._create_activity("10", "TOUR Activity Construct 10")

        # 04-confirm: draft is enough, tour itself performs the confirm.
        cls.act_confirm = cls._create_activity("04", "TOUR Activity Construct 04")

        # 05-approve / 06-reject: pre-drive to "confirm" as admin.
        cls.act_approve = cls._create_activity("05", "TOUR Activity Construct 05")
        cls.act_approve.with_user(cls.admin).action_confirm()
        cls.act_reject = cls._create_activity("06", "TOUR Activity Construct 06")
        cls.act_reject.with_user(cls.admin).action_confirm()

        # 09-finish: pre-drive all the way to "open".
        cls.act_finish = cls._create_activity("09", "TOUR Activity Construct 09")
        cls.act_finish.with_user(cls.admin).action_confirm()
        cls.act_finish.with_user(cls.admin).action_approve_approval()

        # 12-restart: pre-drive to "cancel".
        cls.act_restart = cls._create_activity("12", "TOUR Activity Construct 12")
        cls.act_restart.with_user(cls.admin).action_cancel()

    def test_create(self):
        """Run the create tour for ``school_character_activity``.

        IK: docs/school_character_activity/01-create.md
        """
        self.start_tour("/web", "ssi_school_character_activity_create", login="admin")

    def test_edit(self):
        """Run the edit tour for ``school_character_activity``.

        IK: docs/school_character_activity/02-edit.md
        """
        self.start_tour("/web", "ssi_school_character_activity_edit", login="admin")

    def test_delete(self):
        """Run the delete tour for ``school_character_activity``.

        IK: docs/school_character_activity/03-delete.md
        """
        self.start_tour("/web", "ssi_school_character_activity_delete", login="admin")

    def test_confirm(self):
        """Run the confirm tour for ``school_character_activity``.

        IK: docs/school_character_activity/04-confirm.md
        """
        self.start_tour("/web", "ssi_school_character_activity_confirm", login="admin")

    def test_approve(self):
        """Run the approve tour for ``school_character_activity``.

        IK: docs/school_character_activity/05-approve.md
        """
        self.start_tour("/web", "ssi_school_character_activity_approve", login="admin")

    def test_reject(self):
        """Run the reject tour for ``school_character_activity``.

        IK: docs/school_character_activity/06-reject.md
        """
        self.start_tour("/web", "ssi_school_character_activity_reject", login="admin")

    def test_finish(self):
        """Run the finish (Done) tour for ``school_character_activity``.

        IK: docs/school_character_activity/09-finish.md
        """
        self.start_tour("/web", "ssi_school_character_activity_finish", login="admin")

    def test_cancel(self):
        """Run the cancel tour for ``school_character_activity``.

        IK: docs/school_character_activity/10-cancel.md
        """
        self.start_tour("/web", "ssi_school_character_activity_cancel", login="admin")

    def test_restart(self):
        """Run the restart tour for ``school_character_activity``.

        IK: docs/school_character_activity/12-restart.md
        """
        self.start_tour("/web", "ssi_school_character_activity_restart", login="admin")

# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase -- NOT HttpCase. See structure-and-runner.md "Base class".
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiSchoolCharacterObservation(HttpSavepointCase):
    """Tour tests for the ``school_character_observation`` work
    instructions.
    """

    @classmethod
    def _create_observation(cls, suffix):
        """Create one draft observation for a uniquely-named student.

        :param suffix: unique suffix used for the student's name/code
            and the backing construct code; tours use the student
            name to find this record's row in the list view.
        :return: the created ``school_character_observation`` record.
        """
        contact = cls.env["res.partner"].create(
            {"name": "TOUR Observation Student %s Contact" % suffix}
        )
        student = cls.env["school_student"].create(
            {
                "name": "TOUR Observation Student %s" % suffix,
                "code": "TOUR-OBS-STU-%s" % suffix,
                "contact_id": contact.id,
                "school_id": cls.school.id,
            }
        )
        return cls.env["school_character_observation"].create(
            {
                "student_id": student.id,
                "construct_id": cls.construct.id,
                "user_id": cls.admin.id,
            }
        )

    @classmethod
    def setUpClass(cls):
        """Create the master data and per-tour fixture observations.

        user_id is explicit on every record: cls.env runs as
        SUPERUSER, and the
        ``school_character_observation_internal_user_rule`` record
        rule would otherwise hide these fixtures from the tour's
        admin session.
        """
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        cls.grade_type = cls.env["school_grade_type"].create(
            {"name": "TOUR Observation Grade Type", "sequence": 10}
        )
        cls.school = cls.env["school"].create(
            {
                "name": "TOUR Observation School",
                "code": "TOUR-OBS-SCHOOL",
                "grade_type_id": cls.grade_type.id,
            }
        )
        cls.construct = cls.env["school_character_construct"].create(
            {
                "name": "TOUR Observation Construct",
                "code": "TOUR-OBS-CON",
            }
        )
        cls.cancel_reason = cls.env["base.cancel_reason"].create(
            {
                "name": "TOUR Observation Cancel Reason",
                "code": "TOUR-OBS-CANCEL",
                "global_use": True,
            }
        )

        # 01-create / 02-edit / 03-delete / 10-cancel: draft is enough.
        cls.obs_create = cls._create_observation("01")
        cls.obs_edit = cls._create_observation("02")
        cls.obs_delete = cls._create_observation("03")
        cls.obs_cancel = cls._create_observation("10")

        # 04-confirm: draft is enough, tour itself performs the confirm.
        cls.obs_confirm = cls._create_observation("04")

        # 05-approve / 06-reject: pre-drive to "confirm" as admin.
        cls.obs_approve = cls._create_observation("05")
        cls.obs_approve.with_user(cls.admin).action_confirm()
        cls.obs_reject = cls._create_observation("06")
        cls.obs_reject.with_user(cls.admin).action_confirm()

        # 09-finish: pre-drive all the way to "open".
        cls.obs_finish = cls._create_observation("09")
        cls.obs_finish.with_user(cls.admin).action_confirm()
        cls.obs_finish.with_user(cls.admin).action_approve_approval()

        # 12-restart: pre-drive to "cancel".
        cls.obs_restart = cls._create_observation("12")
        cls.obs_restart.with_user(cls.admin).action_cancel()

    def test_create(self):
        """Run the create tour for ``school_character_observation``.

        IK: docs/school_character_observation/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_evidence_observation_create",
            login="admin",
        )

    def test_edit(self):
        """Run the edit tour for ``school_character_observation``.

        IK: docs/school_character_observation/02-edit.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_evidence_observation_edit",
            login="admin",
        )

    def test_delete(self):
        """Run the delete tour for ``school_character_observation``.

        IK: docs/school_character_observation/03-delete.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_evidence_observation_delete",
            login="admin",
        )

    def test_confirm(self):
        """Run the confirm tour for ``school_character_observation``.

        IK: docs/school_character_observation/04-confirm.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_evidence_observation_confirm",
            login="admin",
        )

    def test_approve(self):
        """Run the approve tour for ``school_character_observation``.

        IK: docs/school_character_observation/05-approve.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_evidence_observation_approve",
            login="admin",
        )

    def test_reject(self):
        """Run the reject tour for ``school_character_observation``.

        IK: docs/school_character_observation/06-reject.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_evidence_observation_reject",
            login="admin",
        )

    def test_finish(self):
        """Run the finish (Done) tour for ``school_character_observation``.

        IK: docs/school_character_observation/09-finish.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_evidence_observation_finish",
            login="admin",
        )

    def test_cancel(self):
        """Run the cancel tour for ``school_character_observation``.

        IK: docs/school_character_observation/10-cancel.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_evidence_observation_cancel",
            login="admin",
        )

    def test_restart(self):
        """Run the restart tour for ``school_character_observation``.

        IK: docs/school_character_observation/12-restart.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_evidence_observation_restart",
            login="admin",
        )

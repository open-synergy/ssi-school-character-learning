# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase -- NOT HttpCase. See structure-and-runner.md "Base class".
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiSchoolCharacterCalibration(HttpSavepointCase):
    """Tour tests for the ``school_character_calibration`` work
    instructions.
    """

    @classmethod
    def _create_calibration(cls, suffix):
        """Create one draft calibration tagged with a unique marker.

        :param suffix: unique suffix stored in ``agreement_result``
            (the only free-text field shown in the tree view), used
            by tours to find this record's row in the list view.
        :return: the created ``school_character_calibration`` record.
        """
        return cls.env["school_character_calibration"].create(
            {
                "agreement_result": "TOUR Calibration %s" % suffix,
                "user_id": cls.admin.id,
            }
        )

    @classmethod
    def setUpClass(cls):
        """Create the master data and per-tour fixture calibrations.

        user_id is explicit on every record: cls.env runs as
        SUPERUSER, and the
        ``school_character_calibration_internal_user_rule`` record
        rule would otherwise hide these fixtures from the tour's
        admin session.
        """
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        cls.construct = cls.env["school_character_construct"].create(
            {"name": "TOUR Calibration Construct", "code": "TOUR-CAL-CON"}
        )
        employee = cls.env["hr.employee"].create({"name": "TOUR Calibration Employee"})
        cls.participant = cls.env["school_teacher"].create(
            {
                "name": "TOUR Calibration Participant",
                "code": "TOUR-CAL-TCH",
                "employee_id": employee.id,
            }
        )
        cls.anchor = cls.env["school_character_anchor"].create(
            {
                "name": "TOUR Calibration Anchor",
                "code": "TOUR-CAL-ANCHOR",
                "construct_id": cls.construct.id,
            }
        )
        scale = cls.env["school_character_scale"].create(
            {"name": "TOUR Calibration Scale", "code": "TOUR-CAL-SCALE"}
        )
        cls.level = cls.env["school_character_level"].create(
            {
                "name": "TOUR Calibration Level",
                "code": "TOUR-CAL-LVL",
                "scale_id": scale.id,
                "sequence": 10,
            }
        )
        cls.cancel_reason = cls.env["base.cancel_reason"].create(
            {
                "name": "TOUR Calibration Cancel Reason",
                "code": "TOUR-CAL-CANCEL",
                "global_use": True,
            }
        )

        # 02-edit / 03-delete / 10-cancel: draft is enough.
        cls.cal_edit = cls._create_calibration("02")
        cls.cal_delete = cls._create_calibration("03")
        cls.cal_cancel = cls._create_calibration("10")

        # 04-confirm: draft is enough, tour itself performs the confirm.
        cls.cal_confirm = cls._create_calibration("04")

        # 05-approve / 06-reject: pre-drive to "confirm" as admin.
        cls.cal_approve = cls._create_calibration("05")
        cls.cal_approve.with_user(cls.admin).action_confirm()
        cls.cal_reject = cls._create_calibration("06")
        cls.cal_reject.with_user(cls.admin).action_confirm()

        # 09-finish: pre-drive all the way to "open".
        #
        # Between action_confirm() and action_approve_approval() the
        # record is flushed and its cache invalidated (scoped to its
        # own ids) -- without the refresh, action_approve_approval()
        # reads a stale cached approve_ok and raises "Document is not
        # allowed to approve" nondeterministically (mirrors
        # opnsynid-hr-expense/ssi_hr_cash_advance's
        # _create_open_cash_advance).
        cls.cal_finish = cls._create_calibration("09")
        cls.cal_finish.with_user(cls.admin).action_confirm()
        cls.cal_finish.flush()
        cls.cal_finish.invalidate_cache(ids=cls.cal_finish.ids)
        cls.cal_finish.with_user(cls.admin).action_approve_approval()

        # 12-restart: pre-drive to "cancel".
        cls.cal_restart = cls._create_calibration("12")
        cls.cal_restart.with_user(cls.admin).action_cancel()

    def test_create(self):
        """Run the create tour for ``school_character_calibration``.

        IK: docs/school_character_calibration/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_evidence_calibration_create",
            login="admin",
        )

    def test_edit(self):
        """Run the edit tour for ``school_character_calibration``.

        IK: docs/school_character_calibration/02-edit.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_evidence_calibration_edit",
            login="admin",
        )

    def test_delete(self):
        """Run the delete tour for ``school_character_calibration``.

        IK: docs/school_character_calibration/03-delete.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_evidence_calibration_delete",
            login="admin",
        )

    def test_confirm(self):
        """Run the confirm tour for ``school_character_calibration``.

        IK: docs/school_character_calibration/04-confirm.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_evidence_calibration_confirm",
            login="admin",
        )

    def test_approve(self):
        """Run the approve tour for ``school_character_calibration``.

        IK: docs/school_character_calibration/05-approve.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_evidence_calibration_approve",
            login="admin",
        )

    def test_reject(self):
        """Run the reject tour for ``school_character_calibration``.

        IK: docs/school_character_calibration/06-reject.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_evidence_calibration_reject",
            login="admin",
        )

    def test_finish(self):
        """Run the finish (Done) tour for ``school_character_calibration``.

        IK: docs/school_character_calibration/09-finish.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_evidence_calibration_finish",
            login="admin",
        )

    def test_cancel(self):
        """Run the cancel tour for ``school_character_calibration``.

        IK: docs/school_character_calibration/10-cancel.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_evidence_calibration_cancel",
            login="admin",
        )

    def test_restart(self):
        """Run the restart tour for ``school_character_calibration``.

        IK: docs/school_character_calibration/12-restart.md
        """
        self.start_tour(
            "/web",
            "ssi_school_character_evidence_calibration_restart",
            login="admin",
        )

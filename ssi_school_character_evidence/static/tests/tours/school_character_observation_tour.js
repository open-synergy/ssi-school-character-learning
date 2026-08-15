odoo.define(
    "ssi_school_character_evidence.school_character_observation_tour",
    function (require) {
        "use strict";

        var tour = require("web_tour.tour");

        function openMenuSteps() {
            return [
                tour.stepUtils.showAppsMenuItem(),
                {
                    content: "Open the School app",
                    trigger: '.o_app[data-menu-xmlid="ssi_school.menu_school_root"]',
                },
                {
                    content: "Open the Character Learning menu",
                    trigger:
                        '.o_menu_sections [data-menu-xmlid="ssi_school_character.menu_character_root"]',
                },
                // "Measurement" (menu_character_measurement_root) has
                // children (this menu and Calibration), so Odoo 14
                // renders it as a non-clickable
                // <div class="dropdown-header"> with no data-menu-xmlid
                // -- it never gets its own tour step (odoo-development-ui-test,
                // patterns.md "Jumlah level menu di IK != jumlah step").
                {
                    content: "Open the Character Observations menu",
                    trigger:
                        '.o_menu_sections [data-menu-xmlid="ssi_school_character_evidence.school_character_observation_menu"]',
                },
                {
                    content: "Character Observations list is displayed",
                    trigger:
                        ".o_control_panel .breadcrumb-item.active:contains(Character Observations)",
                    extra_trigger: ".o_list_view",
                    run: function () {
                        return true;
                    },
                },
            ];
        }

        // IK: docs/school_character_observation/01-create.md
        tour.register(
            "ssi_school_character_evidence_observation_create",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Click Create",
                    trigger: ".o_list_button_add",
                    extra_trigger: ".o_list_view",
                },
                {
                    content: "Form is open in edit mode",
                    trigger: ".o_form_view.o_form_editable",
                    run: function () {
                        return true;
                    },
                },
                {
                    content: "Select the Student",
                    trigger: ".o_field_many2one[name='student_id'] input",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text TOUR Observation Student 01",
                },
                {
                    content: "Pick the Student from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(TOUR Observation Student 01)",
                    in_modal: false,
                },
                {
                    content: "Select the Construct",
                    trigger: ".o_field_many2one[name='construct_id'] input",
                    run: "text TOUR Observation Construct",
                },
                {
                    content: "Pick the Construct from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(TOUR Observation Construct)",
                    in_modal: false,
                },
                {
                    content: "Save the record",
                    trigger: ".o_form_button_save",
                },
                {
                    content: "Record is saved in Draft",
                    trigger: ".o_form_view.o_form_readonly",
                    run: function () {
                        return true;
                    },
                },
            ])
        );

        // IK: docs/school_character_observation/02-edit.md
        tour.register(
            "ssi_school_character_evidence_observation_edit",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Observation Student 02) .o_data_cell:first",
                    extra_trigger: ".o_list_view",
                },
                {
                    content: "Click the Edit button",
                    trigger: ".o_form_button_edit",
                },
                {
                    content: "Form is now editable",
                    trigger: ".o_form_view.o_form_editable",
                    run: function () {
                        // Assertion only; let the edit-mode re-render
                        // settle before switching tabs, so the tab click
                        // below lands on the stable post-edit notebook
                        // rather than a transient node about to be
                        // replaced.
                    },
                },
                {
                    content: "Open the Summary tab",
                    trigger: ".o_notebook .nav-link:contains(Summary)",
                },
                {
                    content: "Change the Summary",
                    trigger: "textarea.o_field_widget[name='summary']",
                    run: "text Edited summary via tour.",
                },
                {
                    content: "Save the record",
                    trigger: ".o_form_button_save",
                },
                {
                    content: "Record is saved",
                    trigger: ".o_form_view.o_form_readonly",
                    run: function () {
                        return true;
                    },
                },
            ])
        );

        // IK: docs/school_character_observation/03-delete.md
        tour.register(
            "ssi_school_character_evidence_observation_delete",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Observation Student 03) .o_data_cell:first",
                    extra_trigger: ".o_list_view",
                },
                {
                    trigger: ".o_form_view",
                    run: function () {
                        return true;
                    },
                },
                {
                    content: "Open the Action menu",
                    trigger: ".o_cp_action_menus button:contains(Action)",
                },
                {
                    content: "Click Delete",
                    trigger: ".o_cp_action_menus .o_menu_item a",
                    run: function () {
                        var $delete = $(".o_cp_action_menus .o_menu_item a").filter(
                            function () {
                                return $(this).text().trim() === "Delete";
                            }
                        );
                        $delete[0].click();
                    },
                },
                {
                    content: "Confirm deletion",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },
                {
                    content: "Back to the list",
                    trigger:
                        ".breadcrumb-item.o_back_button a:contains(Character Observations)",
                },
                {
                    content: "Record no longer in the list",
                    trigger:
                        ".o_list_view:not(:has(.o_data_row:contains(TOUR Observation Student 03)))",
                    run: function () {
                        return true;
                    },
                },
            ])
        );

        // IK: docs/school_character_observation/04-confirm.md
        tour.register(
            "ssi_school_character_evidence_observation_confirm",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Observation Student 04) .o_data_cell:first",
                    extra_trigger: ".o_list_view",
                },
                {
                    trigger: ".o_form_view",
                    run: function () {
                        return true;
                    },
                },
                {
                    content: "Click the Confirm button",
                    trigger: ".o_statusbar_buttons button[name='action_confirm']",
                    extra_trigger: ".o_form_view",
                },
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },
                {
                    content: "Status is Waiting for Approval",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='confirm'].btn-primary",
                    run: function () {
                        return true;
                    },
                },
            ])
        );

        // IK: docs/school_character_observation/05-approve.md
        tour.register(
            "ssi_school_character_evidence_observation_approve",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Observation Student 05) .o_data_cell:first",
                    extra_trigger: ".o_list_view",
                },
                {
                    trigger: ".o_form_view",
                    run: function () {
                        return true;
                    },
                },
                {
                    content: "Click the Approve button",
                    trigger:
                        ".o_statusbar_buttons button[name='action_approve_approval']",
                    extra_trigger: ".o_form_view",
                },
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },
                {
                    content: "Status is Open",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='open'].btn-primary",
                    run: function () {
                        return true;
                    },
                },
            ])
        );

        // IK: docs/school_character_observation/06-reject.md
        tour.register(
            "ssi_school_character_evidence_observation_reject",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Observation Student 06) .o_data_cell:first",
                    extra_trigger: ".o_list_view",
                },
                {
                    trigger: ".o_form_view",
                    run: function () {
                        return true;
                    },
                },
                {
                    content: "Click the Reject button",
                    trigger:
                        ".o_statusbar_buttons button[name='action_reject_approval']",
                    extra_trigger: ".o_form_view",
                },
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },
                {
                    content: "Status is Reject",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='reject'].btn-primary",
                    run: function () {
                        return true;
                    },
                },
            ])
        );

        // IK: docs/school_character_observation/09-finish.md
        tour.register(
            "ssi_school_character_evidence_observation_finish",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Observation Student 09) .o_data_cell:first",
                    extra_trigger: ".o_list_view",
                },
                {
                    trigger: ".o_form_view",
                    run: function () {
                        return true;
                    },
                },
                {
                    content: "Click the Done button",
                    trigger: ".o_statusbar_buttons button[name='action_done']",
                    extra_trigger: ".o_form_view",
                },
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },
                {
                    content: "Status is Done",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='done'].btn-primary",
                    run: function () {
                        return true;
                    },
                },
            ])
        );

        // IK: docs/school_character_observation/10-cancel.md
        tour.register(
            "ssi_school_character_evidence_observation_cancel",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Observation Student 10) .o_data_cell:first",
                    extra_trigger: ".o_list_view",
                },
                {
                    trigger: ".o_form_view",
                    run: function () {
                        return true;
                    },
                },
                {
                    content: "Click the Cancel button",
                    trigger: ".o_statusbar_buttons button:enabled:contains('Cancel')",
                    extra_trigger: ".o_form_view",
                },
                {
                    content: "Wizard is open",
                    trigger: ".o_form_view",
                    run: function () {
                        return true;
                    },
                },
                // Cancel_reason_id is rendered widget="radio"
                // (base_select_cancel_reason_view_form) -- not a
                // many2one autocomplete input, so it's a single click
                // on the matching radio option's label, not
                // type-then-pick.
                {
                    content: "Select the cancellation reason",
                    trigger:
                        ".o_field_widget[name='cancel_reason_id'] .o_radio_item label:contains('TOUR Observation Cancel Reason')",
                },
                // The wizard's Confirm button carries confirm="Are
                // you sure?" (base_select_cancel_reason_view_form),
                // which opens a SECOND, stacked Dialog.confirm() --
                // action_confirm() only actually runs once that
                // dialog's own "Ok" button (class btn-primary) is
                // clicked too.
                {
                    content: "Confirm the wizard",
                    trigger: ".modal-footer button[name='action_confirm']",
                },
                {
                    content: 'Confirm the "Are you sure?" dialog',
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },
                {
                    content: "Status is Cancel",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='cancel'].btn-primary",
                    run: function () {
                        return true;
                    },
                },
            ])
        );

        // IK: docs/school_character_observation/12-restart.md
        tour.register(
            "ssi_school_character_evidence_observation_restart",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Observation Student 12) .o_data_cell:first",
                    extra_trigger: ".o_list_view",
                },
                {
                    trigger: ".o_form_view",
                    run: function () {
                        return true;
                    },
                },
                {
                    content: "Click the Restart button",
                    trigger: ".o_statusbar_buttons button[name='action_restart']",
                    extra_trigger: ".o_form_view",
                },
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },
                {
                    content: "Status is Draft",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='draft'].btn-primary",
                    run: function () {
                        return true;
                    },
                },
            ])
        );
    }
);

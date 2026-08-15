odoo.define(
    "ssi_school_character_evidence.school_character_calibration_tour",
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
                // children (this menu and Observation), so Odoo 14
                // renders it as a non-clickable
                // <div class="dropdown-header"> with no data-menu-xmlid
                // -- it never gets its own tour step (odoo-development-ui-test,
                // patterns.md "Jumlah level menu di IK != jumlah step").
                {
                    content: "Open the Character Teacher Calibrations menu",
                    trigger:
                        '.o_menu_sections [data-menu-xmlid="ssi_school_character_evidence.school_character_calibration_menu"]',
                },
                {
                    content: "Character Teacher Calibrations list is displayed",
                    trigger:
                        ".o_control_panel .breadcrumb-item.active:contains(Character Teacher Calibrations)",
                    extra_trigger: ".o_list_view",
                    run: function () {
                        return true;
                    },
                },
            ];
        }

        // IK: docs/school_character_calibration/01-create.md
        tour.register(
            "ssi_school_character_evidence_calibration_create",
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
                    content: "Open the Scope tab",
                    trigger: ".o_notebook .nav-link:contains(Scope)",
                },
                {
                    content: "Add a Construct to the scope",
                    trigger: ".o_field_many2many_tags[name='construct_ids'] input",
                    run: "text TOUR Calibration Construct",
                },
                {
                    content: "Pick the Construct from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(TOUR Calibration Construct)",
                    in_modal: false,
                },
                {
                    content: "Add a Participant to the scope",
                    trigger: ".o_field_many2many_tags[name='participant_ids'] input",
                    run: "text TOUR Calibration Participant",
                },
                {
                    content: "Pick the Participant from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(TOUR Calibration Participant)",
                    in_modal: false,
                },
                {
                    content: "Add an Anchor to the scope",
                    trigger: ".o_field_many2many_tags[name='anchor_ids'] input",
                    run: "text TOUR Calibration Anchor",
                },
                {
                    content: "Pick the Anchor from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(TOUR Calibration Anchor)",
                    in_modal: false,
                },
                {
                    content: "Open the Ratings tab",
                    trigger: ".o_notebook .nav-link:contains(Ratings)",
                },
                {
                    content: "Add a rating line",
                    trigger: ".o_field_x2many_list_row_add a",
                },
                {
                    content: "Select the Participant on the rating line",
                    trigger:
                        ".o_field_widget[name='rating_ids'] .o_selected_row .o_field_many2one[name='participant_id'] input",
                    run: "text TOUR Calibration Participant",
                },
                {
                    content: "Pick the Participant on the rating line",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(TOUR Calibration Participant)",
                    in_modal: false,
                },
                {
                    content: "Select the Anchor on the rating line",
                    trigger:
                        ".o_field_widget[name='rating_ids'] .o_selected_row .o_field_many2one[name='anchor_id'] input",
                    run: "text TOUR Calibration Anchor",
                },
                {
                    content: "Pick the Anchor on the rating line",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(TOUR Calibration Anchor)",
                    in_modal: false,
                },
                {
                    content: "Select the Assigned Level on the rating line",
                    trigger:
                        ".o_field_widget[name='rating_ids'] .o_selected_row .o_field_many2one[name='assigned_level_id'] input",
                    run: "text TOUR Calibration Level",
                },
                {
                    content: "Pick the Assigned Level on the rating line",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(TOUR Calibration Level)",
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

        // IK: docs/school_character_calibration/02-edit.md
        tour.register(
            "ssi_school_character_evidence_calibration_edit",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Calibration 02) .o_data_cell:first",
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
                    content: "Open the Notes tab",
                    trigger: ".o_notebook .nav-link:contains(Notes)",
                },
                {
                    content: "Change the Notes",
                    trigger: "textarea.o_field_widget[name='notes']",
                    run: "text Edited notes via tour.",
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

        // IK: docs/school_character_calibration/03-delete.md
        tour.register(
            "ssi_school_character_evidence_calibration_delete",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Calibration 03) .o_data_cell:first",
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
                        ".breadcrumb-item.o_back_button a:contains(Character Teacher Calibrations)",
                },
                {
                    content: "Record no longer in the list",
                    trigger:
                        ".o_list_view:not(:has(.o_data_row:contains(TOUR Calibration 03)))",
                    run: function () {
                        return true;
                    },
                },
            ])
        );

        // IK: docs/school_character_calibration/04-confirm.md
        tour.register(
            "ssi_school_character_evidence_calibration_confirm",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Calibration 04) .o_data_cell:first",
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

        // IK: docs/school_character_calibration/05-approve.md
        tour.register(
            "ssi_school_character_evidence_calibration_approve",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Calibration 05) .o_data_cell:first",
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

        // IK: docs/school_character_calibration/06-reject.md
        tour.register(
            "ssi_school_character_evidence_calibration_reject",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Calibration 06) .o_data_cell:first",
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

        // IK: docs/school_character_calibration/09-finish.md
        tour.register(
            "ssi_school_character_evidence_calibration_finish",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Calibration 09) .o_data_cell:first",
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

        // IK: docs/school_character_calibration/10-cancel.md
        tour.register(
            "ssi_school_character_evidence_calibration_cancel",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Calibration 10) .o_data_cell:first",
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
                // cancel_reason_id is rendered widget="radio"
                // (base_select_cancel_reason_view_form) -- not a
                // many2one autocomplete input, so it's a single click
                // on the matching radio option's label, not
                // type-then-pick.
                {
                    content: "Select the cancellation reason",
                    trigger:
                        ".o_field_widget[name='cancel_reason_id'] .o_radio_item label:contains('TOUR Calibration Cancel Reason')",
                },
                {
                    content: "Confirm the wizard",
                    trigger: ".modal-footer button[name='action_confirm']",
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

        // IK: docs/school_character_calibration/12-restart.md
        tour.register(
            "ssi_school_character_evidence_calibration_restart",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Calibration 12) .o_data_cell:first",
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

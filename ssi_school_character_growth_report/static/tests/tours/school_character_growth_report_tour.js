odoo.define(
    "ssi_school_character_growth_report.school_character_growth_report_tour",
    function (require) {
        "use strict";

        var tour = require("web_tour.tour");

        // Shared Flow 1 — Open the School > Character Learning > Growth Report >
        // Character Growth Reports menu.
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
                {
                    content: "Open the Growth Report menu",
                    trigger:
                        '.o_menu_sections [data-menu-xmlid="ssi_school_character_growth_report.menu_character_growth_report_root"]',
                },
                {
                    content: "Open the Character Growth Reports menu",
                    trigger:
                        '.o_menu_sections [data-menu-xmlid="ssi_school_character_growth_report.school_character_growth_report_menu"]',
                },
                {
                    content: "Character Growth Reports list is displayed",
                    trigger:
                        ".o_control_panel .breadcrumb-item.active:contains(Character Growth Reports)",
                    extra_trigger: ".o_list_view",
                    run: function () {
                        return true;
                    },
                },
            ];
        }

        // IK: docs/school_character_growth_report/01-create.md
        tour.register(
            "ssi_school_character_growth_report_create",
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
                    run: "text TOUR Growth Student 01",
                },
                {
                    content: "Pick the Student from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(TOUR Growth Student 01)",
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

        // IK: docs/school_character_growth_report/02-edit.md
        tour.register(
            "ssi_school_character_growth_report_edit",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Growth Student 02) .o_data_cell:first",
                    extra_trigger: ".o_list_view",
                },
                {
                    content: "Click the Edit button",
                    trigger: ".o_form_button_edit",
                },
                {
                    content: "Change the Overall Narrative",
                    trigger: "a.nav-link:contains(Overall Narrative)",
                    extra_trigger: ".o_form_view.o_form_editable",
                },
                {
                    content: "Fill in Overall Narrative",
                    trigger: ".o_field_widget[name='overall_narrative'] textarea",
                    run: "text Edited narrative via tour.",
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

        // IK: docs/school_character_growth_report/03-delete.md
        tour.register(
            "ssi_school_character_growth_report_delete",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Growth Student 03) .o_data_cell:first",
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
                        ".breadcrumb-item.o_back_button a:contains(Character Growth Reports)",
                },
                {
                    content: "Record no longer in the list",
                    trigger:
                        ".o_list_view:not(:has(.o_data_row:contains(TOUR Growth Student 03)))",
                    run: function () {
                        return true;
                    },
                },
            ])
        );

        // IK: docs/school_character_growth_report/04-confirm.md
        tour.register(
            "ssi_school_character_growth_report_confirm",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Growth Student 04) .o_data_cell:first",
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

        // IK: docs/school_character_growth_report/05-approve.md
        tour.register(
            "ssi_school_character_growth_report_approve",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Growth Student 05) .o_data_cell:first",
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

        // IK: docs/school_character_growth_report/06-reject.md
        tour.register(
            "ssi_school_character_growth_report_reject",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Growth Student 06) .o_data_cell:first",
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

        // IK: docs/school_character_growth_report/09-finish.md
        tour.register(
            "ssi_school_character_growth_report_finish",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Growth Student 09) .o_data_cell:first",
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

        // IK: docs/school_character_growth_report/10-cancel.md
        tour.register(
            "ssi_school_character_growth_report_cancel",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Growth Student 10) .o_data_cell:first",
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
                {
                    content: "Select the cancellation reason",
                    trigger: ".o_field_many2one[name='cancel_reason_id'] input",
                    run: "text TOUR Growth Cancel Reason",
                },
                {
                    content: "Pick the reason",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(TOUR Growth Cancel Reason)",
                    in_modal: false,
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

        // IK: docs/school_character_growth_report/12-restart.md
        tour.register(
            "ssi_school_character_growth_report_restart",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Growth Student 12) .o_data_cell:first",
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

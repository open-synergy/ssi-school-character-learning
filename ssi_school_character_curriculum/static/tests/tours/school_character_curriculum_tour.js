odoo.define(
    "ssi_school_character_curriculum.school_character_curriculum_tour",
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
                // "Curriculum" (menu_character_curriculum_root) has a
                // child (this menu), so Odoo 14 renders it as a
                // non-clickable <div class="dropdown-header"> with no
                // data-menu-xmlid -- it never gets its own tour step
                // (odoo-development-ui-test, patterns.md "Jumlah level
                // menu di IK != jumlah step").
                {
                    content: "Open the Character Curriculum Maps menu",
                    trigger:
                        '.o_menu_sections [data-menu-xmlid="ssi_school_character_curriculum.school_character_curriculum_menu"]',
                },
                {
                    content: "Character Curriculum Maps list is displayed",
                    trigger:
                        ".o_control_panel .breadcrumb-item.active:contains(Character Curriculum Maps)",
                    extra_trigger: ".o_list_view",
                    run: function () {
                        return true;
                    },
                },
            ];
        }

        // IK: docs/school_character_curriculum/01-create.md
        tour.register(
            "ssi_school_character_curriculum_create",
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
                    content: "Select the Academic Year",
                    trigger: ".o_field_many2one[name='academic_year_id'] input",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text TOUR Curriculum Year 01",
                },
                {
                    content: "Pick the Academic Year from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(TOUR Curriculum Year 01)",
                    in_modal: false,
                },
                {
                    content: "Select the Character Profile",
                    trigger: ".o_field_many2one[name='profile_id'] input",
                    run: "text TOUR Curriculum Profile",
                },
                {
                    content: "Pick the Character Profile from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(TOUR Curriculum Profile)",
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

        // IK: docs/school_character_curriculum/02-edit.md
        tour.register(
            "ssi_school_character_curriculum_edit",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Curriculum Year 02) .o_data_cell:first",
                    extra_trigger: ".o_list_view",
                },
                {
                    content: "Click the Edit button",
                    trigger: ".o_form_button_edit",
                },
                {
                    content: "Change the Pathway",
                    trigger: "select.o_field_widget[name='pathway']",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text Full",
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

        // IK: docs/school_character_curriculum/03-delete.md
        tour.register(
            "ssi_school_character_curriculum_delete",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Curriculum Year 03) .o_data_cell:first",
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
                        ".breadcrumb-item.o_back_button a:contains(Character Curriculum Maps)",
                },
                {
                    content: "Record no longer in the list",
                    trigger:
                        ".o_list_view:not(:has(.o_data_row:contains(TOUR Curriculum Year 03)))",
                    run: function () {
                        return true;
                    },
                },
            ])
        );

        // IK: docs/school_character_curriculum/04-confirm.md
        tour.register(
            "ssi_school_character_curriculum_confirm",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Curriculum Year 04) .o_data_cell:first",
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

        // IK: docs/school_character_curriculum/05-approve.md
        tour.register(
            "ssi_school_character_curriculum_approve",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Curriculum Year 05) .o_data_cell:first",
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

        // IK: docs/school_character_curriculum/06-reject.md
        tour.register(
            "ssi_school_character_curriculum_reject",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Curriculum Year 06) .o_data_cell:first",
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

        // IK: docs/school_character_curriculum/09-finish.md
        tour.register(
            "ssi_school_character_curriculum_finish",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Curriculum Year 09) .o_data_cell:first",
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

        // IK: docs/school_character_curriculum/10-cancel.md
        tour.register(
            "ssi_school_character_curriculum_cancel",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Curriculum Year 10) .o_data_cell:first",
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
                        ".o_field_widget[name='cancel_reason_id'] .o_radio_item label:contains('TOUR Curriculum Cancel Reason')",
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

        // IK: docs/school_character_curriculum/12-restart.md
        tour.register(
            "ssi_school_character_curriculum_restart",
            {test: true, url: "/web"},
            [].concat(openMenuSteps(), [
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR Curriculum Year 12) .o_data_cell:first",
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

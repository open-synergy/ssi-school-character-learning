odoo.define("ssi_school_character_activity.school_character_activity_tour", function (
    require
) {
    "use strict";

    var tour = require("web_tour.tour");

    // Shared Flow 1 — Open the School > Character Learning > Activity >
    // Character Learning Activities menu. "Activity" is a grouping header
    // with a single leaf child, so it renders WITHOUT a data-menu-xmlid and
    // is skipped (see patterns.md "Jumlah level menu di IK != jumlah step").
    function openActivityMenuSteps() {
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
                content: "Open the Character Learning Activities menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_character_activity.school_character_activity_menu"]',
            },
            {
                content: "Character Learning Activities list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Character Learning Activities)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; gate on the destination action's title.
                    return true;
                },
            },
        ];
    }

    // IK: docs/school_character_activity/01-create.md
    tour.register(
        "ssi_school_character_activity_create",
        {test: true, url: "/web"},
        [].concat(openActivityMenuSteps(), [
            // Flow 2 — Click the New button.
            {
                content: "Click Create",
                trigger: ".o_list_button_add",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open in edit mode",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only.
                    return true;
                },
            },
            // Flow 3 — Fill in the required fields.
            {
                content: "Select the Construct",
                trigger: ".o_field_many2one[name='construct_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR Activity Construct 01",
            },
            {
                content: "Pick the Construct from the dropdown",
                trigger:
                    ".ui-autocomplete .ui-menu-item a:contains(TOUR Activity Construct 01)",
                in_modal: false,
            },
            // Flow 5 — Save.
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },
            // Post-Condition — A new record is created in Draft status.
            {
                content: "Record is saved in Draft",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only.
                    return true;
                },
            },
        ])
    );

    // IK: docs/school_character_activity/02-edit.md
    tour.register(
        "ssi_school_character_activity_edit",
        {test: true, url: "/web"},
        [].concat(openActivityMenuSteps(), [
            // Flow 2 — Find and open the record to edit.
            {
                content: "Open the record",
                trigger:
                    ".o_data_row:contains(TOUR Activity Construct 02) .o_data_cell:first",
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
                    // Assertion only.
                    return true;
                },
            },
            // Flow 3 — Change the required fields.
            {
                content: "Change the Learning Objective",
                trigger: ".o_field_widget[name='objective']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Edited objective via tour.",
            },
            // Flow 5 — Save.
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },
            // Post-Condition — The record is updated with the new values.
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only.
                    return true;
                },
            },
        ])
    );

    // IK: docs/school_character_activity/03-delete.md
    tour.register(
        "ssi_school_character_activity_delete",
        {test: true, url: "/web"},
        [].concat(openActivityMenuSteps(), [
            // Flow 2 — Open the record to delete.
            {
                content: "Open the record",
                trigger:
                    ".o_data_row:contains(TOUR Activity Construct 03) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                trigger: ".o_form_view",
                run: function () {
                    return true;
                },
            },
            // Flow 3 — Click Action > Delete.
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
            // Flow 4 — Click OK to confirm.
            {
                content: "Confirm deletion",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            // Post-Condition — record is gone from the list.
            {
                content: "Back to the list",
                trigger:
                    ".breadcrumb-item.o_back_button a:contains(Character Learning Activities)",
            },
            {
                content: "Record no longer in the list",
                trigger:
                    ".o_list_view:not(:has(.o_data_row:contains(TOUR Activity Construct 03)))",
                run: function () {
                    // Assertion only.
                    return true;
                },
            },
        ])
    );

    // IK: docs/school_character_activity/04-confirm.md
    tour.register(
        "ssi_school_character_activity_confirm",
        {test: true, url: "/web"},
        [].concat(openActivityMenuSteps(), [
            // Flow 2 — Open the record to confirm.
            {
                content: "Open the record",
                trigger:
                    ".o_data_row:contains(TOUR Activity Construct 04) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                trigger: ".o_form_view",
                run: function () {
                    return true;
                },
            },
            // Flow 3 — Click Confirm.
            {
                content: "Click the Confirm button",
                trigger: ".o_statusbar_buttons button[name='action_confirm']",
                extra_trigger: ".o_form_view",
            },
            // Flow 4 — Click OK on the confirmation dialog.
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            // Post-Condition — status is Waiting for Approval.
            {
                content: "Status is Waiting for Approval",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='confirm'].btn-primary",
                run: function () {
                    // Assertion only.
                    return true;
                },
            },
        ])
    );

    // IK: docs/school_character_activity/05-approve.md
    tour.register(
        "ssi_school_character_activity_approve",
        {test: true, url: "/web"},
        [].concat(openActivityMenuSteps(), [
            {
                content: "Open the record",
                trigger:
                    ".o_data_row:contains(TOUR Activity Construct 05) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                trigger: ".o_form_view",
                run: function () {
                    return true;
                },
            },
            // Flow 3 — Click Approve.
            {
                content: "Click the Approve button",
                trigger: ".o_statusbar_buttons button[name='action_approve_approval']",
                extra_trigger: ".o_form_view",
            },
            // Flow 4 — Click OK on the confirmation dialog.
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            // Post-Condition — auto-transitions to Open.
            {
                content: "Status is Open",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='open'].btn-primary",
                run: function () {
                    // Assertion only.
                    return true;
                },
            },
        ])
    );

    // IK: docs/school_character_activity/06-reject.md
    tour.register(
        "ssi_school_character_activity_reject",
        {test: true, url: "/web"},
        [].concat(openActivityMenuSteps(), [
            {
                content: "Open the record",
                trigger:
                    ".o_data_row:contains(TOUR Activity Construct 06) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                trigger: ".o_form_view",
                run: function () {
                    return true;
                },
            },
            // Flow 3 — Click Reject.
            {
                content: "Click the Reject button",
                trigger: ".o_statusbar_buttons button[name='action_reject_approval']",
                extra_trigger: ".o_form_view",
            },
            // Flow 4 — Click OK on the confirmation dialog.
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            // Post-Condition — status is Reject.
            {
                content: "Status is Reject",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='reject'].btn-primary",
                run: function () {
                    // Assertion only.
                    return true;
                },
            },
        ])
    );

    // IK: docs/school_character_activity/09-finish.md
    tour.register(
        "ssi_school_character_activity_finish",
        {test: true, url: "/web"},
        [].concat(openActivityMenuSteps(), [
            {
                content: "Open the record",
                trigger:
                    ".o_data_row:contains(TOUR Activity Construct 09) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                trigger: ".o_form_view",
                run: function () {
                    return true;
                },
            },
            // Flow 3 — Click Done.
            {
                content: "Click the Done button",
                trigger: ".o_statusbar_buttons button[name='action_done']",
                extra_trigger: ".o_form_view",
            },
            // Flow 4 — Click OK on the confirmation dialog.
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            // Post-Condition — status is Done.
            {
                content: "Status is Done",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='done'].btn-primary",
                run: function () {
                    // Assertion only.
                    return true;
                },
            },
        ])
    );

    // IK: docs/school_character_activity/10-cancel.md
    tour.register(
        "ssi_school_character_activity_cancel",
        {test: true, url: "/web"},
        [].concat(openActivityMenuSteps(), [
            {
                content: "Open the record",
                trigger:
                    ".o_data_row:contains(TOUR Activity Construct 10) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                trigger: ".o_form_view",
                run: function () {
                    return true;
                },
            },
            // Flow 3 — Click Cancel. This is a type="action" button, so
            // its rendered `name` is a numeric action id -- target by
            // label instead (selectors.md "Pengecualian type='action'").
            {
                content: "Click the Cancel button",
                trigger: ".o_statusbar_buttons button:enabled:contains('Cancel')",
                extra_trigger: ".o_form_view",
            },
            // Flow 4 — In the wizard, select the Reason.
            {
                content: "Wizard is open",
                trigger: ".o_form_view",
                run: function () {
                    return true;
                },
            },
            // cancel_reason_id is rendered widget="radio"
            // (base_select_cancel_reason_view_form) -- not a many2one
            // autocomplete input, so it's a single click on the
            // matching radio option's label, not type-then-pick.
            {
                content: "Select the cancellation reason",
                trigger:
                    ".o_field_widget[name='cancel_reason_id'] .o_radio_item label:contains('TOUR Activity Cancel Reason')",
            },
            // Flow 5 — Click Confirm.
            {
                content: "Confirm the wizard",
                trigger: ".modal-footer button[name='action_confirm']",
            },
            // Post-Condition — status is Cancel.
            {
                content: "Status is Cancel",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='cancel'].btn-primary",
                run: function () {
                    // Assertion only.
                    return true;
                },
            },
        ])
    );

    // IK: docs/school_character_activity/12-restart.md
    tour.register(
        "ssi_school_character_activity_restart",
        {test: true, url: "/web"},
        [].concat(openActivityMenuSteps(), [
            {
                content: "Open the record",
                trigger:
                    ".o_data_row:contains(TOUR Activity Construct 12) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                trigger: ".o_form_view",
                run: function () {
                    return true;
                },
            },
            // Flow 3 — Click Restart.
            {
                content: "Click the Restart button",
                trigger: ".o_statusbar_buttons button[name='action_restart']",
                extra_trigger: ".o_form_view",
            },
            // Flow 4 — Click OK on the confirmation dialog.
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            // Post-Condition — status is back to Draft.
            {
                content: "Status is Draft",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='draft'].btn-primary",
                run: function () {
                    // Assertion only.
                    return true;
                },
            },
        ])
    );
});

odoo.define("ssi_school_character.school_character_method_tour", function (require) {
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
                content: "Open the Configuration menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school.menu_school_configuration"]',
            },
            {
                content: "Open the Character Methods menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_character.school_character_method_menu"]',
            },
            {
                content: "Character Methods list is displayed",
                trigger: ".o_control_panel .breadcrumb-item.active:contains(Character Methods)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ];
    }

    // IK: docs/school_character_method/01-create.md
    tour.register(
        "ssi_school_character_school_character_method_create",
        {test: true, url: "/web"},
        [
            ...openMenuSteps(),
            {
                content: "Click Create",
                trigger: ".o_list_button_add",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open in edit mode",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Fill in Name",
                trigger: ".o_field_widget[name='name']",
                run: "text Tour Character Method New",
            },
            {
                content: "Fill in Code",
                trigger: ".o_field_widget[name='code']",
                run: "text TOUR-NEW-METHOD",
            },
            {
                content: "Fill in description",
                trigger: ".o_field_widget[name='description'] textarea",
                run: "text Updated by tour.",
            },
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/school_character_method/02-edit.md
    tour.register(
        "ssi_school_character_school_character_method_edit",
        {test: true, url: "/web"},
        [
            ...openMenuSteps(),
            {
                content: "Open the record to edit",
                trigger: ".o_data_row:contains(Tour Character Method Edit)",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Click Edit",
                trigger: ".o_form_button_edit",
            },
            {
                content: "Change the description",
                trigger: ".o_field_widget[name='description'] textarea",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Updated by tour.",
            },
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/school_character_method/03-delete.md
    tour.register(
        "ssi_school_character_school_character_method_delete",
        {test: true, url: "/web"},
        [
            ...openMenuSteps(),
            {
                content: "Open the record to delete",
                trigger: ".o_data_row:contains(Tour Character Method Delete)",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Open the Action menu",
                trigger: ".o_cp_action_menus button:contains(Action)",
            },
            {
                content: "Click Delete",
                trigger: ".o_cp_action_menus .o_menu_item a",
                run: function () {
                    var $delete = $(".o_cp_action_menus .o_menu_item a").filter(function () {
                        return $(this).text().trim() === "Delete";
                    });
                    $delete[0].click();
                },
            },
            {
                content: "Confirm deletion",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            {
                content: "Click the Character Methods breadcrumb to return to the list",
                trigger: ".breadcrumb-item.o_back_button a:contains(Character Methods)",
            },
            {
                content: "Back to the list",
                trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/school_character_method/04-deactivate.md
    tour.register(
        "ssi_school_character_school_character_method_deactivate",
        {test: true, url: "/web"},
        [
            ...openMenuSteps(),
            {
                content: "Select the record to deactivate",
                trigger:
                    ".o_data_row:contains(Tour Character Method Deactivate) .o_list_record_selector input",
            },
            {
                content: "Open the Action menu",
                trigger: ".o_cp_action_menus button:contains(Action)",
            },
            {
                content: "Click Archive",
                trigger: ".o_cp_action_menus .o_menu_item a",
                run: function () {
                    var $archive = $(".o_cp_action_menus .o_menu_item a").filter(function () {
                        return $(this).text().trim() === "Archive";
                    });
                    $archive[0].click();
                },
            },
            {
                content: "Confirm archiving",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            {
                content: "The record no longer appears in the default list view",
                trigger: ".o_list_view:not(:has(.o_data_row:contains(Tour Character Method Deactivate)))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/school_character_method/05-activate.md
    tour.register(
        "ssi_school_character_school_character_method_activate",
        {test: true, url: "/web"},
        [
            ...openMenuSteps(),
            {
                content: "Open the Filters menu",
                trigger: ".o_search_options .o_dropdown button:contains(Filters)",
                run: function () {
                    this.$anchor[0].click();
                },
            },
            {
                content: "Enable the Archived filter",
                trigger: ".o_filter_menu .o_menu_item a:contains(Archived)",
                run: function () {
                    this.$anchor[0].click();
                },
            },
            {
                content: "Archived filter is applied",
                trigger:
                    ".o_filter_menu .o_menu_item a:contains(Archived)[aria-checked='true']",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Select the record to reactivate",
                trigger:
                    ".o_data_row:contains(Tour Character Method Activate) .o_list_record_selector input",
            },
            {
                content: "Open the Action menu",
                trigger: ".o_cp_action_menus button:contains(Action)",
            },
            {
                content: "Click Unarchive",
                trigger: ".o_cp_action_menus .o_menu_item a",
                run: function () {
                    var $unarchive = $(".o_cp_action_menus .o_menu_item a").filter(function () {
                        return $(this).text().trim() === "Unarchive";
                    });
                    $unarchive[0].click();
                },
            },
            {
                content: "The record is restored and listed again",
                trigger: ".o_data_row:contains(Tour Character Method Activate)",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );
});

odoo.define("ssi_school_character.school_character_subconstruct_tour", function (require) {
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
                content: "Open the Character Sub-constructs menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_character.school_character_subconstruct_menu"]',
            },
            {
                content: "Character Sub-constructs list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Character Sub-constructs)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },
        ];
    }

    // IK: docs/school_character_subconstruct/01-create.md
    tour.register(
        "ssi_school_character_school_character_subconstruct_create",
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
                    // Assertion only.
                },
            },
            {
                content: "Fill in Name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour Subconstruct New",
            },
            {
                content: "Fill in Code",
                trigger: ".o_field_widget[name='code']",
                run: "text TOUR-SUB-NEW",
            },
            {
                content: "Select the Construct",
                trigger: ".o_field_many2one[name='construct_id'] input",
                run: "text Tour Subconstruct Construct",
            },
            {
                content: "Pick the Construct from the dropdown",
                trigger:
                    ".ui-autocomplete .ui-menu-item a:contains(Tour Subconstruct Construct)",
                in_modal: false,
            },
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );

    // IK: docs/school_character_subconstruct/02-edit.md
    tour.register(
        "ssi_school_character_school_character_subconstruct_edit",
        {test: true, url: "/web"},
        [
            ...openMenuSteps(),
            {
                content: "Open the sub-construct to edit",
                trigger: ".o_data_row:contains(Tour Subconstruct Edit)",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Click Edit",
                trigger: ".o_form_button_edit",
            },
            {
                content: "Change the Definition",
                trigger: ".o_field_widget[name='definition']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Edited via tour.",
            },
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );

    // IK: docs/school_character_subconstruct/03-delete.md
    tour.register(
        "ssi_school_character_school_character_subconstruct_delete",
        {test: true, url: "/web"},
        [
            ...openMenuSteps(),
            {
                content: "Open the sub-construct to delete",
                trigger: ".o_data_row:contains(Tour Subconstruct Delete)",
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
                content: "Click the Character Sub-constructs breadcrumb to return to the list",
                trigger: ".breadcrumb-item.o_back_button a:contains(Character Sub-constructs)",
            },
            {
                content: "Back to the list",
                trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );

    // IK: docs/school_character_subconstruct/04-deactivate.md
    tour.register(
        "ssi_school_character_school_character_subconstruct_deactivate",
        {test: true, url: "/web"},
        [
            ...openMenuSteps(),
            {
                content: "Select the sub-construct to deactivate",
                trigger:
                    ".o_data_row:contains(Tour Subconstruct Deactivate) .o_list_record_selector input",
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
                trigger:
                    ".o_list_view:not(:has(.o_data_row:contains(Tour Subconstruct Deactivate)))",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );

    // IK: docs/school_character_subconstruct/05-activate.md
    tour.register(
        "ssi_school_character_school_character_subconstruct_activate",
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
                trigger: ".o_filter_menu .o_menu_item a:contains(Archived)[aria-checked='true']",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Select the sub-construct to reactivate",
                trigger:
                    ".o_data_row:contains(Tour Subconstruct Activate) .o_list_record_selector input",
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
                trigger: ".o_data_row:contains(Tour Subconstruct Activate)",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});

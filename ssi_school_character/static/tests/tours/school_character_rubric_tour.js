odoo.define("ssi_school_character.school_character_rubric_tour", function (require) {
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
                content: "Open the Character Rubrics menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_character.school_character_rubric_menu"]',
            },
            {
                content: "Character Rubrics list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Character Rubrics)",
                extra_trigger: ".o_list_view",
                run: function () {},
            },
        ];
    }

    // IK: docs/school_character_rubric/01-create.md
    tour.register(
        "ssi_school_character_school_character_rubric_create",
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
                run: function () {},
            },
            {
                content: "Fill in Name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour Rubric New",
            },
            {
                content: "Fill in Code",
                trigger: ".o_field_widget[name='code']",
                run: "text TOUR-RBC-NEW",
            },
            {
                content: "Open the Rubric tab",
                trigger: ".o_notebook .nav-link:contains(Rubric)",
            },
            {
                content: "Select the Construct",
                trigger: ".o_field_many2one[name='construct_id'] input",
                run: "text Tour Rubric Construct",
            },
            {
                content: "Pick the Construct from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(Tour Rubric Construct)",
                in_modal: false,
            },
            {
                content: "Select the Scale",
                trigger: ".o_field_many2one[name='scale_id'] input",
                run: "text Tour Rubric Scale",
            },
            {
                content: "Pick the Scale from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(Tour Rubric Scale)",
                in_modal: false,
            },
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {},
            },
        ]
    );

    // IK: docs/school_character_rubric/02-edit.md
    tour.register(
        "ssi_school_character_school_character_rubric_edit",
        {test: true, url: "/web"},
        [
            ...openMenuSteps(),
            {
                content: "Open the rubric to edit",
                trigger: ".o_data_row:contains(Tour Rubric Edit)",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Click Edit",
                trigger: ".o_form_button_edit",
            },
            {
                content: "Open the Descriptors tab",
                trigger: ".o_notebook .nav-link:contains(Descriptors)",
            },
            {
                content: "Add a descriptor line",
                trigger: ".o_field_x2many_list_row_add a",
            },
            {
                content: "Select the Level on the descriptor line",
                trigger:
                    ".o_field_widget[name='descriptor_ids'] .o_selected_row .o_field_many2one[name='level_id'] input",
                run: "text Tour Rubric Level",
            },
            {
                content: "Pick the Level on the descriptor line",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(Tour Rubric Level)",
                in_modal: false,
            },
            {
                content: "Fill in the Descriptor text",
                trigger:
                    ".o_field_widget[name='descriptor_ids'] .o_selected_row .o_field_widget[name='descriptor'] textarea",
                run: "text Edited descriptor via tour.",
            },
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {},
            },
        ]
    );

    // IK: docs/school_character_rubric/03-delete.md
    tour.register(
        "ssi_school_character_school_character_rubric_delete",
        {test: true, url: "/web"},
        [
            ...openMenuSteps(),
            {
                content: "Open the rubric to delete",
                trigger: ".o_data_row:contains(Tour Rubric Delete)",
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
                content: "Click the Character Rubrics breadcrumb to return to the list",
                trigger: ".breadcrumb-item.o_back_button a:contains(Character Rubrics)",
            },
            {
                content: "Back to the list",
                trigger: ".o_list_view",
                run: function () {},
            },
        ]
    );

    // IK: docs/school_character_rubric/04-deactivate.md
    tour.register(
        "ssi_school_character_school_character_rubric_deactivate",
        {test: true, url: "/web"},
        [
            ...openMenuSteps(),
            {
                content: "Select the rubric to deactivate",
                trigger:
                    ".o_data_row:contains(Tour Rubric Deactivate) .o_list_record_selector input",
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
                    ".o_list_view:not(:has(.o_data_row:contains(Tour Rubric Deactivate)))",
                run: function () {},
            },
        ]
    );

    // IK: docs/school_character_rubric/05-activate.md
    tour.register(
        "ssi_school_character_school_character_rubric_activate",
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
                run: function () {},
            },
            {
                content: "Select the rubric to reactivate",
                trigger:
                    ".o_data_row:contains(Tour Rubric Activate) .o_list_record_selector input",
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
                trigger: ".o_data_row:contains(Tour Rubric Activate)",
                run: function () {},
            },
        ]
    );
});

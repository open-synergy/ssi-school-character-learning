// Copyright 2026 OpenSynergy Indonesia
// Copyright 2026 PT. Simetri Sinergi Indonesia
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

odoo.define(
    "ssi_school_character_evidence_operating_unit.school_character_observation_tour",
    function (require) {
        "use strict";

        var tour = require("web_tour.tour");

        // IK: docs/school_character_observation/01-create.md (E1 delta --
        // Additional Fields). Navigation (open menu -> New) is taken from
        // the base IK ssi_school_character_evidence/docs/
        // school_character_observation/01-create.md Flow steps 1-2. The
        // delta assertion comes from this module's own IK: the Operating
        // Unit field is visible on the create form for a user in the
        // operating_unit.group_multi_operating_unit group. The tour stops
        // there; it does not fill, save, or confirm (E1 delta-only).
        tour.register(
            "ssi_school_character_evidence_operating_unit_observation_create",
            {
                test: true,
                url: "/web",
            },
            [
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
                    content: "Open the Measurement menu",
                    trigger:
                        '.o_menu_sections [data-menu-xmlid="ssi_school_character_evidence.menu_character_measurement_root"]',
                },
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
                        // Assertion only; do not trigger the default click.
                        return true;
                    },
                },
                {
                    content: "Click New",
                    trigger: ".o_list_button_add",
                    extra_trigger: ".o_list_view",
                },
                {
                    content: "Form is open in edit mode",
                    trigger: ".o_form_view.o_form_editable",
                    run: function () {
                        // Assertion only; do not trigger the default click.
                        return true;
                    },
                },
                {
                    content: "Operating Unit field is visible on the form",
                    trigger:
                        ".o_form_view.o_form_editable .o_field_widget[name='operating_unit_id']",
                    run: function () {
                        // Assertion only; do not trigger the default click.
                        return true;
                    },
                },
            ]
        );
    }
);

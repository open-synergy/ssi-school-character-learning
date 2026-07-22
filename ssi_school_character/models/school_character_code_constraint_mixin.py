# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, models
from odoo.exceptions import UserError


class SchoolCharacterCodeConstraintMixin(models.AbstractModel):
    """
    Abstract mixin that rejects the ``/`` placeholder, together with blank
    or whitespace-only values, as a valid ``code`` on the Character master
    data models (Family, Construct, Sub-construct, Indicator).

    ``mixin.master_data`` (``ssi-mixin``) intentionally accepts ``/`` as a
    valid placeholder ``code`` — it is relied upon across the whole SSI
    ecosystem (``action_reset_code``, ``action_generate_code``, the
    duplicate-code check), so the rule cannot be added there without
    affecting every other master data model. This mixin layers a stricter,
    local rule on top so every Character master data record keeps a
    meaningful, usable reference key, as requested by ICLAD feedback.

    Models that need this rule add ``school_character_code_constraint_mixin``
    to their ``_inherit`` list, in addition to ``mixin.master_data``.
    """

    _name = "school_character_code_constraint_mixin"
    _description = "Character Code Constraint Mixin"

    @api.constrains("code")
    def _check_character_code_not_placeholder(self):
        for record in self:
            code = (record.code or "").strip()
            if not code or code == "/":
                error_message = """
Document Type: %s
Context: Save Character master data
Database ID: %s
Problem: Code is empty or still the '/' placeholder
Solution: Fill in a meaningful, unique code for this record. The '/' \
placeholder is not allowed for Character master data
""" % (
                    record._description,
                    record.id,
                )
                raise UserError(_(error_message))

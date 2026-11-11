# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.osv import expression


class SchoolCharacterSubconstruct(
    models.Model
):  # pylint: disable=too-few-public-methods
    """
    Represents a Sub-construct, a finer-grained facet of a Character
    Construct, per the ICLAD v2.3 construct architecture (Bab 6). A
    sub-construct decomposes a construct into narrower, still-observable
    parts so that indicators can be defined against each of them.
    """

    _name = "school_character_subconstruct"
    _inherit = [
        "mixin.master_data",
        "school_character_code_constraint_mixin",
    ]
    _description = "Character Sub-construct"
    _show_code_on_display_name = True

    construct_id = fields.Many2one(
        string="Construct",
        comodel_name="school_character_construct",
        required=True,
        ondelete="cascade",
        help="Construct this sub-construct decomposes.",
    )
    definition = fields.Text(
        string="Definition",
        help="Precise definition of this sub-construct as a narrower facet "
        "of its parent construct.",
    )

    @api.model
    def _name_search(
        self, name, args=None, operator="ilike", limit=100, name_get_uid=None
    ):
        """Search records by code as well as by name.

        For the pattern operators the name is matched against either
        ``code`` or ``name``; any other operator falls back to the
        default behaviour.

        :param name: Text typed by the user.
        :param args: Extra domain to AND with the match.
        :param operator: Comparison operator for ``name``.
        :param limit: Maximum number of results.
        :param name_get_uid: User used for the access rights check.
        :return: List of matching record ids.
        :rtype: list[int]
        """
        if operator in ("ilike", "like", "=", "=like", "=ilike"):
            args = expression.AND(
                [
                    args or [],
                    ["|", ("code", operator, name), ("name", operator, name)],
                ]
            )
            return self._search(args, limit=limit, access_rights_uid=name_get_uid)
        return super()._name_search(
            name,
            args=args,
            operator=operator,
            limit=limit,
            name_get_uid=name_get_uid,
        )

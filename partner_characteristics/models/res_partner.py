from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    time_code = fields.Char(help="Specific code related to time or scheduling.")

    who_cuts = fields.Char(
        string="Cutter/Responsible",
        help=(
            "Indicates who is responsible for a specific "
            "cutting process or decision."
        ),
    )

    sector_code = fields.Char(
        help="Code identifying the business sector or industry of the contact."
    )

    subsector_code = fields.Char(
        help="Code identifying the specific subsector within the main sector."
    )

    fabric_unit = fields.Char(
        help="Identifier for the factory unit associated with the contact."
    )

    truck_unit = fields.Char(
        help=(
            "Identifier for the truck or transport unit " "associated with the contact."
        )
    )

    channel_code = fields.Char(
        help=(
            "Code indicating the sales or distribution "
            "channel used for this contact."
        )
    )

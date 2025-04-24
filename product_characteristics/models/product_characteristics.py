from odoo import models, fields, _

class ProductCharacteristics(models.Model):
    _inherit = 'product.template'

    collection = fields.Char(
        string=_("Collection"),
        help=_("Indicate the product's collection name (e.g., Summer 2024, Classic Line)")
    )

    weight_label = fields.Char(
        string=_("Weight Label"),
        help=_("Specify the label or code related to the product's weight categorization")
    )

    color_code = fields.Char(
        string=_("Color Code"),
        help=_("Enter the internal or external code for the product's color")
    )

    color = fields.Char(
        string=_("Color"),
        help=_("Provide a descriptive name for the product's color (e.g., Midnight Blue, Crimson Red)")
    )

    cost_kilo_to_weight_label = fields.Char(
        string=_("Cost Kilo to Weight Label"),
        help=_("Enter the cost per kilogram related to the weight label")
    )

    material_code = fields.Char(
        string=_("Material Code"),
        help=_("Enter the internal or external code for the product's primary material")
    )

    material = fields.Char(
        string=_("Material"),
        help=_("Provide a descriptive name for the product's primary material (e.g., Cotton, Steel, Plastic)")
    )

    manufacturing_type = fields.Char(
        string=_("Manufacturing Types"),
        help=_("Specify the type of manufacturing process used for this product")
    )

    comercial_measure = fields.Char(
        string=_("Comercial Measure"),
        help=_("Indicate the standard commercial unit or measure for this product")
    )

    opening_position = fields.Char(
        string=_("Opening Position"),
        help=_("Describe the position of any openings on the product")
    )

    opening_size = fields.Char(
        string=_("Opening Size"),
        help=_("Specify the size of any openings on the product")
    )

    raw_size = fields.Char(
        string=_("Raw Size"),
        help=_("Indicate the dimensions or size of the product in its raw or unprocessed state")
    )

    grinding = fields.Char(
        string=_("Grinding"),
        help=_("Provide details about any grinding applied to the product")
    )

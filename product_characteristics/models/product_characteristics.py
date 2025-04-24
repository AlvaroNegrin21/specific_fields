from odoo import models, fields

class ProductCharacteristics(models.Model):
    _inherit = 'product.template'

    collection = fields.Char(
        string="Collection",
        help="Indicate the product's collection name (e.g., Summer 2024, Classic Line)"
    )

    weight_label = fields.Char(
        string="Weight Label",
        help="Specify the label or code related to the product's weight categorization"
    )

    color_code = fields.Char(
        string="Color Code",
        help="Enter the internal or external code for the product's color"
    )

    color = fields.Char(
        string="Color",
        help="Provide a descriptive name for the product's color (e.g., Midnight Blue, Crimson Red)"
    )

    cost_kilo_to_weight_label = fields.Char(
        string="Cost Kilo to Weight Label",
        help="Enter the cost per kilogram related to the weight label"
    )

    material_code = fields.Char(
        string="Material Code",
        help="Enter the internal or external code for the product's primary material"
    )

    material = fields.Char(
        string="Material",
        help="Provide a descriptive name for the product's primary material (e.g., Cotton, Steel, Plastic)"
    )

    manufacturing_type = fields.Char(
        string="Manufacturing Types",
        help="Specify the type of manufacturing process used for this product"
    )

    comercial_measure = fields.Char(
        string="Comercial Measure",
        help="Indicate the standard commercial unit or measure for this product"
    )

    opening_position = fields.Char(
        string="Opening Position",
        help="Describe the position of any openings on the product"
    )

    opening_size = fields.Char(
        string="Opening Size",
        help="Specify the size of any openings on the product"
    )

    raw_size = fields.Char(
        string="Raw Size",
        help="Indicate the dimensions or size of the product in its raw or unprocessed state"
    )

    grinding = fields.Char(
        string="Grinding",
        help="Provide details about any grinding applied to the product"
    )

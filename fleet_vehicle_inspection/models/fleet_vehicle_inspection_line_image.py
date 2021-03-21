# Copyright 2021 - TODAY, Marcel Savegnago <marcel.savegnago@escodoo.com.br>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError

from .tools import get_video_embed_code


class FleetVehicleInspectionLineImage(models.Model):

    _name = "fleet.vehicle.inspection.line.image"
    _description = "Fleet Vehicle Inspection Line Image"
    _inherit = ["image.mixin"]
    _order = "sequence, id"

    name = fields.Char()
    sequence = fields.Integer(default=10, index=True)
    image_1920 = fields.Image(required=True)
    inspection_line_id = fields.Many2one(
        "fleet.vehicle.inspection.line", "Related Inspection Line", copy=True
    )

    video_url = fields.Char(
        "Video URL", help="URL of a video for showcasing your product."
    )
    embed_code = fields.Char(compute="_compute_embed_code")

    can_image_1024_be_zoomed = fields.Boolean(
        "Can Image 1024 be zoomed",
        compute="_compute_can_image_1024_be_zoomed",
        store=True,
    )

    @api.depends("image_1920", "image_1024")
    def _compute_can_image_1024_be_zoomed(self):
        for image in self:
            image.can_image_1024_be_zoomed = (
                image.image_1920
                and tools.is_image_size_above(image.image_1920, image.image_1024)
            )

    @api.depends("video_url")
    def _compute_embed_code(self):
        for image in self:
            image.embed_code = get_video_embed_code(image.video_url)

    @api.constrains("video_url")
    def _check_valid_video_url(self):
        for image in self:
            if image.video_url and not image.embed_code:
                raise ValidationError(
                    _(
                        "Provided video URL for '%s' is not valid."
                        "Please enter a valid video URL.",
                        image.name,
                    )
                )

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import qrcode
import qrcode.image.svg
import svgwrite

method = 'test'

if method == 'basic':
    # Simple factory, just a set of rects.
    factory = qrcode.image.svg.SvgImage
elif method == 'fragment':
    # Fragment factory (also just a set of rects)
    factory = qrcode.image.svg.SvgFragmentImage
else:
    # Combined path factory, fixes white space that may occur when zooming
    factory = qrcode.image.svg.SvgPathImage

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    image_factory=factory,
    box_size=10,
    border=4,
)

qr.add_data('dfasdfasdf')
qr.make(fit=True)
img = qr.make_image()
dwg = svgwrite.Drawing(filename='test.svg')
dwg.


dwg.save()
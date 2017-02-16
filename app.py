from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=4,
)

qr.add_data('ASDFASDFASDFASDFtest')
qr.make(fit=True)

fnt = ImageFont.truetype("FreeMono.ttf", 16)
base = qr.make_image()

txt = Image.new('RGB', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, half opacity
d.text((10,10), "Hello", font=fnt, fill=(255,255,255,128))
# draw text, full opacity
d.text((10,60), "World", font=fnt, fill=(255,255,255,255))

out = Image.composite(base, txt, 1)

out.show()
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageChops
import curses
import qrcode


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()


method = 'test'
i = 1
l = 10
fontSize = 40
font = ImageFont.truetype("arial.ttf", fontSize)
printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
for x in range(0, l):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
    )

    i += 1
    printProgressBar(i, l, prefix='Progress:', suffix='Complete', length=50)
    newFile = '{:04d}'.format(x)+'.png'
    qr.add_data('CasterCos'+'{:04d}'.format(x))
    qr.make(fit=True)
    qrImg = qr.make_image().get_image()
    newImg = Image.new('RGB',(qrImg.width,qrImg.width*2),(255, 255, 255))
    newImg.paste(qrImg, (0, 10, qrImg.width, 10+qrImg.width))

    canvas = ImageDraw.Draw(newImg)
    padd = 5
    canvas.rectangle([padd,padd,newImg.width-padd,newImg.height-padd],outline=(0,0,0))
    canvas.text((5, qrImg.width+(fontSize)), newFile, (0, 0, 0), font=font)
    canvas.text((5, qrImg.width+(fontSize*2)), "Sample Text 1", (0, 0, 0), font=font)
    canvas.text((5, qrImg.width+(fontSize*3)), "Sample Text 2", (0, 0, 0), font=font)

    newImg.save(newFile)

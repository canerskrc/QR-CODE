import pyqrcode
import png
from pyqrcode import QRCode
cacainsta = "https://www.instagram.com/caner.sekerci/"
url = pyqrcode.create(cacainsta)
url.svg("caca.svg", scale = 8)
url.png("caca.png", scale = 6)




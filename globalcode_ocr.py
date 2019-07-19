try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
def glbcd(filename):
    mytext = pytesseract.image_to_string(filename)
    return mytext


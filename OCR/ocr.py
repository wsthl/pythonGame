import pytesseract
try:
    import Image
except ImportError:
    from PIL import Image

print pytesseract.image_to_string(Image.open('test.png'),lang='chi_sim')

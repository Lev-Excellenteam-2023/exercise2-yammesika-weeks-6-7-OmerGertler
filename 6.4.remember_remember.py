# Author: Omer Gertler

from PIL import Image

DIR = r"C:\Users\omer\Desktop\Notebooks-master\Notebooks-master\week06\resources\code.png"


def decipher_msg_from_pic(image_dir):
    """
    find all black pixels (numeric value == 1) in the image.
    searching column by column left to right, each column top down.
    for every black pixel, it's line-number translated to ascii value.
    the result is a string message of those decipher line numbers.
    :param image_dir: the directory where the image stores
    :return: string of decipher line numbers of the black pixels
    """
    black_pixels = []
    with Image.open(image_dir) as img:
        width, height = img.size
        for x in range(width):
            for y in range(height):
                pix_color = img.getpixel((x, y))
                if pix_color == 1:  # if the pixel is black
                    black_pixels.append(y)
    return ''.join([chr(pixel) for pixel in black_pixels])


res = decipher_msg_from_pic(DIR)
print(res)


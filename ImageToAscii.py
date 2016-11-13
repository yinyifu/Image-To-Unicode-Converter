#!usr/bin/python
# -*- coding : utf-8 -*-
from PIL import Image, ImageEnhance
import codecs
ASCII_CHARS = [chr(9608),chr(9619), chr(9618),chr(9617)]

twitch = 34
youtube = 56
image_glo = '';
def scale_image(image, new_width=100):
    #print new_width

    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)*0.6
    new_height = int( aspect_ratio*new_width )

    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    image.save('temp2.png', 'png')
    i=image.convert('LA')
    i.save('temp.png', 'png')
    return i
def get_enhance_image():
    global image_glo
    return image_glo
def enhance_image(image, contV, brightV, colorV, sharpV):
    contrast = ImageEnhance.Contrast(image)
    image = contrast.enhance(contV)
    brightness = ImageEnhance.Brightness(image)
    image = brightness.enhance(brightV)
    color =ImageEnhance.Color(image)
    image = color.enhance(colorV)
    sharp = ImageEnhance.Sharpness(image)
    global image_glo
    image_glo = sharp.enhance(sharpV)
    return image
    pass


def map_pixels_to_ascii_chars(image, range_width=255/(len(ASCII_CHARS)-1)):
    """Maps each pixel to an ascii char based on the range
    in which it lies.

    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_in_image = list(image.getdata())
    #print pixels_in_image
    pixels_to_chars = []
    for pixel_value in pixels_in_image:
        if pixel_value[1]==0:
            pixels_to_chars.append(ASCII_CHARS[int(255/range_width)])
        else:
            pixels_to_chars.append(ASCII_CHARS[int(pixel_value[0]/range_width)])

    # u = ""
    # u = [u+unichr(2588) for i in xrange(0, 38)]
    # #print u
    # pixels_to_chars[0] = "".join(u)
    return "".join(pixels_to_chars)

def convert_image_to_ascii(image, new_width=100, cov=1, bv=1, cv=1, sv=1):
    image = enhance_image(image, cov, bv, cv, sv)
    image = scale_image(image, int(new_width))
    image =  convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in
            range(0, len_pixels_to_chars, new_width)]
    #u = ""
    #u = [u+unichr(8192) for i in xrange(0, 38)]
    #print u
    #image_ascii[0] = "".join(u)
    return '\n'.join(image_ascii)

def handle_image_conversion(image_filepath, new_width, cov, bv, cv, sv):
    print(image_filepath)
    if new_width == "twitch":
        new_width = twitch
    elif new_width == "youtube":
        new_width = youtube
    else:
    	new_width = int(new_width)
    image = None
    try:
        #print ("\n\n\n\n\n\n\n\n\n" + image_filepath)
        image = Image.open(image_filepath)

    except:
        #print ("Unable to open image file {image_filepath}.".format(image_filepath=image_filepath))
        #print (image_filepath)
        return

    image_ascii = convert_image_to_ascii(image, new_width, cov, bv, cv, sv)
    file1 = codecs.open("temp.txt", 'w', "utf-8")
    #image_ascii = image_ascii.decode("")
    file1.write(image_ascii)
    
    #print image_ascii
    file1.close()

if __name__=='__main__':
    import sys
 	
    image_file_path = sys.argv[1]
    #image_width = sys.argv[2]
    new_width = sys.argv[2]
    
    cov = float(sys.argv[3])
    bv = float(sys.argv[4])
    cv = float(sys.argv[5])
    sv = float(sys.argv[6])
    handle_image_conversion(image_file_path, new_width, cov,bv,cv,sv)

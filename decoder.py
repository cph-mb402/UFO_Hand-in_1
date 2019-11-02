from PIL import Image

def decode_image(file_location="encoded_image.png"):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]
 
    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]
 
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    
    bits = ""

    class Found(Exception): pass
    try:
        for i in range(x_size):
            for j in range(y_size):
                pixel_value = red_channel.getpixel((j, i))
                pixel_bit = bin(pixel_value)[-1]
                # print(pixel_bit)
                bits += pixel_bit
                if pixel_value == 0:
                    raise Found
    except Found:
        i = 0
        decoded_string = ""
        the_bytes = ''
        while i<= len(bits):
            byte = bits[i:i+8]
            print(byte)
            i += 9
            the_bytes += byte
            # print(int(byte, 2))
            string_byte = chr(int(byte, 2))
            decoded_string += string_byte

        # print(the_bytes)
        print(decoded_string)
        # print(len(bits))
        # print(chr(int(bits, 2)))

        decoded_string =""

decode_image()

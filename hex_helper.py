import colorsys as csys

minimum_rgb = 0
maximum_rgb = 255

def hls_to_hex(hue,lightness,saturation):
    """
    Convert a colour from HLS to a hex string.

    All three inputs use a 0 to 1 scale. Note the order is hue, lightness, saturation
    instead of hue, saturation, lightness.
    :param hue: Position on the colour wheel.
    :param lightness: Brightness from black to white.
    :param saturation: Colour intensity from grey to vivid.
    :return: The colour as a "#RRGGBB" string.
    """
    #colorsys conversion
    red, green, blue = csys.hls_to_rgb(hue, lightness, saturation)

    #scale rgb values
    red_adjust = red * maximum_rgb
    green_adjust = green * maximum_rgb
    blue_adjust = blue * maximum_rgb

    #hex code formatting
    red_hex = f"{round(red_adjust):02X}"
    green_hex = f"{round(green_adjust):02X}"
    blue_hex = f"{round(blue_adjust):02X}"

    original_hex = f"#{red_hex}{green_hex}{blue_hex}"

    return original_hex

if __name__ == "__main__":
    print(hls_to_hex(0,0.5,1.0))
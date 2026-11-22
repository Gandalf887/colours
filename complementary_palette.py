import colorsys as csys
import random as rnd

#constants
minimum_rgb = 0
maximum_rgb = 255
rotation_factor = 0.5
rotation_degree = 1

def original_complementary():
    """
    Pick a random RGB colour and return it with its complementary colour.

    The complement is found by converting to HLS, rotating the hue half
    a turn around the colour wheel and converting back. Lightness and
    Saturation are constant.

    :return: A tuple of two "#RRGGBB" strings: (original, complementary).
    """

    #randomise the rgb values.
    red_raw = rnd.randint(minimum_rgb, maximum_rgb)
    green_raw = rnd.randint(minimum_rgb, maximum_rgb)
    blue_raw = rnd.randint(minimum_rgb, maximum_rgb)

    #adjustment pre calculation.
    red_adjust = red_raw / maximum_rgb
    green_adjust = green_raw / maximum_rgb
    blue_adjust = blue_raw / maximum_rgb

    hue, lightness, saturation = csys.rgb_to_hls(red_adjust, green_adjust, blue_adjust)

    #rotate the colour wheel
    comp_hue = (hue + rotation_factor) % rotation_degree

    comp_red, comp_green, comp_blue = csys.hls_to_rgb(comp_hue, lightness, saturation)

    #get hex codes.
    comp_red_hex = f"{round(comp_red * maximum_rgb):02X}"
    comp_green_hex = f"{round(comp_green * maximum_rgb):02X}"
    comp_blue_hex = f"{round(comp_blue * maximum_rgb):02X}"

    #get result
    red_hex = f"{round(red_raw):02X}"
    green_hex = f"{round(green_raw):02X}"
    blue_hex = f"{round(blue_raw):02X}"

    #combine hex codes.
    original_hex = f"#{red_hex}{green_hex}{blue_hex}"
    complementary_hex = f"#{comp_red_hex}{comp_green_hex}{comp_blue_hex}"

    return original_hex, complementary_hex

if __name__ == "__main__":
    original_complementary()
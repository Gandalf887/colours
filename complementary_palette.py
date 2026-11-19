import colorsys as csys
import random as rnd

minimum_rgb = 0
maximum_rgb = 255
rotation_factor = 0.5
rotation_degree = 1

def original_complementary():

    red_raw = rnd.randint(minimum_rgb, maximum_rgb)
    green_raw = rnd.randint(minimum_rgb, maximum_rgb)
    blue_raw = rnd.randint(minimum_rgb, maximum_rgb)

    red_adjust = red_raw / maximum_rgb
    green_adjust = green_raw / maximum_rgb
    blue_adjust = blue_raw / maximum_rgb

    hue, lightness, saturation = csys.rgb_to_hls(red_adjust, green_adjust, blue_adjust)

    comp_hue = (hue + rotation_factor) % rotation_degree

    comp_red, comp_green, comp_blue = csys.hls_to_rgb(comp_hue, lightness, saturation)

    comp_red_hex = f"{round(comp_red * maximum_rgb):02X}"
    comp_green_hex = f"{round(comp_green * maximum_rgb):02X}"
    comp_blue_hex = f"{round(comp_blue * maximum_rgb):02X}"

    red_hex = f"{round(red_raw):02X}"
    green_hex = f"{round(green_raw):02X}"
    blue_hex = f"{round(blue_raw):02X}"

    original_hex = f"#{red_hex}{green_hex}{blue_hex}"
    complementary_hex = f"#{comp_red_hex}{comp_green_hex}{comp_blue_hex}"

    return original_hex, complementary_hex

if __name__ == "__main__":
    original_complementary()
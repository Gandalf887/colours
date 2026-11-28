import random as rnd
from hex_helper import hls_to_hex

#constants
base_hue_bottom = 0.00
base_hue_top = 1.00
hue_variance = 0.04
rotation_range = 1

lightness_variance = 0.05
lightness_steps = [0.2, 0.4, 0.6, 0.8]

saturation_constant = 0.7
accent_lightness = 0.75
rotation_factor = 0.5

colour_count = 5

def analogous():
    """
    Generate a five colour palette: a dark to light ramp plus accent.

    Four colours share a tight hue band off a randomised base hue,
    the fifth is an accent on the opposite side of the colour wheel.

    :return: A list of five "#RRGGBB" strings: four ramp colours and the accent.
    """
    # hues:
    base_hue = rnd.uniform(base_hue_bottom, base_hue_top)

    hue_offset = []
    for _ in range(0, 4):
        hue_offset.append(rnd.uniform(-hue_variance, hue_variance))

    adjusted_hues = []
    for hue_offsets in hue_offset:
        adjusted_hues.append((base_hue + hue_offsets) % rotation_range)

    # lightness:
    adjusted_lightness = []
    for step in lightness_steps:
        nudge = rnd.uniform(-lightness_variance, lightness_variance)
        adjusted_lightness.append(min(1, max(0, nudge + step)))

    results = []
    for hue, lightness in zip(adjusted_hues, adjusted_lightness):
        results.append(hls_to_hex(hue, lightness, saturation_constant))

    #complementary
    comp_hue = (base_hue + rotation_factor) % rotation_range
    comp_hex = hls_to_hex(comp_hue, accent_lightness, saturation_constant)

    results.append(comp_hex)

    return results

def spread_values():
    """
    Generate hues spread evenly round the colour wheel.

    A random base hue is picked, then colour_count hues are placed at equal spacing around
    the colour wheel.

    :return: A list of colour_count hues from 0 to 1.
    """
    positions = []

    base_hue = rnd.uniform(base_hue_bottom, base_hue_top)

    for i in range(colour_count):
        positions.append((i/colour_count + base_hue) % rotation_range)

    return positions

if __name__ == "__main__":
    print(analogous())
    print(spread_values())
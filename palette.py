import random as rnd

base_hue_bottom = 0.00
base_hue_top = 1.00
hue_variance = 0.04
rotation_range = 1

lightness_variance = 0.05
lightness_steps = [0.2, 0.4, 0.6, 0.8]


def analogous():
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

    return adjusted_hues, adjusted_lightness

if __name__ == "__main__":
    print(analogous())
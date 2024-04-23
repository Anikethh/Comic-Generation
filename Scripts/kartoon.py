import json
import sys
import os

from generate_panels import generate_panels
from stability_ai import text_to_image
from add_text import add_text_to_panel
from create_strip import create_strip
from utils import find_next_available_file, find_next_available_directory

SCENARIO = """
Characters: Peter is a tall guy with blond hair. Steven is a small guy with black hair.
Peter and Steven walk together in new york when aliens attack the city. They are afraid and try to run for their lives. The army arrive and save them.
"""

STYLE = "indian comic, colored"

# ==========================================================================================

# print(f"Generate panels with style '{STYLE}' for this scenario: \n {SCENARIO}")

directory = "../Generations"
base_filename = "generation"

# with open('output/panels.json') as json_file:
#   panels = json.load(json_file)

def main(scenario):
    STYLE = "american comic, colored"
    panels = generate_panels(scenario)[1:]
    panel_images = []

    for panel in panels:
        print(panel)

    next_file_path = find_next_available_file(directory, base_filename)

    with open(next_file_path, 'w') as outfile:
        json.dump(panels, outfile)

    print(f"Panels were written to {next_file_path}")

    img_directory = "../output"
    img_base_dirname = "generation"
    
    next_img_directory = find_next_available_directory(img_directory, img_base_dirname)
    
    for panel in panels:
        panel_prompt = panel["description"] + ", cartoon box, " + STYLE
        print(f"Generate panel {panel['number']} with prompt: {panel_prompt}")
        panel_image = text_to_image(panel_prompt)
        panel_image_with_text = add_text_to_panel(panel["text"], panel_image)
        save_path = os.path.join(next_img_directory, f"panel-{panel['number']}.png")
        panel_image_with_text.save(save_path)
        panel_images.append(panel_image_with_text)

    strip_path = os.path.join(next_img_directory, "strip.png")
    create_strip(panel_images).save(strip_path)
    print(f"Comic strip saved to {strip_path}")

if __name__ == "__main__":
    scenario = sys.argv[1] if len(sys.argv) > 1 else SCENARIO
    main(scenario)
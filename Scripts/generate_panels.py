import re
import base64
import json
import google.generativeai as genai

API_KEY = "AIzaSyDkJH1j5OgrsRxxRxIyrdrSmn_hzwnt2X0"
genai.configure(api_key=API_KEY)

model = "gemini-pro"

def generate_panels(scenario):
    contents = [{"role": "user", "parts": [{"text": scenario}]}]

    contents_b64 = "W3sicm9sZSI6InVzZXIiLCAicGFydHMiIDogW3sidGV4dCI6ICJoZWxsbyJ9XX0sIHsicm9sZSI6ICJtb2RlbCIsICJwYXJ0cyI6IFt7InRleHQiOiAiSGVsbG8hIEhvdyBjYW4gSSBhc3Npc3QgeW91IHRvZGF5PyJ9XX1d" # @param {isTemplate: true}
    generation_config_b64 = "e30=" # @param {isTemplate: true}
    safety_settings_b64 = "e30=" # @param {isTemplate: true}
    user_input_b64 = 'SG93IGRvZXMgZWxlY3RyaWNpdHkgd29yaz8=' #@param {isTemplate: true}

    contents = json.loads(base64.b64decode(contents_b64))
    generation_config = json.loads(base64.b64decode(generation_config_b64))
    safety_settings = json.loads(base64.b64decode(safety_settings_b64))
    stream=False

    gemini = genai.GenerativeModel(model_name=model)
    chat = gemini.start_chat(history=contents)

    template = """
You are a cartoon creator.

You will be given a short scenario, you must split it in 6 parts.
Each part will be a different cartoon panel.
For each cartoon panel, you will write a description of it with:
 - the characters in the panel, they must be described precisely each time
 - the background of the panel
The description should be only word or group of word delimited by a comma, no sentence.
Always use the characters descriptions instead of their name in the cartoon panel description.
You can not use the same description twice.
You will also write the text of the panel.
The text should not be more than 2 small sentences.
Each sentence should start by the character name

Example input:
Characters: Adrien is a guy with blond hair wearing glasses. Vincent is a guy with black hair wearing a hat.
Adrien and vincent want to start a new product, and they create it in one night before presenting it to the board.

Example output:

# Panel 1
description: 2 guys, a blond hair guy wearing glasses, a dark hair guy wearing hat, sitting at the office, with computers
text:
Vincent: I think Generative AI are the future of the company.
Adrien: Let's create a new product with it.

# end

Short Scenario:
{scenario}

Split the scenario in 6 parts. Do it EXACTLY in the same format as the example above, with # Panel, description:, text:, characters name and their dialogues:
"""

    response = chat.send_message(
        template,
        stream=stream)
    
    return extract_panel_info(response.text)

def extract_panel_info(text):
    panel_info_list = []
    panel_blocks = text.split('# Panel')

    for block in panel_blocks:
        if block.strip() != '':
            panel_info = {}
            
            # Extracting panel number
            panel_number = re.search(r'\d+', block)
            if panel_number is not None:
                panel_info['number'] = panel_number.group()
            
            # Extracting panel description
            panel_description = re.search(r'description: (.+)', block)
            if panel_description is not None:
                panel_info['description'] = panel_description.group(1)
            
            # Extracting panel text
            panel_text = re.search(r'text:\s*\n*(.+)', block, re.DOTALL)
            # print(panel_text.group(1))
            if panel_text is not None:
                panel_info['text'] = panel_text.group(1)
            
            panel_info_list.append(panel_info)
    return panel_info_list


# scenario = "Characters: Adrien is a guy with blond hair wearing glasses. Vincent is a guy with black hair wearing a hat. Adrien and Vincent decide to explore a mysterious island where they discover hidden treasures and face various challenges."
# panels = generate_panels(scenario)
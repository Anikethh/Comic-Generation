import re
import base64
import json
import google.generativeai as genai

API_KEY = "AIzaSyDkJH1j5OgrsRxxRxIyrdrSmn_hzwnt2X0"
genai.configure(api_key=API_KEY)

# model = "gemini-pro"

def generate_panels(scenario):
    model = genai.GenerativeModel('gemini-pro')

    template = f"""
You are a cartoon creator.

You are given a short scenario, you must split it in 6 parts.
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

Example scenario:
Adrien is a guy with blond hair wearing glasses. Vincent is a guy with black hair wearing a hat.
Adrien and vincent want to start a new product, and they create it in one night before presenting it to the board.

Example output:

# Panel 1
description: A guy with blond hair and a guy with black hair sitting in a casual setting with a laptop between them.
text:
Vincent: I think we need a new product.
Adrien: Let's brainstorm some ideas.

# Panel 2
description: The two guys, one with black hair and the other with blond, vigorously discussing and jotting down ideas on a whiteboard.
text:
Adrien: How about something related to AI?
Vincent: That sounds promising.

# Panel 3
description: The duo, one with black hair, the other blond, looking at the laptop screen, their faces illuminated with excitement.
text:
Vincent: Let's do this!
Adrien: We need to work overnight.

# Panel 4
description: The guys, one with blond hair, the other with black, working on the laptop, surrounded by empty coffee cups and pizza boxes.
text:
Adrien: This is tough, but we can do it.
Vincent: Absolutely, no backing out now.

# Panel 5
description: The sun is rising, the guy with blond hair and the guy with black hair looking exhausted but satisfied, staring at the finished product on the laptop screen.
text:
Vincent: We...we did it!
Adrien: Just in time for the board meeting.

# Panel 6
description: The guys presenting their product to a boardroom full of people. The blond-haired guy is talking, the black-haired guy operating the laptop.
text:
Adrien: Ladies and gentlemen, we present our new product.
Vincent: Hope you find it as exciting as we do.

NOTE: THE EXAMPLE IS ONLY TO HELP YOU LEARN THE PATTERN/FORMAT OF THE OUTPUT. DO NOT COPY THE EXAMPLE.

Scenario:
{scenario}

According to this scenario, split this into 6 parts, follow exactly the scenario described above. NOTHING ELSE.

Split the scenario in 6 parts. Do it in the same format as # Panel, description:, text:, characters name and their dialogues:
"""

    # response = chat.send_message(
    #     template,
    #     stream=False)

    response = model.generate_content(
    template,
    generation_config=genai.types.GenerationConfig(
        candidate_count=1,
        temperature=0.5)
)
    
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
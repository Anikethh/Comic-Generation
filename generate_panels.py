
import re

# from langchain.chat_models import ChatOpenAI
# from langchain.prompts.chat import (
#     ChatPromptTemplate,
#     HumanMessagePromptTemplate,
# )

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
```
Vincent: I think Generative AI are the future of the company.
Adrien: Let's create a new product with it.
```
# end

Short Scenario:
{scenario}

Split the scenario in 6 parts:
"
"""

def generate_panels(scenario):
    # model = ChatOpenAI(model_name='gpt-4')

    # human_message_prompt = HumanMessagePromptTemplate.from_template(template)

    # chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt])

    # chat_prompt.format_messages(scenario=scenario)

    # result = model(chat_prompt.format_messages(scenario=scenario))

    # print(result.content)

    result = """# Panel 1
description: 2 guys, tall blond guy, small guy with black hair, walking in New York City, skyscrapers in the background
text: 
Peter: Wow, what a beautiful day in the city!
Steven: Yeah, perfect for a stroll.

# Panel 2
description: 2 guys, expressions of shock, tall blond guy, small guy with black hair, aliens descending from the sky, chaos in the streets
text: 
Peter: What in the world is that?
Steven: Aliens! We need to get out of here!

# Panel 3
description: 2 guys, running in panic, tall blond guy, small guy with black hair, crowded streets, people screaming
text: 
Peter: Run, Steven, run!
Steven: I'm right behind you, Peter!

# Panel 4
description: 2 guys, soldiers in combat gear, tall blond guy, small guy with black hair, army vehicles, smoke rising from the streets
text: 
Soldier: Are you two okay? Come with us, we'll get you to safety.
Peter: Thank goodness you're here!

# Panel 5
description: 2 guys, relieved expressions, tall blond guy, small guy with black hair, standing next to soldiers, wreckage of alien attack in the background
text: 
Steven: I can't believe we made it out alive.
Peter: Me neither. Thanks for saving us, soldiers.

# Panel 6
description: 2 guys, tall blond guy, small guy with black hair, standing in a group of people, cheering for the army, New York City skyline in the background
text: 
Peter: Let's hear it for the heroes who saved our city!
Steven: Hooray for the army!
 """

    return extract_panel_info(result)

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
            panel_text = re.search(r'text: (.+)', block, re.DOTALL)
            # print(panel_text.group(1))
            if panel_text is not None:
                panel_info['text'] = panel_text.group(1)
            
            panel_info_list.append(panel_info)
    return panel_info_list

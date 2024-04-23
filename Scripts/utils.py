import os

def find_next_available_file(directory, base_filename):
    """Finds the next available filename in the form 'panels_i.txt' that does not yet exist."""
    i = 1
    while True:
        filename = f"{base_filename}_{i}.json"
        file_path = os.path.join(directory, filename)
        if not os.path.exists(file_path):
            return file_path
        i += 1

# def find_next_available_directory(directory):
#     """Finds the next available directory in the form 'output_i' that does not yet exist."""
#     i = 1
#     while True:
#         next_directory = f"{directory}_{i}"
#         if not os.path.exists(next_directory):
#             return next_directory
#         i += 1

def find_next_available_directory(base_directory, base_filename):
    i = 1
    while True:
        directory_path = os.path.join(base_directory, f"{base_filename}_{i}")
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)  # Ensure directory is created before use
            return directory_path
        i += 1

def write_panels_to_file(panels, file_path):
    with open(file_path, 'w') as f:
        for panel in panels:
            # Check if panel data is complete and write accordingly
            if 'number' in panel:
                f.write(f"# Panel {panel['number']}\n")
            else:
                print("Warning: Panel number is missing. Defaulting to 'Unknown'.")

            if 'description' in panel:
                f.write(f"description: {panel['description']}\n")
            else:
                print("Warning: Description is missing. Defaulting to 'Unknown'.")

            if 'text' in panel:
                f.write(f"text:\n{panel['text']}\n")
            else:
                print("Warning: Text is missing. Defaulting to 'Unknown'.")
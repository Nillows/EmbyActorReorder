import os
import xml.etree.ElementTree as ET
import inquirer

def find_nfo_files(directory, media_type):
    """Searches for .nfo files in the specified directory and its subdirectories based on media type."""
    nfo_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if (media_type == 'TV Shows' and file == 'tvshow.nfo') or (media_type == 'Movies' and file.endswith('.nfo')):
                nfo_files.append(os.path.join(root, file))
    return nfo_files

def reorder_actors(file_path):
    """Loads the .nfo file, displays current actors, allows partial or full user reordering, sets lockdata to true, and saves the changes."""
    tree = ET.parse(file_path)
    root = tree.getroot()
    actors = root.findall('.//actor')
    lockdata = root.find('.//lockdata')
    
    while True:  # Loop to allow reordering until confirmation is given
        print()  # Add an empty line for spacing
        actor_info = [(actor.find('name').text, actor.find('role').text) for actor in actors if actor.find('name') is not None and actor.find('role') is not None]
        print(f"Current order of actors in {file_path}:")
        for index, (name, role) in enumerate(actor_info, 1):
            print(f"{index}: {name} as {role}")

        print()  # Add an empty line for spacing
        order_input = input("Enter the preferred order of actors using numbers separated by spaces (e.g., '5 6 4 8 2' or just '5 6 4' to partially re-order), or press Enter to skip this file: ")
        if not order_input.strip():  # Check if input is empty to skip
            print("Skipping file, no changes made.")
            break

        order_indices = [int(idx) - 1 for idx in order_input.split()]  # Split input by spaces and convert to integers
        new_actors_order = [actors[idx] for idx in order_indices]
        remaining_actors = [actor for idx, actor in enumerate(actors) if idx not in order_indices]
        final_actors_order = new_actors_order + remaining_actors

        print()  # Add an empty line for spacing
        new_actor_info = [(actor.find('name').text, actor.find('role').text) for actor in final_actors_order]
        print("New order of actors:")
        for index, (name, role) in enumerate(new_actor_info, 1):
            print(f"{index}: {name} as {role}")

        print()  # Add an empty line before the confirm question
        questions = [inquirer.Confirm('confirm', message="Is this order correct?", default=True)]
        answers = inquirer.prompt(questions)

        if answers.get('confirm'):
            if lockdata is not None:
                lockdata.text = 'true'
            else:
                ET.SubElement(root, 'lockdata').text = 'true'
            
            for actor in actors:
                root.remove(actor)
            for actor in final_actors_order:
                root.append(actor)

            tree.write(file_path)
            print(f"Updated order of actors and set lockdata to true in {file_path}")
            break
        else:
            print("Reordering canceled. Let's try again.")
            print()  # Add an empty line after cancellation message

def main():
    """Main function to run the UI and handle file processing."""
    print("Running the script...")
    print()  # Add an empty line for spacing
    directory = input("What directory do you want to search? (e.g., C:\\Users\\thomw\\Desktop\\movies): ").strip()
    print(f"Searching in directory: {directory}")
    print()  # Add an empty line for spacing

    media_type_question = [
        inquirer.Checkbox('media_type',
                          message="Using your arrow keys and space bar, select the media type the directory contains and press enter (must select at least one):",
                          choices=['TV Shows', 'Movies'],
                          default=[])
    ]
    media_type_answers = inquirer.prompt(media_type_question)
    media_type = media_type_answers['media_type']

    while not media_type:
        print("No media type was selected. Please select at least one media type.")
        media_type_answers = inquirer.prompt(media_type_question)
        media_type = media_type_answers['media_type']

    nfo_files = find_nfo_files(directory, media_type[0])  # Process the first selected media type
    if nfo_files:
        for file_path in nfo_files:
            print(f"Processing file: {file_path}")
            reorder_actors(file_path)
        print("All files processed.")
    else:
        print(f"No '.nfo' files found for {media_type[0]} in the directory.")

if __name__ == '__main__':
    main()

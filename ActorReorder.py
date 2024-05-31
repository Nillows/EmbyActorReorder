import os
import xml.etree.ElementTree as ET
import inquirer

def find_nfo_files(directory):
    """Searches for all 'tvshow.nfo' files in the specified directory and its subdirectories."""
    nfo_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == 'tvshow.nfo':
                nfo_files.append(os.path.join(root, file))
    return nfo_files

def reorder_actors(file_path):
    """Loads the .nfo file, displays current actors, allows partial or full user reordering, sets lockdata to true, and saves the changes."""
    tree = ET.parse(file_path)
    root = tree.getroot()
    actors = root.findall('.//actor')
    lockdata = root.find('.//lockdata')
    
    while True:  # Loop to allow reordering until confirmation is given
        # Extract actor names and roles
        actor_info = [(actor.find('name').text, actor.find('role').text) for actor in actors
                      if actor.find('name') is not None and actor.find('role') is not None]
        print(f"Current order of actors in {file_path}:")
        for index, (name, role) in enumerate(actor_info, 1):
            print(f"{index}: {name} as {role}")

        # Get new order from user input, handling both space-separated and contiguous inputs
        order_input = input("Enter the new order of actors by numbers (e.g., '56482' or '5 6 4 8 2' or partial like '5 6'): ")
        order_input = order_input.replace(" ", "")  # Remove spaces if any
        
        # Generate new ordered list of actors based on full or partial input
        try:
            partial_order_indices = [int(idx) - 1 for idx in order_input]
            new_actors_order = [actors[idx] for idx in partial_order_indices]
            remaining_actors = [actor for idx, actor in enumerate(actors) if idx not in partial_order_indices]
            final_actors_order = new_actors_order + remaining_actors
            
            new_actor_info = [(actor.find('name').text, actor.find('role').text) for actor in final_actors_order]
            
            # Show new order for confirmation
            print("New order of actors:")
            for index, (name, role) in enumerate(new_actor_info, 1):
                print(f"{index}: {name} as {role}")

            # Confirm the new order before proceeding
            questions = [
                inquirer.Confirm('confirm', message="Is this order correct?", default=True)
            ]
            answers = inquirer.prompt(questions)

            if answers and answers.get('confirm'):
                # Set lockdata to true
                if lockdata is not None:
                    lockdata.text = 'true'
                else:
                    # If lockdata element doesn't exist, create one
                    ET.SubElement(root, 'lockdata').text = 'true'
                
                # Remove old actors and append new ones in selected order
                for actor in actors:
                    root.remove(actor)
                for actor in final_actors_order:
                    root.append(actor)

                tree.write(file_path)
                print(f"Updated order of actors and set lockdata to true in {file_path}")
                break  # Exit the loop after successful confirmation
            else:
                print("Reordering canceled. Let's try again.")
        except IndexError:
            print("Invalid input. Please ensure the numbers correspond to the actor list.")
        except ValueError:
            print("Please enter only numeric values.")

def main():
    """Main function to run the UI and handle file processing."""
    questions = [
        inquirer.Text('directory', message="What directory do you want to search?")
    ]
    answers = inquirer.prompt(questions)
    directory = answers['directory']

    nfo_files = find_nfo_files(directory)
    if nfo_files:
        for file_path in nfo_files:
            print(f"Processing file: {file_path}")
            reorder_actors(file_path)
        print("All files processed.")
    else:
        print("No 'tvshow.nfo' files found in the directory.")

if __name__ == '__main__':
    main()

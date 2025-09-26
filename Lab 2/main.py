import os
from pathlib import Path

def change_file_extensions_in_folder(folder_path, old_extension, new_extension):
    try:
        for entry in os.scandir(folder_path):
            if entry.is_file():
                file_path = Path(entry.path)
                if file_path.suffix == old_extension:
                    new_file_path = file_path.with_suffix(new_extension)
                    os.rename(file_path, new_file_path)
                    print(f"Renamed '{file_path.name}' to '{new_file_path.name}'")
    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
change_file_extensions_in_folder("C:/Users/Caleb/Downloads/tmp", ".txt", ".js")
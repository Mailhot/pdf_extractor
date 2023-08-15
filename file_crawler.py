import os
import shutil

def save_file_with_new_name(source_path, new_path, new_name):
    try:
        # Copy the file to the new location with the new name
        shutil.copy(source_path, f"{new_path}/{new_name}")
        #print("File saved successfully!")
        print(f"{new_path}/{new_name} Saved!")
    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def crawl_folder(folder_path, destination_folder):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            
            #print("Folder:", item_path)
            crawl_folder(item_path, destination_folder)
        else:
            if item == '_PDF':
                folders = item_path.split('/')
                part_name = folders[-3].replace('_SLDDRW', '')
                new_name = part_name + '_' + folders[-2] + '.pdf'
                if bool([ele for ele in ['SUBC', 'S-0', 'S-1'] if(ele in folders[-4])]): # Check in project name if this is sub-contracting
                    continue
                save_file_with_new_name(item_path, destination_folder, new_name)
                print("File:", item_path)
                if 'SUBC' in item_path:
                    print(folders)

if __name__ == "__main__":
    root_folder = input("Enter the path of the root folder: ")
    destination_folder_input = input("Enter the path of the destination folder: ")
    if not destination_folder_input:
        destination_folder_input = None
    print(root_folder, destination_folder_input)
    if os.path.exists(root_folder) and os.path.exists(destination_folder_input):
        crawl_folder(root_folder, destination_folder=destination_folder_input)
    else:
        print("The provided folders path doesn't exist.")

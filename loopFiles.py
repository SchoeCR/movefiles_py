import os
import shutil

# Set the folder path
source_path = input('\nEnter source path: ')  # Replace with your folder path
dest_path = input('Enter dest path: ')

try:
    # List files in the folder
    for filename in os.listdir(source_path):
        origin = os.path.join(source_path, filename)
        print(f"-------------------------------------------------\nFilename: {filename}")
        print("Choose an operator from the following list:")
        print("\tf - Make folder")
        print("\ts - Skip")
        print("\tt - Terminate")
        response = input("Enter choice: ")
        match response:
            case "s":
                continue
            case "t":
                print("\nOperation terminated\n")
                break
            case "f":
                root = os.path.basename(filename).split('.')[0]
                new_path = os.path.join(dest_path, root)
                os.mkdir(new_path)
                print(f"Directory '{new_path}' created successfully.")
                doEnd = False
                while doEnd != True:
                    moveFile = input("Move file into new directory? - Y or n: ")
                    match moveFile:
                        case "Y":
                            try:
                                shutil.move(origin,new_path)
                                print(f"\n{new_path}\{filename}")
                                if os.path.isfile(f"{new_path}\{filename}") == True:
                                    print("Operation successful")
                                    doEnd = True
                                else:
                                    print("Operation failed\n")
                            except Exception as e:
                                print(f"An error occurred: {e}")
                        case "n":
                            doEnd = True
                            break
                        case _:
                            print("Invalid entry\n")
except FileNotFoundError:
    print(f"Folder not found: {source_path}")
except Exception as e:
    print(f"An error occurred: {e}")
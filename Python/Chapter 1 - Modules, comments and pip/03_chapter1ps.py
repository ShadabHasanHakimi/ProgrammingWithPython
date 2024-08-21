# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Hello, How are you?")
# engine.runAndWait()

import os

def list_directory_contents(path='D:\Programming\Python\ProgrammingWithPython\Python Practice'):
    try:
        # Get the list of all files and directories in the specified directory
        directory_contents = os.listdir(path)
        
        # Print the contents
        print(f"Contents of directory '{path}':")
        for item in directory_contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the desired directory path
# Default is the current directory
list_directory_contents()

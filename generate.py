# When ran, this file will compile all /ui elements to files in /screen_old.

import os

for file in os.listdir("ui/"):
    file_location = f"screen/{file.replace('.ui', '.py')}"
    os.system(f"pyuic5 -o {file_location} ui/{file}")

    # pyuic5/QtDesigner's setupUi method is causing attributes to be garbage collected.
    # To avoid this, we swap this setupUi method with a standard constructor.
    with open(file_location, 'r') as new_file:
        contents = new_file.read()
        contents = contents.replace("setupUi", "__init__")

    with open(file_location, 'w') as write_file:
        write_file.write(contents)

# When ran, this file will compile all /ui elements to files in /screen_old.

import os

for file in os.listdir("ui/"):
    os.system(f"pyuic5 -o screen/{file.replace('.ui', '.py')} ui/{file}")

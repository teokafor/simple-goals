# When ran, this file will compile all /ui elements to files in /screen_old.

import os

for file in os.listdir("src/ui/"):
    os.system(f"pyuic5 -o src/screen/{file.replace('.ui', '.py')} src/ui/{file}")

# cd scripts
# python3 preprocess-from-blender.py futuristic-car-raw/
# node encoder.js -i futuristic-car-raw/ -o futuristic-car/ -w 35 -h 25 -q 75
# cd ..
# python3 -m http.server

import os
import sys

folder = os.path.join(os.getcwd(), sys.argv[1])
files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

prefix = 'input_Cam'
ext = '.png'

renamed_count = 0
for filename in files:

    if(not filename.startswith(prefix)):
        continue

    index = str(int(filename[len(prefix):-len(ext)]))

    os.rename(os.path.join(folder, filename), os.path.join(folder, index + ext))
    renamed_count = renamed_count + 1

print("Renamed " + str(renamed_count) + " files.")
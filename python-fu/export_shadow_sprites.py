from gimpfu import *

# Get list of layers
img = gimp.image_list()[0]
layers = list(img.layers)


# Get directory path
first_file_name = pdb.gimp_image_get_filename(img)
file_dir = first_file_name[0:first_file_name.rfind('\\')] + '\\'

# Create folder for shadows
import os
file_dir = file_dir + '\\shadow_sprites'
if not os.path.exists(file_dir):
	os.makedirs(file_dir)


# Adjust layers and export
for l in layers:
	# Save File
	pdb.gimp_file_save(img, l, file_dir + '\\' + l.name, '?')
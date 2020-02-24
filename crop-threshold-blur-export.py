
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



# Crop image
new_size = img.width * 0.6
offset = img.width/2 - new_size/2
pdb.gimp_image_crop(img, new_size, new_size, offset, offset)

# Adjust layers and export
for l in layers:
	# Layer to black
	pdb.gimp_drawable_threshold(l, 0, 0, 0)
	
	# Blur layer
	for n in range(15):
		pdb.plug_in_blur(img, l)
	
	# Save File
	layer_name = l.name.partition('.')[0]
	newname = layer_name + '_shadow.png'
	pdb.gimp_file_save(img, l, file_dir + newname, '?')


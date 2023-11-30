import pytesseract as pt
from PIL import Image
import bs4

image_directory = "Images/ZandvoortScreenshots/20231130012500_1.jpg"
example_image = Image.open(image_directory)

# print(pt.image_to_string(example_image))

# print(pt.image_to_alto_xml(example_image))

xml_mess = pt.image_to_alto_xml(example_image)

souped_mess = bs4.BeautifulSoup(xml_mess)

pretty_mess = souped_mess.prettify()

# with open("soup_mess.txt", "w") as f:
#     f.write(pretty_mess)

# Rough idea
# 1. Use pt to make an alto xml version of the image.
# 2. Use bs4 to be able to search through file.
# 3. The headings of the files are in the same positions, so can 
#    find horizontal positions of each column. 
# 4. Using horizontal and vertical positions to make rows and
#    columns occur.
# Trouble - Lap and Lap Time Overlap...


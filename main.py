from rembg import remove
import easygui
from PIL import Image

inputPath = easygui.fileopenbox(title='Select an image to remove the background')
outputPath = easygui.filesavebox(title='Save the image as')

input = Image.open(inputPath)
output = remove(input)
output.save(outputPath)
from PIL import Image
 
img = Image.new('RGB', (1280,720), color = 'red')
img.save('pil_red.png')

from PIL import Image

def generate_wechat_cover(path, face):
  image = Image.open("intramirror/"+path+"/"+face+".jpg")
  image = image.resize((image.size[0]*500/image.size[1], 500))
  background = Image.new('RGB', (900, 500), (255,255,255))
  background.paste(image, ((900-image.size[0])/2, 0))
  background.save("wechat-cover/"+path+"-l.png")
  background = background.resize((360, 200))
  background.save("wechat-cover/"+path+"-s.png")

import sys

if len(sys.argv) != 3:
  sys.stderr.write("usage: python %s product-path face" % sys.argv[0])
else:
  generate_wechat_cover(sys.argv[1], sys.argv[2])

from __future__ import print_function
import os
from PIL import Image
bilder = []
def schleife(bilderinschleife,inputa):
    bilder.clear()
    counter = 0
    eingabe = inputa
    while counter < bilderinschleife:
        bilder.extend([eingabe])
        counter = counter +1
    print(len(bilder))



def bild(x,y,r,g,b):
    global result
    result = Image.new("RGBA", (x, y),(r, g, b))

def bildperso(thumbnailx,thumbnaily,xi,yi):
    for index, file in enumerate(bilder):
         path = os.path.expanduser(file)
         img = Image.open(path)
         img.thumbnail((thumbnailx, thumbnaily), Image.ANTIALIAS)
         x = index // 2 * xi
         y = index % 2 * yi
         w, h = img.size
        #print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
         result.paste(img, (x, y, x + w, y + h))
    #result.save(os.path.expanduser('1.jpg'))

def bildfinal(x,y,r,g,b,xa,ya,save):
    final = Image.new("RGB",(x,y),(r, g, b))
    final.paste(result,(xa,ya))
    sp = save.split(".")
    final.save(sp[0]+" P"+".png")

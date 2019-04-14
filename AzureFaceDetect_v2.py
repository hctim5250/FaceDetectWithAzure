import base64
import cognitive_face as CF
import json
from os.path import expanduser
from PIL import Image, ImageDraw, ImageFont

def getRectangle(dataRectangle):    
    left = dataRectangle['left']
    top = dataRectangle['top']
    bottom = left + dataRectangle['height']
    right = top + dataRectangle['width']
    return ((left, top), (bottom, right))

def main():
    KEY = '' #API Key
    CF.Key.set(KEY)

    face_api_url = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0'
    CF.BaseUrl.set(face_api_url)

    #try:
    result = CF.face.detect('image.jpg', attributes='age,gender')
    #img_url='https://how-old.net/Images/faces2/main007.jpg'
    #result = CF.face.detect(img_url, attributes='age,gender')
    faces = result
    """
    for face in faces:
        fId = face["faceId"]
        fGdr = face['faceAttributes']['gender']
        fAge = face['faceAttributes']['age']
        print fId
        print fGdr
        print fAge
        print ''
    """

    dImage = Image.open('image.jpg')
    print dImage.size
    wsize = 4096
    if dImage.size[0]>=wsize:                
        imgRatio = float(wsize)/dImage.size[0]
        hsize = float(dImage.size[1])*imgRatio
        rsImage = dImage.resize((wsize, int(hsize)),Image.ANTIALIAS)
        rsImage.save('image_resize.jpg','JPEG')
        dImage = Image.open('image.jpg')
        draw = ImageDraw.Draw(dImage)
        fs = 25
        ps=28
    else:        
        draw = ImageDraw.Draw(dImage)
        fs=25
        ps=28
    
    font = ImageFont.truetype('/usr/share/fonts/truetype/piboto/PibotoLt-Regular.ttf',fs)
    draw.ink = 255+0*256+0*256*256
    
    for face in faces:
        a = face['faceRectangle']
        b = getRectangle(a)
        draw.rectangle(b, outline='red')
        fa = face['faceAttributes']
        draw.text([b[0][0],b[0][1]-ps], "Gender="+fa['gender']+", Age= "+str(round(fa['age'],2)),font=font)
    del draw   
    dImage.save('result.jpg','JPEG')
    print "Done."
        
    #except Exception as e:
        


if __name__ == '__main__':

    main()

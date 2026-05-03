import cv2
from ultralytics import YOLO
class VisionEngine:
 def __init__(self):
  self.model=YOLO("yolov8n.pt")
  self.conf=0.20
  self.clahe=cv2.createCLAHE(2.0,(8,8))
 def analyze(self,path):
  img=cv2.imread(path)
  if img is None:return {"sdi":0,"sku":0,"cov":0}
  lab=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
  l,a,b=cv2.split(lab)
  l=self.clahe.apply(l)
  img=cv2.cvtColor(cv2.merge((l,a,b)),cv2.COLOR_LAB2BGR)
  img=cv2.resize(img,(640,640))
  res=self.model(img,verbose=False)
  boxes=[]
  for r in res:
   if r.boxes is None:continue
   for box in r.boxes:
    if float(box.conf[0])>=self.conf:
     boxes.append(box.xyxy[0].tolist())
  sku=len(boxes)
  area=sum(max(0,(b[2]-b[0]))*max(0,(b[3]-b[1])) for b in boxes)
  raw=area/(640*640)
  sku_proxy=min(sku/12,0.9)
  if raw<0.25:
   sdi=max(0.45,sku_proxy)
  else:
   sdi=0.6*raw+0.4*sku_proxy
  return {"sdi":round(min(sdi,1),4),"sku":sku,"cov":round(raw,3)}

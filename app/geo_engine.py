import hashlib
class GeoEngine:
 def get(self,lat,lng):
  h=int(hashlib.md5(f"{round(lat,2)}{round(lng,2)}".encode()).hexdigest(),16)
  c=int((h%20)+5)
  f=min(c*0.1,0.9)
  comp=0.7 if c<5 else 0.4
  return round(0.35*0.5+0.4*f+0.25*comp,4)

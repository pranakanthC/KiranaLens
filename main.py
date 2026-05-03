import streamlit as st
from app.vision_engine import VisionEngine
from app.geo_engine import GeoEngine
from app.fraud_engine import FraudEngine
from app.decision_engine import DecisionEngine
st.title("KiranaLens")
lat=st.number_input("Latitude",12.97)
lng=st.number_input("Longitude",77.59)
files=st.file_uploader("Upload images",accept_multiple_files=True)
if st.button("Run Audit"):
 if files:
  v=VisionEngine()
  s=[];c=[]
  for i,f in enumerate(files[:5]):
   open(f"img{i}.jpg","wb").write(f.read())
   r=v.analyze(f"img{i}.jpg")
   s.append(r["sdi"]);c.append(r["cov"])
  sdi=sum(s)/len(s)
  cov=sum(c)/len(c)
  g=GeoEngine().get(lat,lng)
  f=FraudEngine().run(sdi,g,cov)
  m,conf,res,x=DecisionEngine().run(sdi,g,f)
  st.success(f"Recommended Credit Limit: ₹{m}")
  st.write(f"Confidence: {int(conf*100)}%")
  st.write(f"Decision: {res}")
  st.info(x)

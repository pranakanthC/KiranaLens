class FraudEngine:
 def run(self,s,g,c):
  if s>0.6 and g<0.4:return "HIGH"
  if c<0.3:return "LOW"
  return "CLEAR"

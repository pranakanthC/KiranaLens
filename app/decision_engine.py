class DecisionEngine:
 def run(self,s,g,f):
  base=50000
  m=s*base*(1+g)
  h=0
  if f=="HIGH":
   m*=0.6
   h=40
  cons=1-abs(s-g)
  conf=max(0.1,round(0.6*cons+0.4*s,3))
  d="APPROVE" if conf>=0.5 else "VERIFY"
  x=f"Credit derived from SDI {round(s,3)} and geo {round(g,3)}. Consistency {round(cons,3)}. Haircut {h}%."
  return int(m),conf,d,x

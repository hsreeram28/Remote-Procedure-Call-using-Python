import rpyc
conn = rpyc.classic.connect("localhost")
conn.execute('import math')
conn.eval('2*math.pi')

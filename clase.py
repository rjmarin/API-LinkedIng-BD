import psycopg2
import datetime  
import time 
from tabulate import tabulate
import matplotlib.pyplot as plt

conn = psycopg2.connect(host = "201.238.213.114", port= "54321", database="grupo23", user="grupo23", password="f9kNXT")
cur = conn.cursor()
id = 2
fechast = []
fechasr = []
cur.execute("SELECT id_publicacion FROM  publicacion WHERE id_usuario = {} and 	estado = 'Activo'".format(id))
publicaciones = cur.fetchall()
for i in publicaciones:
	cur.execute("SELECT EXTRACT(MONTH FROM fecha)m , COUNT(*)  FROM comentario WHERE id_publicacion = {} GROUP BY m ".format(i[0]))
	ff = cur.fetchall()
	for f in ff:
		fechast.append(f)


cur.execute("SELECT EXTRACT(MONTH FROM fecha)m , COUNT(*)  FROM comentario WHERE id_usuario = {} GROUP BY m ".format(id))
fe = cur.fetchall()
for f in fe:
	fechasr.append(f)
cur.execute("SELECT EXTRACT(MONTH FROM fecha)m , COUNT(*)  FROM sub_comentario WHERE id_usuario = {} GROUP BY m ".format(id))
fe = cur.fetchall()
for f in fe:
	fechasr.append(f)

cur.execute("SELECT id_comentario FROM comentario WHERE id_usuario = {} ".format(id))
coments = cur.fetchall()
for j in coments:
	cur.execute("SELECT  EXTRACT(MONTH FROM fecha)m , COUNT(*) FROM sub_comentario  WHERE id_comentario = {} GROUP BY m".format(j[0]))
	cc = cur.fetchall()
	for c in cc: 
		fechast.append(c)
mesest= []
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0
c10 = 0
c11 = 0
c12 = 0

for k in fechast:
	if k[0] == 1:
		c1+=k[1]	
	elif k[0] == 2:
		c2+=k[1]
	elif k[0] == 3:
		c3+=k[1]
	elif k[0] == 4:
		c4+=k[1]
	elif k[0] == 5:
		c5+=k[1]
	elif k[0] == 6:
		c6+=k[1]
	elif k[0] == 7:
		c7+=k[1]
	elif k[0] == 8:
		c8+=k[1]
	elif k[0] == 9:
		c9+=k[1]
	elif k[0] == 10:
		c10+=k[1]
	elif k[0] == 11:
		c11+=k[1]
	elif k[0] == 12:
		c12+=k[1]

mesest.append(c1)
mesest.append(c2)
mesest.append(c3)
mesest.append(c4)
mesest.append(c5)
mesest.append(c6)
mesest.append(c7)
mesest.append(c8)
mesest.append(c9)
mesest.append(c10)
mesest.append(c11)
mesest.append(c12)



mesesr= []
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0
c10 = 0
c11 = 0
c12 = 0

for k in fechasr:
	if k[0] == 1:
		c1+=k[1]	
	elif k[0] == 2:
		c2+=k[1]
	elif k[0] == 3:
		c3+=k[1]
	elif k[0] == 4:
		c4+=k[1]
	elif k[0] == 5:
		c5+=k[1]
	elif k[0] == 6:
		c6+=k[1]
	elif k[0] == 7:
		c7+=k[1]
	elif k[0] == 8:
		c8+=k[1]
	elif k[0] == 9:
		c9+=k[1]
	elif k[0] == 10:
		c10+=k[1]
	elif k[0] == 11:
		c11+=k[1]
	elif k[0] == 12:
		c12+=k[1]

mesesr.append(c1)
mesesr.append(c2)
mesesr.append(c3)
mesesr.append(c4)
mesesr.append(c5)
mesesr.append(c6)
mesesr.append(c7)
mesesr.append(c8)
mesesr.append(c9)
mesesr.append(c10)
mesesr.append(c11)
mesesr.append(c12)

x = [1,2,3,4,5,6,7,8,9,10,11,12]
plt.plot(x, mesesr, "r", x, mesest, "b")
plt.legend(["Comentario creados", "Comentario que ha tenido"])
plt.show()




















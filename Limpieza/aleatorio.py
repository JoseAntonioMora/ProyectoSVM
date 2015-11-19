
final = open("prediccion90-10.txt", 'w')
archivo = open("testironicos.txt",'r')
archivo2 = open("noironicos.txt",'r')

cont = 0
nl=0
for linea in archivo:
	if nl >1:
		if cont < 900:
			linea=linea.strip()
			linea = linea + '\n'
			final.write(linea)
			cont = cont +1
		else:
			break
	nl = nl+1

cont = 0 
nl=0
for linea in archivo2:
	if nl> 30800:
		if cont < 100:
			linea=linea.strip()
			linea = linea + '\n'
			final.write(linea)
			cont = cont +1
		else:
			break
	nl=nl+1

final.close()


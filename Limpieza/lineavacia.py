import argparse

p = argparse.ArgumentParser("Limpieza")
p.add_argument("Archivo", default = None, action="store", help="Archivo para eliminar saltos de linea")
p.add_argument("-l","--nlineas",default = 0, action= "store", type=int, dest="nlineas", help="Numero de lineas a almacenar")

opts = p.parse_args()

nombre = raw_input("Nombre del archivo final:")
nombre = nombre + ".txt"
archivo = open(opts.Archivo,'r')
final = open(nombre, 'w')

cont = 0
if opts.nlineas > 0:
	for linea in archivo:
		if cont < opts.nlineas:
			linea=linea.strip()
			if len(linea) > 1:
				linea = linea + '\n'
				final.write(linea)
			cont = cont +1
		else:
			break
else:
	for linea in archivo:
		linea=linea.strip()
		if len(linea) > 1:
			linea = linea + '\n'
			final.write(linea)
final.close()
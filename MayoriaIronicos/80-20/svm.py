from sklearn.feature_extraction.text import CountVectorizer
import argparse
from sklearn import svm
import cPickle

p = argparse.ArgumentParser("Ejemplo")
p.add_argument("Archivo1", default = None, action="store", help="Archivo con tweets ironicos")
p.add_argument("Archivo2", default = None, action="store", help="Archivo con tweets no ironicos")



opts = p.parse_args()

archivo1=open(opts.Archivo1,'r')
archivo2=open(opts.Archivo2,'r')


vectorizer=CountVectorizer(min_df=5)

lista=[]
listafinal=[]
clases=[]

for linea in archivo1:
	linea= unicode(linea,'utf-8')
	linea=linea.strip()
	if len(linea) > 1:
		lista.append(linea)
		clases.append(1)

for linea in archivo2:
	linea= unicode(linea,'utf-8')
	if len(linea) > 1:
		linea=linea.strip()
		lista.append(linea)
		clases.append(0)

#print lista
print clases
x = vectorizer.fit_transform(lista)
#print x.toarray()

clf=svm.SVC(kernel='linear', C=1.0, verbose= True)

modelo = clf.fit(x,clases)
print "---------------------------------------------"

f = file('Model.save', 'wb')
cPickle.dump(modelo, f, protocol=cPickle.HIGHEST_PROTOCOL)
f.close()

vec = file('Vectorizer.save', 'wb')
cPickle.dump(vectorizer, vec, protocol=cPickle.HIGHEST_PROTOCOL)
vec.close()

f = file('Clases.save', 'wb')
cPickle.dump(modelo, f, protocol=cPickle.HIGHEST_PROTOCOL)
f.close()

#Aqui se crea el documento para poder predecir a partir del modelo
# for linea in archivo3:
# 	linea= unicode(linea,'utf-8')
# 	linea=linea.strip()
# 	if len(linea) > 1:
# 		listafinal.append(linea)		

# for linea in archivo4:
# 	linea= unicode(linea,'utf-8')
# 	if len(linea) > 1:
# 		linea=linea.strip()
# 		listafinal.append(linea)		

# pre = vectorizer.transform(listafinal)
# #print pre
# print pre.toarray()
# print clases
# print "---------------------------------------------"
# res=clf.predict(pre)
# from sklearn import metrics
# print(metrics.classification_report(clases, res))

from sklearn.feature_extraction.text import CountVectorizer
import argparse
from sklearn import svm
import cPickle
from sklearn import metrics
from sklearn.metrics import confusion_matrix

p = argparse.ArgumentParser("Ejemplo")
p.add_argument("Archivo1", default = None, action="store", help="Archivo con tweets")
opts = p.parse_args()
archivo1=open(opts.Archivo1,'r')

listafinal=[]
clases =[]


f = file('Model.save', 'rb')
clf = cPickle.load(f)
f.close()

g = file('Vectorizer.save', 'rb')
vectorizer = cPickle.load(g)
g.close()

# c = file('Clases.save', 'rb')
# clases= cPickle.load(c)
# c.close()


nl =0
for linea in archivo1:
	if nl > 900:
		clases.append(0)
	else:
		clases.append(1)
	nl = nl+1
	linea= unicode(linea,'utf-8')
	linea=linea.strip()
	if len(linea) > 0:
		listafinal.append(linea)


pre = vectorizer.transform(listafinal)
print pre.toarray()
print "---------------------------------------------"
res=clf.predict(pre)

print "Resultado de la prediccion--->", res

print(metrics.classification_report(clases, res))
print "Confusion Matrix"
print confusion_matrix(clases, res)
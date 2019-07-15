import shutil

vetorlaudos = [line.rstrip() for line in open('C:/Generator/lista.txt')]

quant_laudos = len(vetorlaudos)

i=1
for i in range (quant_laudos):
	juntador ='C:/Generator/arquivos/'+vetorlaudos[i]+'.pdf'
	shutil.copyfile('C:/Generator/L00000000000000.pdf',juntador)
	i = i + 1

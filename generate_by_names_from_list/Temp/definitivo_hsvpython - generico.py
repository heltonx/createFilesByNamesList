import shutil

vetorlaudos = [line.rstrip() for line in open('C:/Temp/lista.txt')]

quant_laudos = len(vetorlaudos)

i=1
for i in range (quant_laudos):
	juntador ='C:/Temp/arquivos/'+vetorlaudos[i]+'.pdf'
	shutil.copyfile('C:/Temp/L00000000000000.pdf',juntador)
	i = i + 1

import shutil

vetorlaudos = [line.rstrip() for line in open('D:/Temp/faturamento/laudos_data_atual.txt')]
#rstrip remove espa�os � direita
#ent�o a variavel vetorlaudos est� recebendo o conteudo de todas as linhas do txt, mas sem os espa�os

quant_laudos = len(vetorlaudos) #recebe a quantidade de linhas (laudos) no txt, para usar no la�o de repeti��o

i=1
# para cada linha no range
for i in range (quant_laudos):
        #j� deixa o caminho de destino pronto na var juntador, especificando o laudo da rodada
        #e ja deixa pronto o nome do arquivo
	juntador ='D:/Temp/faturamento/L0/'+vetorlaudos[i]+'.pdf'
	#antes da virgula eh o arquivo que vai ser copiado, depois da virgula eh o destino
	shutil.copyfile('D:/Temp/faturamento/L00000000000000.pdf',juntador) 
	i = i + 1 # j� deixa pronto pra pr�xima rodada

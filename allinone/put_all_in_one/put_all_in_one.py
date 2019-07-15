#!/usr/bin/env python
# -*- coding: utf-8 -*-
#precisa desse comentario "coding..." para poder comentar com acento

#para funcionar esse programa precisa estar no mesmo diretório
#dos arquivos

import glob 

vetor = glob.glob('all/*.txt') #o glob vai juntar tudo que tem .txt nesse diretorio

quant_files = len(vetor)

unico=[]#cria a variável unico, que vai armazenar o conteúdo dos arquivos até coloca no arquivo único definitivo
string='\n'#prepara a nova linha para se posta no laço de repetição

i=1
for i in range (quant_files):
	arquivo = open(vetor[i],'r')#pelo nome do arquivo da rodada, pega o arquivo equivalente e abre
	aux = arquivo.readlines() #vai colocar, linha por linha, o conteudo do arquivo na variavel
	if i > 1: #se for a primeira rodada, não acrescentar nova linha, senão vai ficar uma linha em branco
                unico.append(string)#para cada arquivo novo acrescenta uma nova linha, senão a primeira linha do novo ia ficar grudada na ultima do velho
	unico = unico + aux#vai manter o que ja tem e acrescentar o conteúdo do novo arquivo
	i=i+1

f = open('arquivo_unico.txt','w') #abre o arquivo para escrever o resuldado
f.writelines(unico)#escreve o resultado da união de todos os arquivos

#comandos que não foram úteis nem necessários, porém úteis em outros programas
#pickle.dump(unico,f) - usado no dieckmon
#shutil.copyfile(unico,f) - usado no hsvpython

#este programa passou nos testes realizados, que foram:
#-executar e ver o resultado em Kb, ao mesmo tempo em que
#se fez o processo tradicional (copying one by one), mas se deu um byte a mais no arquivo pelo programa,
#o arquivo_unico deu 36,6 e o tradicional deu 36,5
#-ver quantas linhas da no Calc, e deram as duas 425 linhas
#-ver se o primeiro e o último arquivo têm o mesmo nome

import shutil
import os

#Replace HERE by the file you want copies with different names
FILE_TO_REPLICATE = 'L00000000000000.pdf'

isExist = os.path.exists('result/') #if result directory does not exist, creates it
if not isExist:
	os.makedirs('result/')

arrayNames = [line.rstrip() for line in open('sampleList.txt')]

sumNames = len(arrayNames)

for i in range (sumNames):
	joiner ='result/'+arrayNames[i]+'.pdf'
	shutil.copyfile(FILE_TO_REPLICATE,joiner)

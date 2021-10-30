# custom gapps extractor by wahyu6070
# 21.04 30-10-2021
#

import os
import zipfile
import tarfile
import subprocess
import shutil

def UNZIP(INPUT1, INPUT2):
	with zipfile.ZipFile(INPUT1 , 'r') as zip_ref:
		zip_ref.extractall(INPUT2)

INPUT = "input/"
TMP = "tmp/"
OUTPUT = "output/"

print(" ")
print("              Custom Gapps Extractor by wahyu6070")
print(" ")
for LIST_INPUT in os.listdir(INPUT):
    if os.path.isfile(INPUT + LIST_INPUT):  
         if not os.path.exists(TMP + LIST_INPUT):
         	os.makedirs(TMP + LIST_INPUT)
         else:
         	shutil.rmtree(TMP + LIST_INPUT)
         	os.makedirs(TMP + LIST_INPUT)
         if not os.path.exists(OUTPUT + LIST_INPUT):
         	os.makedirs(OUTPUT + LIST_INPUT)
         else:
         	shutil.rmtree(OUTPUT + LIST_INPUT)
         	os.makedirs(OUTPUT + LIST_INPUT)	
         if LIST_INPUT.startswith("open_gapps"):
         	print("- Opengapps Detected") 
         	print("- Extracting : ", INPUT + LIST_INPUT)
         	UNZIP(INPUT + LIST_INPUT, TMP + LIST_INPUT)
         	for root, dirs, files in os.walk(TMP + LIST_INPUT):
         		for file in files:
         			if file.endswith('.lz'):
         			 	LZ_IN = os.path.join(root, file)
         			 	LZ_OUT = os.path.join(root)
         			 	print("- Extracting •> ", LZ_IN)
         			 	# opengapps using lzip compression
         			 	subprocess.call(["tar", "-xf", LZ_IN, "-C", LZ_OUT])
         			 	os.remove(LZ_IN)
         	#moving files
         	for root, dirs, files in os.walk(TMP + LIST_INPUT):
         		for FILES in dirs:
         			if FILES == 'nodpi':
         				input_mv = os.path.join(root, FILES)
         				out_mv = os.path.join(OUTPUT, LIST_INPUT,  FILES)
         				shutil.copytree (input_mv, out_mv, dirs_exist_ok=True)
         			elif FILES == 'common':
         				input_mv = os.path.join(root, FILES)
         				out_mv = os.path.join(OUTPUT, LIST_INPUT,  FILES)
         				shutil.copytree (input_mv, out_mv, dirs_exist_ok=True)	
         			elif FILES == '480':
         				input_mv = os.path.join(root, FILES)
         				out_mv = os.path.join(OUTPUT, LIST_INPUT,  FILES)
         				shutil.copytree (input_mv, out_mv, dirs_exist_ok=True)
         			elif FILES == '320':
         				input_mv = os.path.join(root, FILES)
         				out_mv = os.path.join(OUTPUT, LIST_INPUT,  FILES)
         				shutil.copytree (input_mv, out_mv, dirs_exist_ok=True)	
         else:
         	print("! Package not support : ", LIST_INPUT)
         	
    else:
        print("! Is Not package file : ", INPUT + LIST_INPUT)
        
        
shutil.rmtree(TMP)

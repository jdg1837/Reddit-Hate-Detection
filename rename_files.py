import sys
import os 

if len(sys.argv) < 2:
    print("Please include directory name and file suffix")
directory = sys.argv[1]

for filename in os.listdir(directory):
    dst = filename.split('_')[0] + '_' + directory + '.json'
    src = directory + '/' + filename 
    dst = directory + '/' + dst 
    os.rename(src, dst)
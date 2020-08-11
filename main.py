import os
import sys

count=0
print(f"number of occurence of "+ sys.argv[1])
dir_content = os.listdir()
# print(dir_content)
for file in dir_content:
    if(file.endswith(".txt")):
        document=open(file)
        word_list=document.read().split()
        for word in word_list:
            if word.casefold() == sys.argv[1].casefold():
                count+=1
print(count)

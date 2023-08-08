import os
os.chdir("c:/Users/User/Desktop/Web dev/django/facebook/python/")

# print(os.path.abspath("sampletext"))
# 
# file_contents = 'Because I could\n not stop for Death,\n' #, 'He kindly stopped for me;\n', 'The carriage held but just ourselves\n', 'And Immortality.']
# print(file_contents.split("\n")[0])


file = open("sampletext.txt", "r")
print(file.read())

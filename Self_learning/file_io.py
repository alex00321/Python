# file = open("hello.txt",mode="w")
# file.write("hello,world!")
import os
file = open("crash.txt",mode="w")
file.write("hello,world!")
os._exit(1)
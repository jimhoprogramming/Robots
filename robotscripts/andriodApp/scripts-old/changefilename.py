#-*-coding:utf8;-*-
#qpy:console
#qpy:2
import os 
def change(path): 
   i = 1 
   for f in os.listdir(path): 
      
      a,b = os.path.splitext(f) 
      print(str(i))
      print(a)
      print(b)
      #print(os.sep)
      if b == '.mp4': 
          os.rename(f, str(i) + os.extsep+'dat') 
      i+=1
if __name__ == '__main__': 
    chpath='/storage/sdcard0/download'
    os.chdir(chpath)
    path=os.getcwd()
    change(path)
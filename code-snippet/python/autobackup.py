import os
import shutil
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='backup.log',
                    filemode='a',
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )

srcFolder = "/Users/liang/study/src"
destFolder = "/Users/liang/study/dest"

fileNum = 0
def copy_folder(src, dest):
  global fileNum
  global srcFolder
  global destFolder
  names = os.listdir(src)
  if not os.path.exists(dest):
    os.mkdir(dest)
  for name in names:
    srcName = os.path.join(src, name)
    destName = os.path.join(dest, name)
    try:
      if os.path.isdir(srcName):
        copy_folder(srcName, destName)
      else:
        if (not os.path.exists(destName)
          or ((os.path.exists(destName))
            and (os.path.getsize(destName) != os.path.getsize(srcName)))):
          logging.info("src:"+ srcName)
          shutil.copy2(srcName, dest)
          fileNum = fileNum + 1
    except:
      logging.error ("file copy faild:"+srcName)
      raise

def dir_backup():
  global fileNum
  fileNum = 0
  logging.info("-------backup start--------")
  copy_folder(srcFolder, destFolder)
  logging.info("****copy total file number "+ str(fileNum))
  logging.info("-------backup finsh--------")
  print("backup finish")

if __name__=="__main__":
  dir_backup()
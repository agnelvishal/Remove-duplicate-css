import re

def main():

    #Open the file back and read the contents
    with open("1st place.md","r") as f:
        allLessFiles=[]
        similarLessFiles=[]
        fl =f.readlines()
        flagContainsStar = True
        flagWrite = False
        stringToWrite=""
        for line in fl:
          words = line.split()
          if len(words)!=0:
              #print(flagContainsStar)
              if words[0] == "*":
                  if flagContainsStar == True:
                    similarLessFiles.append(words[1])
                    #print(words[1],end="")
                    flagContainsStar = True
                  else:
                    allLessFiles.append(similarLessFiles)
                    #print("")
                    #print(words[1],end="")
                    similarLessFiles=[]
                    similarLessFiles.append(words[1])
                    flagContainsStar = True
              else:
                  flagContainsStar = False
              if(words[0]) == "####":
                  #newFile2 = re.findall('"([^"]*)"', words)
                  #print(newFile2)
                  newfile = words[-1]
                  newfile = newfile.replace('.','')
                  newfile = newfile.replace('"','')
                  newfile = newfile.replace(' ','')
                  newfile = newfile.replace("'",'')
                  newfile = newfile.replace("[",'')
                  newfile = newfile.replace("]",'')
                  newfile = newfile.replace(">",'')
                  newfile = newfile.replace("<",'')
                  newfile = newfile + ".less"
                  #print(type(newfile))
                  # with open(newfile,"w") as writeF:
                  #     writeF.write("hello")
              if words[0] == "```":
                  with open(newfile,"w") as writeF:
                       writeF.write(stringToWrite)
                  for loc in similarLessFiles:
                      loc = "C:\\Users\\Lenovo\\src"+loc.replace("/","\\")
                      with open(loc,"r",encoding="utf8") as of:
                          fileS = of.read()
                          print(stringToWrite)
                          print(loc)
                          print(fileS.find(stringToWrite))
                  flagWrite = False
              if flagWrite == True:
                 #stringToWrite +="\n"
                 #stringToWrite += ''.join(words)
                 stringToWrite += line
              else:
                  stringToWrite = ""
              if words[0] == "```css":
                  flagWrite = True
                  # while words[0] != "```":
                      # stringToWrite += words[0]

          else:
              flagContainsStar = False
        #print(allLessFiles)

if __name__== "__main__":
  main()
  x=input()

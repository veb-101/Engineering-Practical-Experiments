# SPCC Exp 6 Lexical Analyzer

with open("Exp6.txt", "r") as f:
  data = f.readlines()
  data = list(map(lambda x: x.replace("\n", "" ), data))
  #print(data)
  keywords = ['include','stdio.h','auto','break','case','char','const','continue','default','do','double','else','enum','extern','float','for','goto','if','int','long',
              'register','return','short','signed','sizeof','static','struct','switch','typedef','union','unsigned','void','volatile','while']
  paranthesis = ['{','}','[',']','(',')','<','>']
  delimiters = [';',' ',',']
  print("Lexical Analyzer")
  for j in data:
    j = j.split()
    for i in j:
      if i in keywords:
        print("Keyword: \t\t",i)
      elif '#' in i:
        print("Header File: \t",i)
      elif '(' and ')' in i:
        print("Function: \t\t",i)
      elif i in paranthesis:
        print("Paranthesis: \t",i)
      elif i in delimiters:
        print("Delimiters: \t\t",i)
      else:
        print("Variable: \t\t",i)
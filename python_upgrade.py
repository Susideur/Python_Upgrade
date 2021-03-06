from ion import keydown,KEY_LEFT,KEY_RIGHT,KEY_UP,KEY_DOWN,KEY_EXE,KEY_OK
from time import sleep

def super_print(screen,list_,page=True,fill=False,valid=False):
### v Testing fonction v ###
  if not (type(screen) == bool or type(screen) ==  str): raise TypeError("\n\tParamètre 'screen' : Le contenu doit être un Booléen ou un Str.")
  if not type(list_) == list: raise TypeError("\n\tParamètre 'list_' : Le contenu n'est pas une liste.")
  if not(type(page) == int or type(page) == bool): raise TypeError("\n\tParamètre 'page' : Le contenu n'est pas valide.")
  if not type(fill) == bool: raise TypeError("\n\tParamètre 'fill' : Le contenu n'est un Booléen")
  if not(type(valid) == int or type(valid) == bool or valid == {"easter": 99}): raise TypeError("\n\tParamètre 'valid' : Le contenu n'est pas valide.")
### ^ Testing fonction ^ ###
  def __init__(screen,list_,page):
    try:
      screen+1
      if not screen: letters,lines=27,11
      if screen: letters,lines=40,14
    except TypeError:
      screen=screen.split("x")
      if len(screen) == 2 and screen[0].isdigit() and screen[1].isdigit(): lines,letters=int(screen[0]),int(screen[1])
      else: raise TypeError("\n\tParamètre 'screen' : Le format de résolution n'est pas valide. (format : '<lignes>x<lettres>')")
    Nb,index,Nb_page=len(list_),0,0
    try:
      if page == True:
        page=Nb//(lines-1)
        if Nb%(lines-1): page+=1
    except ZeroDivisionError: raise ValueError("\n\tParamètre 'screen' : Le contenu n'est pas valide.")
    return letters,lines,index,Nb,Nb_page,page
  
  def printing(list_,Nb,index,lines):
    try:
      print()
      for i in range(Nb):
        print(list_[index])
        index+=1
        lines-=1
    except IndexError: ...
    return lines,index

  def filling(fill,lines):
    if fill == True:
      for i in range(lines): print()

  def page_indexing(letters,page,Nb_page):
    letters_space="  "
    for i in range(letters-len(">EXE to exit"+"Page "+"/"+str(Nb_page)+str(page))):
      letters_space=letters_space+" "
    print(">EXE to exit{}Page {}/{}".format(letters_space,Nb_page,page))
    return page,Nb_page

  def scanAndprint(list_,page,fill,Nb,Nb_page,index,lines,letters,left=False):
    if page == False:
      lines,index=printing(list_,Nb,index,lines)
      filling(fill,lines)

    if page == True or page >=2:
      lines-=1
      if left == True:
        for i in range(Nb):
          if not index%lines: break
          index+=1
        index+=-lines*2
      if Nb>lines: Nb=lines
      lines,index=printing(list_,Nb,index,lines)
      filling(True,lines)
      page,Nb_page=page_indexing(letters,page,Nb_page)
  ### v Debug line v ###
  #  print("Nb:{} lines:{} index:{}".format(Nb,lines,index))
  ### ^ Debug line ^ ###
    return index

  letters,lines,index,Nb,Nb_page,page=__init__(screen,list_,page)
  Nb_page+=1
  index=scanAndprint(list_,page,fill,Nb,Nb_page,index,lines,letters)
  sleep(0.2)
  while (page == True or page >= 2):
    if keydown(KEY_EXE): break
    if keydown(KEY_LEFT) and Nb_page < page+1 and Nb_page > 1:
      Nb_page-=1
      index=scanAndprint(list_,page,fill,Nb,Nb_page,index,lines,letters,True)
      sleep(0.2)

    if keydown(KEY_RIGHT) and Nb_page < page and Nb_page > 0:
      Nb_page+=1
      index=scanAndprint(list_,page,fill,Nb,Nb_page,index,lines,letters)
      sleep(0.2)

  if valid == False: return False
  else:  
    if valid == 1: input("-->          _|OK|_           ")
    if valid == 2: input("-->        _|Retour|_         ")
    if valid == 3: input("-->        _|Cancel|_         ")
    if valid == {"easter": 99}: input("--> _|LoL it's a Easter Egg|_ "); input("-->   _|Morgan le caca !|_    "); input("-->     _|Tina la BG !|_      "); input("-->    _|Made by Zackari|_    "); input("-->    _|It's my name XD|_    ")
    return True

######Fonction separator######

def len2(object):
  try: return len(object)
  except TypeError: 
    if type(object) == type: return len(str(object))-10
    else: return len(str(object))

######Fonction separator######

def AIsplit(letters,text,separator=" ",full=True):
### v Testing fonction v ###
  if not (type(letters) == int or type(letters) == bool): raise TypeError("\n\tParamètre 'letters' : Le contenu n'est pas un Int.")
  if letters < 1: raise ValueError("\n\tParamètre 'letters' : Le contenu doit être supérieur à 1.")
  if not type(text) == str: raise TypeError("\n\tParamètre 'text' : Le contenu n'est pas un Str.")
  if not type(separator) == str: raise TypeError("\n\tParamètre 'separator' : Le contenu n'est pas un Str.")
  if separator == "": raise ValueError("\n\tParamètre 'separator' : Le séparateur est vide.")
### ^ Testing fonction ^ ###
  if letters == False: letters=27
  if letters == True: letters=42
  if separator == "\n": separator=" "
  if full == True: 
    text,index=text.split(separator),0
    for i in text:
      if len(i) > letters: 
        __temp__=insert(letters,i,"\n",True).splitlines()
        del text[index]
        for object in range(len(__temp__)): text.insert(index+object,__temp__[object])
        __temp__=[]
      index+=1
    for i in range(len(text)*int(letters/2)):
      try: 
        if not len(text[i]+text[i+1]) >= letters: 
          text[i+1]=separator.join([text[i],text[i+1]])
          del text[i]
      except IndexError: break
    #for i in range(text.count(" ")): text.remove(" ")
    return text
  else: return insert(letters, text,"\n",True)

######Fonction separator######

def list2print(list_,lines):
### v Testing fonction v ###
  if not type(list_) == list: raise TypeError("\n\tParamètre 'list_' : Le contenu n'est pas une liste.")
  if not type(lines) == int: raise TypeError("\n\tParamètre 'lines' : Le contenu n'est pas un Int.")
  if len(list_) < lines: raise IndexError("\n\tErreur : 'lines' doit être inférieur au nombre d'occurrences de 'list_'.")
### ^ Testing fonction ^ ###
  def printing(list_,index,lines):
    print()
    for i in range(lines):
      print(list_[index])
      index+=1
    return index

  def up(list_,index,lines):
    if index>lines+1:
      index+=-lines-1
      index=printing(list_,index-1,lines+1)
    sleep(0.2)
    return index

  def down(list_,index):
    if index<len(list_):
      print(list_[index])
      index+=1
    sleep(0.2)
    return index
  
  index=printing(list_,0,lines)
  sleep(0.2)
  while True:
    if keydown(KEY_EXE) or keydown(KEY_OK): break
    if keydown(KEY_UP): index=up(list_,index,lines)
    if keydown(KEY_DOWN): index=down(list_,index)
  return

######Fonction separator######

def insert(index,object,add,repeat=False):
### v Testing fonction v ###
  if not type(index) == int: raise TypeError("'index': string indices must be integers")
  if index < 1: raise ValueError("'index' must be greater than 1.")
  if type(object) == type: raise TypeError("cannot insert 'object' into a type")
  if not type(repeat) == bool: raise TypeError("'repeat' must be a boolean")
### ^ Testing fonction ^ ###
  __temp__,save='',index
  for i in range(len(object)+1):
    try:
      if i == index: 
        __temp__+=str(add)
        if repeat: index+=save
  ### v Debug line v ###
  #      print(index,":",i,":",__temp__)
  ### ^ Debug line ^ ###
      __temp__+=object[i]
    except IndexError: ...
  if (not len(object) % save) and repeat == True: __temp__+=str(add)
  return __temp__

######Fonction separator######

def reverse(object):
  if type(object) == str:
    output, index="", len(object)
    for i in range(index):
      output+=object[index-i-1]
    return output
    
  elif type(object) == list: 
    object.reverse()
    return object

  elif type(object) == dict:
    output={}
    for (key, value) in object.items():
      output.update({str(value): key})
    return output

  elif type(object) == tuple:
    output, index=(), len(object)
    for i in range(index):
      output+=(object[index-i-1],)
    return output
  
  else: raise TypeError("type '{}' isn't accepted".format(type(object)))

######Fonction separator######

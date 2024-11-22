import os
from termcolor import  colored

def collectVals ():
  header ()
  body ()

def header ():
  clrSc ()
  print ()
  print (colored ("                **** CollectVals ****                ", "blue", attrs= ["bold"]))
  print ()
  input (colored ("[Press any key to proceed]", "magenta"))
  clrLn (1)
  print (colored (" *    Description: Calculate the average          * \n        of any list of numbers", "cyan"))
  print ()
  print (colored ("                                                    ", "white", attrs= ["underline"]))
  print ()
  input (colored ("[Press any key to proceed]", "magenta"))
  clrLn (2)

  return 10

def body ():
 menu ()

def menu ():
  print ()
  print (colored ("                **** Menu ****                 ", "blue", attrs= ["bold"]))
  input (colored ("[Press any key to proceed]", "magenta"))
  clrLn (1)
  print ()
  print (colored ("  Options: ", "cyan"))
  print ()
  print (colored ("    a = Calculate Average"))
  print (colored ("    x = exit"))
  print ()
  input (colored ("[Press and key to proceed]", "magenta"))
  clrLn (1)

  menuState_2 ()

def menuState_2 ():
  menuOpt = input (colored ("Select: ", "green"))
  clrLn (1)

  if menuOpt == "a" or menuOpt == "A":
    print (colored ("You selected: ", "green"), colored (menuOpt, "white"))
    print ()
    input (colored ("[Press any key to proceed]", "magenta"))
    clrLn (11)
    calculateAverage ()

  elif menuOpt == "x" or menuOpt == "X":
    close ()

  else:
    print (colored ("  Note: Option invaled", "red"))
    print ()
    input (colored ("[Press any key to reselect]"))
    clrLn (3)
    
    menuState_2 ()
    
def calculateAverage ():
  print ()
  print (colored ("                **** Calculate Average ****                ", "blue", attrs= ["bold"]))
  print ()
  input (colored ("[Press any key to proceed]", "magenta"))
  clrLn (1)
  print (colored (" * Instructions:                      * ", "cyan"))
  print ()
  print (colored ("    1. Enter a list of numbers via the keyboard."))
  print (colored ("    2. Numbers should be separated by commas."))
  print (colored ("    3. Confirm your choice of numbers or reselect."))
  print (colored ("    4. The Average is calculated automatically."))
  print (colored ("    5. View results"))
  print (colored ("    6. Exit or start over."))
  print ()
  input (colored ("[Press any key to proceed]", "magenta"))
  clrLn (1)
  print(colored ("                                                    ", "white", attrs= ["underline"]))

  calculateAverageState_2 ()

def calculateAverageState_2 ():
  print ()
  inputStr = input (colored ("Enter numbers: ", "green"))
  clrLn (1)

  valsStrs = inputStr.split (",", -1)
  valsAmt = len (valsStrs)
  isNum = []
  valsFlts = []
  
  for x in valsStrs:
    isNum.append (x.isnumeric ())

  if False in isNum:
      print (colored (" Note: Only numbers can be selected", "red"))
      print ()
      input (colored ("[Press any key to reselect]", "magenta"))
      clrLn (4) 
      calculateAverageState_2 ()
  else:
    if valsAmt  < 2:
      print (colored (" Note: More than 1 number must be entered.", "red"))
      print ()
      input (colored ("[Press any key to proceed]", "magenta"))
      clrLn (4)
      calculateAverageState_2 ()
    else:
      print (colored ("Selected numbers: ", "green")
      )
      print ()

      for x in valsStrs:
        valsFlts.append (float (x))
        print ("    ", valsFlts[valsStrs.index (x)])
      print ()
      print (colored ("  Options: ", "cyan"))
      print ()
      print (colored ("    p = Proceed"))
      print (colored ("    e = Enter new numbers"))
      print (colored ("    x = Exit"))
        
      calculateAverageState_3 (valsFlts)

def calculateAverageState_3 (vals):
  print ()
  strCals = input (colored ("Select: "))
  clrLn (1)

  if strCals == "p" or strCals == "P":
    print ("p")
  elif strCals == "e" or strCals == "E":
    print ("e")
  elif strCals == "x" or strCals == "X":
    print ("x")
  else:
    print ("z")

def clrSc ():
  os.system('cls' if os.name == 'nt' else 'clear')    
def clrLn (amt):
  for x in range (amt):
    print ("\033[A                                                    \033[A")

def close ():
  print ()
  print (colored ("Goodbye...", "cyan"))
  print ()
  input (colored ("[Press any key to proceed]", "magenta"))
  clrSc ()
  exit ()

collectVals ()

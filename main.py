#imports
import os
from termcolor import  colored #pip3 import termcolor
import time
#name function collectVals
def collectVals ():
  header () #1
  body () #2
#programne header
def header ():
  clrSc ()
  print ()
  print (colored ("                **** CollectVals ****                ", "blue", attrs= ["bold"]))
  print ()
  input (colored ("[Press enter key to proceed]", "magenta"))
  clrLn (1)
  print (colored (" *    Description: Calculate the average          * \n        of any list of numbers", "cyan"))
  print ()
  print (colored ("                                                    ", "white", attrs= ["underline"]))
  input (colored ("[Press enter key to proceed]", "magenta"))
  clrLn (1)
#body of programne
def body ():
 menu () #3
#menu screen
def menu ():
  print ()
  print (colored ("                **** Menu ****                 ", "blue", attrs= ["bold"]))
  input (colored ("[Press enter key to proceed]", "magenta"))
  clrLn (1)
  print ()
  print (colored ("  Options: ", "cyan"))
  print ()
  print (colored ("    a = Calculate Average"))
  print (colored ("    x = exit"))
  print ()
  input (colored ("[Press enter key to proceed]", "magenta"))
  clrLn (1)
  menuState_2 () #4
#options in menu
def menuState_2 ():
  #collect a list of numbers from user via keyboard.
  print ()
  menuOpt = input (colored ("Select: ", "green"))
  clrLn (1)
  if menuOpt == "a" or menuOpt == "A":
    print (colored ("You selected: ", "green"), colored (menuOpt, "white"))
    print ()
    input (colored ("[Press enter key to proceed]", "magenta"))
    clrLn (12)
    calculateAverage () #5
  elif menuOpt == "x" or menuOpt == "X":
    print (colored ("You selected: ", "green"), colored (menuOpt, "white"))
    print ()
    input (colored ("[Press enter key to proceed]", "magenta"))
    clrLn (12)
    close () #5
  else:
    print (colored ("  Note: Option invaled", "red"))
    print ()
    input (colored ("[Press enter key to reselect]", "magenta"))
    clrLn (4)
    menuState_2 () #5
#calculating average screen 
def calculateAverage ():
  print ()
  print (colored ("                **** Calculate Average ****                ", "blue", attrs= ["bold"]))
  print ()
  input (colored ("[Press enter key to proceed]", "magenta"))
  clrLn (1)
  print (colored (" * Instructions:                                  * ", "cyan"))
  print ()
  print (colored ("    1. Enter a list of numbers via the keyboard."))
  print (colored ("    2. Numbers should be separated by commas."))
  print (colored ("    3. Confirm your choice of numbers or reselect."))
  print (colored ("    4. The Average is calculated automatically."))
  print (colored ("    5. View results"))
  print (colored ("    6. Exit or start over."))
  print ()
  input (colored ("[Press enter key to proceed]", "magenta"))
  clrLn (1)
  print(colored ("                                                    ", "white", attrs= ["underline"]))
  calculateAverageState_2 () #6
#collecting list of numbers from user
def calculateAverageState_2 ():
  print ()
  inputStr = input (colored ("Enter numbers: ", "green"))
  clrLn (1)
  inputStr = inputStr.replace (" ", "")
  valsStrs = inputStr.split (",", -1)
  valsAmt = len (valsStrs)
  isNum = []
  valsFlts = []
  for x in valsStrs:
    isNum.append (x.isnumeric ())
  if False in isNum:
      print (colored (" Note: Only numbers can be selected", "red"))
      print ()
      input (colored ("[Press enter key to reselect]", "magenta"))
      clrLn (4) 
      calculateAverageState_2 () #7
  else:
    if valsAmt  < 2:
      print (colored (" Note: More than 1 number must be entered.", "red"))
      print ()
      input (colored ("[Press enter key to proceed]", "magenta"))
      clrLn (4)
      calculateAverageState_2 () #7
    else:
      print (colored ("Selected numbers: ", "green"))
      print ()
      print ("  ", inputStr)
      for x in valsStrs:
        valsFlts.append (float (x))
      input (colored ("[Press enter key to proceed]", "magenta"))
      clrLn (1)   
      print ()
      print (colored ("  Options: ", "cyan"))
      print ()
      print (colored ("    p = Proceed"))
      print (colored ("    e = Enter new numbers"))
      print (colored ("    m = Return to Menu"))
      print (colored ("    x = Exit"))
      print ()
      input (colored ("[Press enter key to proceed]", "magenta"))
      clrLn (1)    
      calculateAverageState_3 (valsFlts, valsAmt, inputStr) #7
#options after selecting list of numbers
def calculateAverageState_3 (vals, amt, strs):
  print ()
  strCals = input (colored ("Select: ", "magenta"))
  clrLn (1)
  if strCals == "p" or strCals == "P":   
    print (colored ("You selected: ", "green"), colored (strCals, "white"))
    print ()
    input (colored ("[Press enter key to proceed]", "magenta"))
    clrLn (27)
    calculateAverageState_4 (vals, amt, strs) #8
  elif strCals == "e" or strCals == "E":
    print (colored ("You selected: ", "green"), colored (strCals, "white"))
    print ()
    input (colored ("[Press enter key to proceed]", "magenta"))
    clrLn (16)
    calculateAverageState_2 () #8
  elif strCals == "m" or strCals == "M":
    print (colored ("You selected: ", "green"), colored (strCals, "white"))
    print ()
    input (colored ("[Press enter key to proceed]", "magenta"))
    clrLn (29)
    menu () #8
  elif strCals == "x" or strCals == "X":
    print (colored ("You selected:", "green"), colored (strCals, "white"))
    print ()
    input (colored ("[Press enter key to proceed]", "magenta"))
    clrLn (29)
    close () #8
  else:
    print (colored (' Note: Option invalid', "red"))
    print ()
    input (colored ("[Press enter key to reselect]", "magenta"))
    clrLn (4)
    calculateAverageState_3 (vals, amt, strs) #8
#math to calculate average done here
def calculateAverageState_4 (vals, amt, strs):
  valsSum = sum (vals)
  #calculate the average of the given list of numbers
  valsAvg = valsSum / amt
  valsAbvAvg = []
  abvAvgStr = ""
  for x in vals:
    if x > valsAvg:
      valsAbvAvg.append (x)
  abvAvgStr = ",".join(str(element) for element in valsAbvAvg)
  #calculate how many numbers from 
  #the list are above the average
  valsAbvAvgAmt = len (valsAbvAvg)
  reviewResult (vals, amt, valsAvg, valsAbvAvgAmt, valsAbvAvg, strs, abvAvgStr) #9
#output results screen
def reviewResult (vals, amt, avg, abvAvg, numsAbvAvg, strs, abvAvgStr):
  print ()
  print (colored (" Results: ", "cyan"))
  input (colored ("[Press enter key to proceed]", "magenta"))
  clrLn (1)
  print ()
  print (colored ("    Numbers: ", "cyan"))
  input (colored ("[Press enter key to proceed]", "magenta"))
  clrLn (1)
  print("    ", strs)
  input (colored ("[Press enter key to proceed]", "magenta"))
  clrLn (1)
  print ()
  print (colored ("    Average: ", "cyan"), colored (avg, "white"))
  input (colored ("[Press enter key to proceed]", "magenta"))
  clrLn (1)
  print ()
  print (colored ("    Numbers above Average (amt): ","cyan"), colored (abvAvg, "white"))
  input (colored ("[Press enter key to proceed]", "magenta"))
  clrLn (1)
  print ()
  print (colored ("    Numbers above Average:", "cyan"))
  input (colored ("[Press any key to proceed]", "magenta"))
  clrLn (1)
  print ("    ", abvAvgStr)
  input (colored ("[Press enter key to proceed]", "magenta"))
  clrLn (1)
  print ()
  print (colored ("  Options: ", "cyan"))
  print ()
  print (colored ("    m = return to menu"))
  print (colored ("    x = exit"))
  input (colored ("[Press enter key to proceed]", "magenta"))
  clrLn (1)
  ending (amt) #10
#options after results are shown
def ending (amt):
  print ()
  endOpt = input (colored (" Select: ", "green"))
  clrLn (1)
  if endOpt == "m" or endOpt == "M":
    print (colored (" You selected: ", "green"), colored (endOpt))
    print ()
    input (colored ("[Press enter key to proceed]", "magenta"))
    clrLn (23)
    menu () #11
  elif endOpt == "x" or endOpt == "X":
    print (colored (" You selected ", "green"), colored (endOpt, "white"))
    print ()
    input (colored ("[Press enter key to proceed]", "magenta"))
    clrLn (23)
    close () #11
  else:
    print (colored (" Note: Option invalid", "red"))
    print ()
    input (colored ("[Press enter key to reselect]", "magenta"))
    clrLn (4)
    ending (amt) #11
#clear the terminal screen
def clrSc ():
  os.system('cls' if os.name == 'nt' else 'clear')
#clear lines in the terminal  
def clrLn (amt):
  for x in range (amt):
    print ("\033[A                                                    \033[A")
#exit programme
def close ():
  print ()
  print (colored ("Goodbye...", "cyan"))
  print ()
  input (colored ("[Press enter key to proceed]", "magenta"))
  clrSc ()
  exit ()
#entry point
collectVals () #0

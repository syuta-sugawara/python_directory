#naomi barrel

import random
gameWord=''
wordState=''

def importWord () :
            
      global gameWord
      wordStrings=""
      wordsLists=[]

      fin =open('/Users/sugawarasyuta/Desktop/DeAnza/python/python_directory/word.txt','r')
     
      for words in fin:
       
            wordStrings+=words

      wordsLists = wordStrings.split ('\n')

      gameWord=wordsLists[random.randint(0 ,len(wordsLists)-1)]

      print(gameWord)

def creatingWordState():
      global gameWord
      global wordState
      for x in range(len(gameWord)):
            wordState +='_ '
      
useWordArray=[]
def removeSpace(wordArray):
      global useWordArray
      for u in wordArray:
            if u !=' ':
                  useWordArray+=u
      

def playHangman():
      global wordState
      global useWordArray
      
      wordArray=list(wordState)
      removeSpace(wordArray)
      
      correctGuess=0
      attemptsLeft = 6
      usedWord=[]
      
      while attemptsLeft > 0 and correctGuess < len(gameWord) :
            
            print ( '\n'+wordState +' (  '+ str(attemptsLeft) +' error-attempts left)'+'\n')

            serchValue=input('Guess a letter : ')
            
            while len(serchValue)>=2:
                  print('please enter the one character (you might put spaces.):')
                  serchValue=input('Guess a letter : ')

            usedWord+=serchValue
            
            usedWordCount=0
            for x in range(len(usedWord)) :

                  if usedWord[x] == serchValue:
                        usedWordCount+=1
                        
            if usedWordCount  >= 2 :
                  print('\n you have already guessed the letter. \n')
                  continue


            findID = -1
            for i  in  range(len(gameWord)):

                  if  gameWord[i] ==  serchValue:
                        findID=i
                        useWordArray[i] = serchValue
                        correctGuess +=1                              
                 
            wordState=''
            for x in useWordArray :
                  wordState+=x

            if findID == -1 :
                  print('\n there is no '  + serchValue )
                        
            if findID ==  -1 and usedWordCount < 2  :
                  attemptsLeft-=1

      if correctGuess == len(gameWord) :
            print('\n Congratulation! You can guess all of them !')
            print('\n the number of letters you can guess correctly is ' + str(correctGuess) )
            print('\n the word is '+ gameWord +'. (you got it after picking '+str(len(gameWord))+' letters ) ')

      if attemptsLeft  == 0 :
            print('\n the number of letters you can guess correctly is ' + str(correctGuess) )
            print('\n the word is '+ gameWord + '. Good luck next time.')

print ('Welcome to Hangman!')


importWord()
creatingWordState()
playHangman()

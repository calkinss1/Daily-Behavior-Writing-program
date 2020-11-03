Name=input('Student Name:')

while True:
        try:
            Meals=int(input('Number of Meals(between 0-3):'))
        except ValueError:
                print ('Sorry your response must be a value between 0-3')
                continue
        else:
            break

        while True:
            if 0<= Meals <=3:
                break
            print('not an appropriate choice please select a number between 0-3')
            #if Meals== 3:
            #Meals= 'ate all 3 meals today'
            #elif Meals==2:
            #Meals='ate 2 meals today'
            #elif Meals==1:
            #Meals='ate only 1 meal today'
            #elif Meals==0:
            #Meals='did not eat any meals today'

print (Meals)
#mornteeth=input('Did student brush their teeth this morning? y or n:')
#if mornteeth== 'y':
    #mornteeth='he brushed his teeth this morning'
#elif mornteeth== 'n':
    #mornteeth='he did not brush his teeth this morning'
#else:
    #print(' invalid input, please enter y or n')

#amshower=input('Did the student shower this morning? y or n:')
#if amshower=='y':
    #amshower='He showered this morning'
#elif amshower=='n':
    #amshower= input('Did the student shower this evening? y or n:' )
    #if amshower=='y':
        #amshower='He showered this evening'

#school=int(input('How many School checks(0-4):'))
#if school==4:
    #school='He went to school and participated for the entire duration'
#elif school==3:
    #school='He went to school and participated for most of the day'
#elif school==2:
    #school='He went to school and participated for half of the schoolday'
#elif school==1:
    #school='He was briefly at school and minimally participated'
#elif school==0:
    #school='He did not go to school today'
#print(Name,Meals+','+mornteeth+'.',amshower)
#print(school+'.')

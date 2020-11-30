def daily():
    Name=input('Student Name:')

    while True:
            try:
                Meals=int(input('Number of Meals(between 0-3):'))
                if 0<= Meals <=3:
                    break
                raise Exception()
            except:
                print('not an appropriate choice please select a number between 0-3')
    if Meals== 3:
        Meals= 'ate all 3 meals today'
    elif Meals==2:
        Meals='ate 2 meals today'
    elif Meals==1:
        Meals='ate only 1 meal today'
    elif Meals==0:
        Meals='did not eat any meals today'

    while True:
        mornteeth=input('Did student brush their teeth this morning? y or n:')
        if  mornteeth not in ('y','n'):
            print('not an appropriate choice please enter y or n ')
            continue
        else:
            break
    if mornteeth== 'y':
        mornteeth='he brushed his teeth this morning'
    elif mornteeth== 'n':
        mornteeth='he did not brush his teeth this morning'

    while True:
        amshower=input('Did the student shower this morning? y or n:')
        if amshower not in ('y','n'):
            print('not and appropriate choice please enter y or n')
            continue
        else:
            break
    if amshower=='y':
        amshower='He showered this morning'
    elif amshower=='n':
        while True:
            amshower= input('Did the student shower this evening? y or n:' )
            if amshower not in ('y','n'):
                continue
            else:
                break
        if amshower=='y':
            amshower='He showered this evening'
        if amshower=='n':
            amshower=='He did not shower today'

    while True:

        bedroomclean=input('Did they clean their room today? y or n:')
        if bedroomclean not in ('y','n'):
            print('not and appropriate choice please enter y or n')
            continue
        else:
            break
    if bedroomclean=='y':
        bedroomclean='He cleaned his bedroom today'
    elif bedroomclean=='n':
        bedroomclean='He did not clean his bedroom today'

    while True:
            try:
                school=int(input('How many School checks?(0-4):'))
                if 0<= school <=4:
                    break
                raise Exception()
            except:
                print('not an appropriate choice please select a number between 0-4')

    if school==4:
        school='He went to school and participated for the entire duration'
    elif school==3:
        school='He went to school and participated for most of the day'
    elif school==2:
        school='He went to school and participated for half of the schoolday'
    elif school==1:
        school='He was briefly at school and minimally participated'
    elif school==0:
        school='He did not go to school today'

    activity=''

    while True:
        largemuscle=input('Did they complete a large muscle activity for 1 hour today? y or n:')
        if largemuscle not in ('y','n'):
            print('not and appropriate choice please enter y or n')
            continue
        else:
            break
    if largemuscle=='y':
        largemuscle='He completed his large muscle today, for large muscle he'
        activity=input('What activity did they do for large muscle?:' )

    elif largemuscle=='n':
        largemuscle='He did not complete a large muscle activity today'
    #activity=input('What activity did they do for large muscle?:' )

    while True:
        chore=input('Did they complete a chore today? y or n:')
        if chore not in ('y','n'):
            print('not an appropriate response please enter y or n')
            continue
        else:
            break
    comchore=''
    if chore=='y':
        comchore=input('What chore did they complete today?:')
        chore='He completed his chore today. For his chore he'
    elif chore=='n':
        chore='He did not complete his chore today'

    while True:
        media=input('Was today a media free day? y or n:')
        if media not in('y', 'n'):
            print('not an appropriate response please enter y or n')
            continue
        else:
            break
    if media=='n':
        while True:
            media=input('Did they get their media today? y or n:')
            if media not in('y', 'n'):
                print('not an appropriate response please enter y or n')
                continue
            else:
                break
        if media=='y':
            media='He got his media today and spent time after dinner playing on it'
        elif media=='n':
                media=''
    elif media=='y':
        media='Today was a media free day and he did not recieve media today'

    while True:
        add=input('Would you like to add additional behaviors? y or n:')
        if add not in('y','n'):
            continue
        else:
            break
    if add=='y':
        add=input('Please enter additional behaviors(paragraphs):')
    elif add=='n':
        add=''

    print(Name,Meals+','+mornteeth+'.',amshower+'.',bedroomclean+'.',school+'.', largemuscle,activity+'.',chore,comchore+'.', media+'.', add)

while True:
    daily()
    if input('Do another daily? y or n:').strip() !='y':
        break

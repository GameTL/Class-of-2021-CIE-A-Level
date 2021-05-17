
def DisplayIntro():
    print('Hello Fellow Traveller')
    print('Are you are ready to feel Maximum Pain?')

    print('(y for Yes), Anything or No')
    MyYesOrNo = input() 
    if MyYesOrNo == 'y':
        print('OK Then then Boi-yo, let\'s go')
    else:
        print('Fine Boi-yo, Go back to your country Gringo')

    print('But first how old are you? cuz this game contain butts')
    Age = int(input('What\'s your age?'))
    if Age < 18:
        print('Ok, let\'s play bro!')  


def sayGoodbye():
    print('Goodbye! Boi-yo')

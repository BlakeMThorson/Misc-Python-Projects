import random
import pickle


#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------   
def setUpRace():
    with open('racers.pickle', 'rb') as handle:
        animals = pickle.load(handle)
    
    #select 4 random animals
    racers = []
    numbers = random.sample(range(0, 9), 4)
    animalList = list(animals.keys())
    
    for i in numbers:
        x = animalList[i]
        racers.append( [x, animals[x]])
    return racers

#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------   
def chooseWinner(racers):
    winners = random.sample(range(0, 4), 4)
    places = {
        "first" : racers[winners[0]],
        "second" : racers[winners[1]],
        "third" : racers[winners[2]],
        "fourth" : racers[winners[3]]
        }
    return places

#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------   
def adjustStats(places):
    with open('racers.pickle', 'rb') as handle:
        animals = pickle.load(handle)
    #adjust rankings
    animals[ places[ "first"][0] ]["wins"] += 1
    animals[ places[ "second"][0] ]["losses"] += 1
    animals[ places[ "third" ][0] ]["losses"] += 1
    animals[ places[ "fourth"][0] ]["losses"] += 1
    with open('racers.pickle', 'wb') as handle:
        pickle.dump(animals, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    return animals

def fullRace():
    x = setUpRace()
    y = chooseWinner(x)
    adjustStats(y)
    return y

#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#------------------   LOTTERY MANAGER ---------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------
#WORKING---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------



def twoToOneCard(): # $10
    x = ['🍏', '🍎', '🍐', '🍊', '🍋', '🍌', '🍉', '🍇', '🍓', '🍈', '🍒', '🍑', '🍍', '🥝', '🍅', '🍆', '🥑',  '🥒',  '🌶', '🌽', '🥕', '🥔', '🍠', '🥐', '🍞', '🥖',  '🧀', '🥚', '🍳', '🥞', '🥓',  '🍗', '🍖', '🌭', '🍔', '🍟', '🍕',  '🥙', '🌮', '🌯', '🥗', '🥘',  '🍝', '🍜', '🍲', '🍛', '🍣', '🍱',  '🍤', '🍙', '🍚', '🍘', '🍥',  '🍢', '🍡', '🍧', '🍨', '🍦',  '🍰', '🎂', '🍮', '🍭', '🍬', '🍫', '🍿', '🍩', '🍪', '🌰', '🥜', '🍯', '🥛', '🍼', '☕️', '🍵', '🍶', '🍺', '🍻', '🥂', '🍷', '🥃', '🍸', '🍹', '🍾', '🥄', '🍴', '🍽']

    isWinner = bool(random.getrandbits(1))
    if isWinner:
        winner = random.randint(0,len(x)-1)
        cardPart = random.sample(range(0, len(x)-1), 9)
        toReplace = random.sample(range(0, 8), 3)
        card = []
        for i in cardPart:
            card.append("||{}||".format(x[i]))
        
        for i in toReplace:
            card[i] = "||{}||".format(x[winner])        
        
        return ["WINNER",card]
    else:
        cardPart = random.sample(range(0, len(x)-1), 9)
        card = []
        for i in cardPart:
            card.append("||{}||".format(x[i]))
        fuck = random.randint(0,len(card)-1)
        
        you = random.randint(0,len(card)-1)
        
        card[fuck] = card[you]
        
        
        return ["LOSER",card]
    
def threeToOneCard(): # $50
    x = ['🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼', '🐨', '🐯', '🦁', '🐮', '🐷', '🐽', '🐸', '🐵', '🙈', '🙉', '🙊', '🐒', '🐔', '🐧', '🐦', '🐤', '🐣', '🐥', '🦆', '🦅', '🦉', '🦇', '🐺', '🐗', '🐴', '🦄', '🐝', '🐛', '🦋', '🐌', '🐚', '🐞', '🐜', '🕷', '🕸', '🦂','🐢', '🐍', '🦎',  '🐙', '🦑', '🦐', '🦀', '🐡', '🐠', '🐟', '🐬', '🐳', '🐋', '🦈', '🐊', '🐅', '🐆',  '🦍', '🐘', '🦏',  '🐪', '🐫', '🐃', '🐂', '🐄', '🐎', '🐖', '🐏', '🐑', '🐐', '🦌', '🐕', '🐩', '🐈', '🐓', '🦃', '🕊', '🐇', '🐁', '🐀', '🐿']


    isWinner = random.randint(1,3)
    #decide if they win
    if isWinner == 1:
        isWinner = True
    else:
        isWinner = False
    if isWinner:
        winner = random.randint(0,len(x)-1)
        cardPart = random.sample(range(0, len(x)-1), 25)
        toReplace = random.sample(range(0, 24), 5)
        card = []
        for i in cardPart:
            card.append("||{}||".format(x[i]))
        
        for i in toReplace:
            card[i] = "||{}||".format(x[winner])        
        
        return ["WINNER",card]
    else:
        cardPart = random.sample(range(0, len(x)-1), 25)
        card = []
        for i in cardPart:
            card.append("||{}||".format(x[i]))
        
        fuck = random.randint(0,len(card)-1)
        
        you = random.randint(0,len(card)-1)
        

        too = random.randint(0,len(card)-1)
                
        
        card[fuck] = card[you]
        
        card[too] = card[you]
        
        return ["LOSER",card]



def lottery(card):
    lottoNumbers = random.sample(range(1, 70), 10)
    if len(card) != len(lottoNumbers):
        return "card isn't correct length"
    payout = 0
    correct = 0
    for i in range(len(card)):
        if lottoNumbers[i] == card[i]:
            correct += 1
            payout += 10**(1+correct)
    
    return [payout, card, lottoNumbers]
        
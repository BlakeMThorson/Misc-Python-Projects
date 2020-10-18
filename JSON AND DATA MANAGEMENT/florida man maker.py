import pickle
import markovify

def makeF():
    corpus = open("florida2.txt").read()
    
    text_model = markovify.NewlineText(corpus, state_size=2)
    model_json = text_model.to_json()
    
    with open('floridaMarkov.pickle', 'wb') as handle:
        pickle.dump(toReturn, handle, protocol=pickle.HIGHEST_PROTOCOL)      

def getF():
    with open('floridaMarkov.pickle', 'rb') as gator:
        markovModel = pickle.load(gator)  
        floridaMarkov = markovify.Text.from_json(markovModel)    
    return floridaMarkov.make_sentence()
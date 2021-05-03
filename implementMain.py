import random
import json
import torch
from model import NeuralNet
from tokenizationAndStemming import BagOfWords, tokenize
from voice import listener


# Tokenize, stem the spoken word and shape them to fit on the model
def tokenizeAndStemSpoken(sentence, allWords):
    sentence = tokenize(sentence)
    x = BagOfWords(sentence, allWords)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x)
    return x


# open the intents file
def loadIntent():
    with open("intents.json", "r") as f:
        intents = json.load(f)
    return intents

# Load the creadential saved during training


def loadModel():
    FILE = "data.pth"
    data = torch.load(FILE)

    # load all the saved values
    inputSize = data["input_size"]
    outputSize = data["output_size"]
    hiddenSize = data["hidden_size"]
    allWords = data["allWords_size"]
    tags = data["tags"]
    modelState = data["modelState"]

    model = NeuralNet(inputSize, hiddenSize, outputSize)
    return model, modelState, allWords, tags

# Listen to the next Html tag


def listenTag(sentence, botName):
    # load the saved model
    model, modelState, allWords, tags = loadModel()

    # load the statedictionary
    model.load_state_dict(modelState)
    model.eval()

    # load intentsfile
    intents = loadIntent()

    # tokenize find BOG predict the class for new sentence
    x = tokenizeAndStemSpoken(sentence, allWords)

    # find the predicted output
    output = model(x)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    # apply softmax to find probability of predicted class
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    # loop for pattern to see if any pattern matches
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tags"]:
                # {random.choice(intent['tags'])}
                print(f"{botName}: {tag}")
                return tag
    else:
        print(f"{botName}: I do not understand...")

# Listen to the attributes assigned to each tag


def listenAttribute():
    pass


# create a html file according to the commands
def createHtml():
    pass


# dictionary to hold the command given
commandTags = {
    "tags": []
}


def main():
    # create the bot
    botName = "Jony"
    print("Let's chat! type quit to exit ")

    # listen to user, predict the command, and gve appropriate response
    while True:
        # listen to voice command
        sentence = listener()

        # check if listener return an error
        if 'error!' in sentence:
            print(f"{botName}: I do not understand...")

        else:
            print(f'you: {sentence}')  # sentence =input('you:')
            if sentence == 'quit':
                break
            # if command is understandable synthesize the tag
            tag = listenTag(sentence, botName)

            # For each tag there are attributes listen to the attributes
            attribute = listenAttribute()

            # After tag and attributes are clear make appropriate data to pass to react
            data = {
                "element": tag,
                "innerHtml": "this"
            }
            # save the command to dictionary
            commandTags["tags"].append(data)

    print("commandTags:", commandTags)
    # now create a html file according to the command tag
    # createHtml(commandTags)
    # render the page


if __name__ == "__main__":
    main()

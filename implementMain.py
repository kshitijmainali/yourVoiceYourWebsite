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
    with open("attributes.json", "r") as f:
        attributes = json.load(f)
    return intents, attributes

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

# synthesize next Html tag or attribute provided


def listenTag(sentence, botName, recType):
    # load the saved model
    model, modelState, allWords, tags = loadModel()

    # load the statedictionary
    model.load_state_dict(modelState)
    model.eval()

    # load intentsfile
    intents, attributes = loadIntent()

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
        # now we have to decide are we looking for tag or attribute
        if recType == 1:
            for intent in intents['intents']:
                if tag == intent["tags"]:
                    return tag
        else:
            for attribute in attributes['attributes']:
                if tag == attribute['attr']:
                    return tag
    else:
        print(f"{botName}: I do not understand...")

# create a html file according to the commands


def createHtml():
    pass


# listen to user for tag or atrribute
def listenUser(recType):
    # dont be confuse this while is for the case when tag is not recognized
    while True:
        # create the bot
        botName = "Jony"
        if recType == 1:
            print("Let's hear tag!")
        else:
            print("Let's hear atriibute! ")

        # listen to voice command
        sentence = listener()
        print('I hear', sentence)

        # check if listener return an error
        if 'error!' in sentence:
            print(f"{botName}: I do not understand...")
        elif 'quit' in sentence:
            return 'quit'
        else:
            print(f'you: {sentence}')
            # if command is understandable synthesize the tag
            tag = listenTag(sentence, botName, recType)
            print(f'jony: {tag}')

            return tag

# As some one give an atribute there should be a value associated


def listenValue(attribute):
    while True:
        print(f'jony: speak {attribute} value')
        value = listener()
        if 'error!' in value:
            print(f"jony: I don't understand")
        else:
            return value


# dictionary to hold the command given
commandTags = {
    "tags": []
}


def main():
    # listen to user, predict the command, and gve appropriate response
    while True:
        # empty lists to contain the atriibute and
        tag = []
        attribute = []

        # listen the tag
        tag = listenUser(1)
        if tag == 'quit':
            break
        # For each tag there can be multiple attributes listen to the attributes
        while True:
            listenedAttribute = listenUser(2)
            if listenedAttribute == 'quit':
                break
            if listenedAttribute is not None:
                value = listenValue(listenedAttribute)
                attrValue = {
                    "attr": listenedAttribute,
                    "value": value
                }
                attribute.append(attrValue)
       # After tag and attributes are clear make appropriate data to pass to react
        data = {
            "element": tag,
            "attributes": attribute
        }
        # save the command to dictionary
        commandTags["tags"].append(data)

    print("commandTags:", commandTags)
    # now create a html file according to the command tag
    # createHtml(commandTags)
    # render the page


if __name__ == "__main__":
    main()

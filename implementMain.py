import random
import json
import torch
from model import NeuralNet
from tokenizationAndStemming import BagOfWords, tokenize
from voice import listener

from specialHandlers import handleSrc, handleTable, handleList, handleSelect, listenType

# Tokenize, stem the spoken word and shape them to fit on the model


def tokenizeAndStemSpoken(sentence, allWords):
    sentence = tokenize(sentence)
    x = BagOfWords(sentence, allWords)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x)
    return x


# open the intents file
with open("intents.json", "r") as f:
    intents = json.load(f)
with open("attributes.json", "r") as f:
    attributes = json.load(f)

# Load the creadential saved during training

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
# synthesize next Html tag or attribute provided


def synthesizeTag(sentence, botName, recType):
    # load the statedictionary
    model.load_state_dict(modelState)
    model.eval()

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
    if prob.item() > 0.85:
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
        print('Jony: I hear>', sentence)

        # see if the user say quit to end the tag
        if 'quit' in sentence:
            return 'quit'
        elif 'finish' in sentence:
            return 'quit'
        else:
            print(f'you: {sentence}')
            # if command is understandable synthesize the tag

            tag = synthesizeTag(sentence, botName, recType)
            print(f'jony: {tag}')
            if tag != None:
                return tag


def listenTag():
     # listen the tag
    innerElement = []
    tag = listenUser(1)
    # we have to handle some special tag like tabe,list,inputoption etc
    if tag == 'table':
        innerElement = handleTable()
    if tag == 'ol' or tag == 'ul':
        innerElement = handleList()
    if tag == "form":
        innerElement = handleForm()
    if tag == 'select':
        innerElement = handleSelect()
    if tag == 'nav':
        innerElement = handleNav()

    return tag, innerElement

# it listen to the attribute for special tag


def listenAttribute(tag):
    attribute = []
    # For each tag there can be multiple attributes listen to the attributes
    while True:
        listenedAttribute = listenUser(2)
        if listenedAttribute is not None:
            value = []
            if 'quit' in listenedAttribute:
                return attribute
            # we have to handle some special attribute like src,values of option
            if listenedAttribute == "src":
                value = handleSrc()
            if listenAttribute == "type":
                value = listenType()
            else:
                print(f'jony: speak {listenedAttribute} value')
                value = listener()
            attrValue = {
                "attr": listenedAttribute,
                "value": value
            }
            attribute.append(attrValue)


def completeListener():
    # empty lists to contain the atriibute and
    tag = []
    attribute = []
    innerElement = []
    innerText = []

    # listen to various tag and their inner nested tags
    tag, innerElement = listenTag()

    # some tag like img,vedio,input,href need atrribute like src,type,href
    mustHaveAtrribute = ['img', 'input', 'vedio', 'a']

    # listen to associated attribute
    if tag in mustHaveAtrribute:
        attribute = listenAttribute(tag)

    # now we have to listen to the innertext if there is any
    print(f'is there any inner text associated with {tag} ?')
    openion = listener()
    if 'yes' in openion:
        innerText = listener()

    # After tag and attributes are clear make appropriate data to pass to react
    data = {
        "element": tag,
        "innerText": innerText,
        "attributes": attribute,
        "innerElement": innerElement
    }
    return data


# Notice here these two special handlers are here because we need to listen to complete tag
# again and doing it in special handlers create importing problem

def handleForm():
    tags = []
    while True:
        tag = completeListener()
        tags.append(tag)
        print('till now ', tags)
        print('is there more tag inside form?')
        openion = listener()
        if 'yes' not in openion:
            return tags


def handleNav():
    tags = []
    while True:
        tag = completeListener()
        tags.append(tag)
        print('is there more <a> tags? yes to continue')
        openion = listener()
        if 'yes' not in openion:
            return tags


# dictionary to hold the command given
commandTags = {
    "tags": []
}


def main():
    # listen to user, predict the command, and gve appropriate response
    data = completeListener()

    # save the command to dictionary
    commandTags["tags"].append(data)

    print("commandTags:", commandTags)
    # now create a html file according to the command tag
    # createHtml(commandTags)
    # render the page


if __name__ == "__main__":
    main()

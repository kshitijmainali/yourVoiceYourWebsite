from pathlib import Path
from voice import listener
#from implementMain import completeListener


def handleSrc():
    while True:
        print(f'jony: speak src value')
        spoken = listener()
        # file are with different extension like .jpg,jpeg,mp4 we have to find appropriate file
        fileToOpen = completeFile(spoken)
        if fileToOpen:
            return fileToOpen


def handleTable():
    row = 1
    rowData = []
    while True:
        print(f'Table row {row}')
        rowInner = listenTableData(row)
        intermidiateRow = {
            "tag": 'tr',
            "innerElement": rowInner
        }
        rowData.append(intermidiateRow)
        print(rowData)
        print(f"want to add more rows? 'Yes' to continue")
        openion = listener()
        if "yes" not in openion.lower():
            return rowData
        row = row+1


def listenTableData(row):
    tag = 'td'
    values = []
    if row == 1:
        tag = 'th'
    # now to listen data in a table row we loop
    while True:
        print(f"speak {tag} data")
        spoken = listener()
        data = {
            "tag": tag,
            "value": spoken
        }
        values.append(data)
        print(f"more {tag}? speak 'Yes' to continue")
        openion = listener()
        if "yes" not in openion.lower():
            return values

# this handle specially ordered or unordered list


def handleList():
    listNo = 1
    listCollection = []
    while True:
        print(f"{listNo} list value")
        value = listener()
        list = {
            "tag": "li",
            "value": value
        }
        listCollection.append(list)
        print(f'updatedli: {listCollection} ')
        print(f"want to add more? 'Yes' to continue")
        openion = listener()
        if "yes" not in openion.lower():
            return listCollection
        listNo = listNo+1

# select tag handler


def handleSelect():
    optionNo = 1
    options = []
    while True:
        print(f"speak option {optionNo}")
        value = listener()
        option = {
            "tag": 'option',
            "value": value
        }
        options.append(option)
        print(options)
        print(f"is their more option?")
        openion = listener()
        if 'yes' not in openion.lower():
            return options
        optionNo += 1

 # this function looks for appropriate match for spekon file


def completeFile(spoken):
    dataFolder = Path(
        'C:/Users/KSHITIJ/OneDrive/Desktop/finalProject/imgAndVedio')
    extension = ['jpeg', 'jpg', 'png', 'mp4', 'mp3']
    if spoken.endswith('.*'):
        possible = dataFolder/spoken
        if possible.exists():
            return possible
    else:
        for complete in extension:
            possible = dataFolder/(spoken+'.'+complete)
            if possible.exists():
                return possible
    print("File doesn't exist")
    return None

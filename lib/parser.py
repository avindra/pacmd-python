import re

def parseList(output):
    lines = output.split('\n')
    first = lines.pop(0)

    data = {}

    currentItem = {}

    patternNewItem = re.compile('(\* )?index: (\d+)')
    patternKeyValue = re.compile('\t?([\S]+): (.+)')

    for line in lines:
        matchNewItem = patternNewItem.search(line)
        matchKeyValue = patternKeyValue.search(line)

        if matchNewItem:
            isActive = matchNewItem.group(1) == '* '
            index = matchNewItem.group(2)

            # Finalize object and reset
            data[index] = currentItem
            currentItem = {}

            if isActive:
                data['activeItem'] = index

        elif matchKeyValue:
            parsedKey = matchKeyValue.group(1)
            parsedValue = matchKeyValue.group(2)
            currentItem[parsedKey] = parsedValue


    return data
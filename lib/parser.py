import re

def parseList(output):
    lines = output.split('\n')
    first = lines.pop(0)

    if first.startswith('Unknown command'):
        raise Exception(first)

    data = {}

    currentItem = {}
    currentIndex = -1

    patternNewItem = re.compile('(\* )?index: (\d+)')
    patternKeyValue = re.compile('\t?([\S]+): (.+)')

    for line in lines:
        matchNewItem = patternNewItem.search(line)
        matchKeyValue = patternKeyValue.search(line)

        if matchNewItem:
            isActive = matchNewItem.group(1) == '* '
            index = matchNewItem.group(2)

            # Finalize object and reset
            if currentIndex != -1:
                data[currentIndex] = currentItem
                currentItem = {}

            currentIndex = index

            if isActive:
                data['activeItem'] = index

        elif matchKeyValue:
            parsedKey = matchKeyValue.group(1)
            parsedValue = matchKeyValue.group(2)
            currentItem[parsedKey] = parsedValue

    # Last item will need to be pushed manually
    data[currentIndex] = currentItem

    return data
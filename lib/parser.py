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
    patternKeyValue = re.compile('\t*([^:]+):(?: (.+))?')
    patternEnumerating = re.compile('^\tproperties:')
    patternProps = re.compile('(\S+) = "(.+)"')

    enumeratingProps = None

    lastKey = None

    for line in lines:
        matchNewItem = patternNewItem.search(line)
        matchKeyValue = patternKeyValue.search(line)
        matchEnumerating = patternEnumerating.search(line)


        if enumeratingProps:
            matchProps = patternProps.search(line)
            if matchProps:
                enumeratingProps[matchProps.group(1)] = matchProps.group(2)
                continue
            else: # reset
                currentItem['properties'] = enumeratingProps
                enumeratingProps = None

        if matchEnumerating:
            enumeratingProps = { 'device-api' : None }
        elif matchNewItem:
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
            parsedKey = matchKeyValue.group(1).strip()
            parsedValue = matchKeyValue.group(2)

            # skip until we're out of "ports".
            # not currently supported
            if lastKey == 'ports' and parsedKey != 'active port':
                continue

            lastKey = parsedKey
            currentItem[parsedKey] = parsedValue
        elif lastKey and lastKey != 'ports': # If it gets to here, we can assume its a multiline attr
            currentItem[lastKey] += re.sub('^\s+', '\n', line)

    # Last item will need to be pushed manually
    data[currentIndex] = currentItem

    return data
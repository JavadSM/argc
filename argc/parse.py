import json

# detect type of string
def detectType(data = str()):
    # int
    if data.isdigit() and detectType:
        data = int(data)
    # Float
    elif data.isdecimal and "." in data and detectType:
        data = float(data)

    # Bool
    elif data in ("True", "False") and detectType:
        if data == "True":
            data = True
        elif data == "False":
            data = False
    # Bool
    elif data in ("true", "false") and detectType:
        if data == "true":
            data = True
        elif data == "false":
            data = False

    # try to parse arrays as json
    elif "[" in data and "]" in data and detectType:
        try:
            data = json.loads(data)
        except:
            pass
        # parse dicts as json
    elif "{" in data and "}" in data and detectType:
        try:
            data = json.loads(data)
        except:
            pass
    if data == None:
        return True
    return data

def parse(args = list(), convert = True):
    isArg = lambda string: string[0] in ("-", "/")
    argv = dict()
    for count, thisA in enumerate(args):
        try:
            # if we are on the last argument
            if len(args) - count == 1 and isArg(thisA):
                argv.update({thisA: True})

            nextA = args[count + 1]
            
            if isArg(thisA) and isArg(nextA):
                argv.update({thisA: True})

            elif isArg(thisA) and not isArg(nextA):
                if convert:
                    argv.update({thisA: detectType(nextA)})
                else:
                    argv.update({thisA: nextA})
            else:
                pass

        except IndexError:
            # No more
            break
    # return parsed dict
    return argv
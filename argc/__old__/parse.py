import json

def parse(args, detectType = True):
    argv = dict()
    for c, item in enumerate(args):
        M = 0 + len(args) - c # Calculate length
    
        if item[0] in ("-", "/"):
            if args[c + 1 - M][0] in ("-", "/") and args[c + 2 - M][0] in ("-", "/"):
                argv.update({item.replace("-", "").replace("/", ""): True})
            else:
                data = str(args[c + 1])
                
                # detect type of varible
                # only is detectType is True

                # Int
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
                    
                argv.update({item.replace("-", "").replace("/", ""): data})
    return argv
### Example
```py
    # example program that takes some arguments
    # run as ${python} test.py ${args}

    import random
    from argc import argc

    __version__ = "1.0.0"
    __author__ = "Monty python"
    __package__ = "STRING RING"
    __help__ = [
        "Usage: ",
        "   import STRING_RING as sr",
        "   tone = 10",
        "   sr.RING(tone)",
        "Author: {}".format(__author__),
        "Name: %(__package__)s"
    ]


    # arguments are case sensetive but the -- and - (/ for windows) is stripped
    # so you only need the names. but that also means that -hallo,  --hallo and /hallo 
    # all triggers the hello command/option

    if __name__ == "__main__":
        args = argc() # uses sys.argv by default
        args.add("help", __help__, True) # exits on help
        args.add("version", __version__,  True)
        # supports functions (prints return value)
        args.add("func", lambda: random.randint(0, 10**10), True)
        # checks and runs commands
        args.run() 

        # code after .run
    
        # Use .get for config
        if args.get("useL"):
            print("Using L")
        else:
            print("am not using L")

        # and for custom config
        print(args.get("config", False)) # Use raw data returns None if it does not exist 
```
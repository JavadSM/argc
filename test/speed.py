import timeit
import argc
import argc._parse as parse

arguments = ["-x", "Hallo", "--num", "10.10"]
args = argc.argc(arguments, False)

args.set("-x", "--extra", "x", "an x-option", 0)
args.set("-n", "--num", "num", "Sets number", 10)
timeit.default_number
gd1 = timeit.timeit("args.generate_docs(True)", setup="from __main__ import args")
gd0 = timeit.timeit("args.generate_docs(False)", setup="from __main__ import args")

load1 = timeit.timeit("a = argc.argc(arguments, False)", setup="from __main__ import argc, arguments")
load2 = timeit.timeit("a = argc.argc(arguments, True)", setup="from __main__ import argc, arguments")

print("Generate Docs, with compact:", gd0)
print("Generate Docs, without compact:", gd1)

print("Load with detect", load2)
print("Load without detect", load1)
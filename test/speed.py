import timeit
import argc
import argc._parse as parse

arguments = ["-x", "Hallo", "--num", "10.10"]
args = argc.argc(arguments, False)

args.set("-x", "--extra", "x", "an x-option", 0)
args.set("-n", "--num", "num", "Sets number", 10)

gd1 = timeit.timeit("args.generate_docs(True)", setup="from __main__ import args", number=100)
gd0 = timeit.timeit("args.generate_docs(False)", setup="from __main__ import args", number=100)

print(gd0)
print(gd1)
import sys

patha = sys.argv[1]
pathb = sys.argv[2]
open(patha).close()
open(pathb).close()

with open(patha) as f:
    texta = f.read()
with open(pathb) as f:
    textb = f.read()

print(
    texta == textb)

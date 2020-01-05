import pegpy
peg = pegpy.grammar('sen.tpeg')
parser = pegpy.generate(peg)


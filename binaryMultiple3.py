import re

pattern_answer = re.compile(r'^(0|1(01*0)*1)*$')

# same number of even and odd position 1
# multiple of 3 even and odd 1
0*(1(00)*1)*0*|(1(00)*1)*{3}0*|(10)*{3}

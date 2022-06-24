#!/usr/bin/env python3
#Tarek Ibrahim
#2022-2-25, Cairo-Egypt
#------------------------------------------------------------------------
#Code to extract programs from the ABS html files
#to run this code over set of files use the bash find command as follows:
#       find -name '*.html' -exec py-find.py {} \;
#then turn them excutables 
#       chmod +x *.sh
#------------------------------------------------------------------------

import re
import sys
html=sys.argv[1][2:]
with open(html, encoding='latin-1') as fl:
  txt=fl.read()

#re_find=re.compile(r'PROGRAMLISTING"\n\>(#!.*\n)([\s\S]*?)\<\/PRE')
re_find=re.compile(r'PROGRAMLISTING"\n\>([\s\S]*?)\<\/PRE')
line='#{0}X{0}#'.format('='*60)
for i, match in enumerate(re_find.finditer(txt)):

  #1111111111111111111111111
  out='{}--{}.sh'.format(html,str(i+1).zfill(2))
  print(out)
  code = '#{}\n'.format(out)+\
         match.group(1)
  code = code.replace('&#62;','>').replace('&#60;','<').replace('&#38;','&').replace('&#13;','\n')
  #with open(out, 'wt') as fl:
  #  fl.write(code)
  #2222222222222222222222222

  code = '\n#<PRE>{}\n#{}\n{}\nexit\n#</PRE>'.format(line,out,match.group(1))
  code = code.replace('&#62;','>').replace('&#60;','<').replace('&#38;','&').replace('&#13;','\n')
  with open('abs-guide.sh', 'at') as fl:
    fl.write('{}'.format(code))




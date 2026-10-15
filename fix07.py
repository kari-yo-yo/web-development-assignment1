# -*- coding: utf-8 -*-
import io

p = r'C:\Users\Shang\Desktop\assignment1\.lark-slides\slide-07.xml'
s = io.open(p, encoding='utf-8').read()
s = s.replace('<rect type="rect"', '<shape type="rect"')
s = s.replace('</rect>', '</shape>')
io.open(p, 'w', encoding='utf-8').write(s)
print('patched')

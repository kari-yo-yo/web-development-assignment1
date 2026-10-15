# -*- coding: utf-8 -*-
import io

p = r'C:\Users\Shang\Desktop\assignment1\.lark-slides\slide-03.xml'
s = io.open(p, encoding='utf-8').read()

# 右侧三个标题：x 652 -> 640, width 260 -> 300, fontSize 18 -> 16
s = s.replace('topLeftX="652" topLeftY="162" width="260" height="30"', 'topLeftX="640" topLeftY="164" width="300" height="30"')
s = s.replace('topLeftX="652" topLeftY="250" width="260" height="30"', 'topLeftX="640" topLeftY="252" width="300" height="30"')
s = s.replace('topLeftX="652" topLeftY="338" width="260" height="30"', 'topLeftX="640" topLeftY="340" width="300" height="30"')
s = s.replace('fontSize="18" fontFamily="Montserrat" bold="true" color="rgba(9,51,98,1)"', 'fontSize="16" fontFamily="Montserrat" bold="true" color="rgba(9,51,98,1)"')

# 右侧说明文字 x 652 -> 640
s = s.replace('topLeftX="652" topLeftY="192"', 'topLeftX="640" topLeftY="192"')
s = s.replace('topLeftX="652" topLeftY="280"', 'topLeftX="640" topLeftY="280"')
s = s.replace('topLeftX="652" topLeftY="368"', 'topLeftX="640" topLeftY="368"')

io.open(p, 'w', encoding='utf-8').write(s)
print('patched')

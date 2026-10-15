# -*- coding: utf-8 -*-
import io

p = r'C:\Users\Shang\Desktop\assignment1\.lark-slides\slide-10.xml'
s = io.open(p, encoding='utf-8').read()

# 标题文本框缩小宽度
s = s.replace('topLeftX="80" topLeftY="44" width="700" height="56"', 'topLeftX="80" topLeftY="44" width="600" height="56"')

# 图片下移并缩小：x=80 y=56 w=240 h=469 -> x=80 y=110 w=220 h=430
s = s.replace('topLeftX="80" topLeftY="56" width="240" height="469"', 'topLeftX="80" topLeftY="110" width="220" height="430"')

# 竖线下移：x=360 y=56..525 -> x=340 y=110..520
s = s.replace('<line startX="360" startY="56" endX="360" endY="525">', '<line startX="340" startY="110" endX="340" endY="520">')

# 右侧文字从 x=410 改为 x=380
s = s.replace('topLeftX="410"', 'topLeftX="380"')

io.open(p, 'w', encoding='utf-8').write(s)
print('patched')

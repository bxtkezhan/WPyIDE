#! /usr/bin/env python3

'''
欢迎使用百晓通客栈为您制作的WPyIDE！
WPyIDE是一款为Python新人打造的Web版IDE，
现阶段除了支持一些Python3的基本功能，
还可以调用一些Javascript功能模块。
您可尝试点击蓝色按钮RUN，运行实例´ ▽ ` )ﾉ！
'''

# 引入JS库
from browser import alert, document

message = '''
Nice，干的漂亮(｡･ω･)ﾉ
'''

# 弹窗输出
alert(message)
# 终端打印
print(message)
# 页面显示
document['runButton'].text = message

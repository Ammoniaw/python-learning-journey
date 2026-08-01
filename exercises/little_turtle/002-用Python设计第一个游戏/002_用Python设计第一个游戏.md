# 用Python设计第一个游戏课后习题
## 问答题
### 0. IDLE 的交互模式和编辑器模式有什么区别？

 - 交互模式是代码即编即反馈的效果，而编辑模式下可以实现代码的保存从而实现在其他设备得以运行。

### 1. 在课堂上敲过的代码中，除了`print()` 和 `input()`，你觉得还有哪一个是 Python 的 BIF 内置函数？
- `int()`/`input()`/`dir()`

### 2. 请问 `print()` 和 `Print()` 的功能一样吗？
- 不一样，大小写不同，且如果未定义`Print()`的话，Python会报错。而`print()`则是Python的内置函数，所以无论如何都可以正常使用。

### 3. 请统计一下 Python 一共有多少个 BIF 内置函数？

- 可以使用`dir()`函数来查看内置函数、常量、异常名称；内置函数数量大约为69个

  ```python
  dir(__builtins__)
  ```

  执行结果

  ```python
  ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'PythonFinalizationError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_IncompleteInputError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
  
  ```

### 4.Tab 键除了用于缩进，你还发现它在 IDLE 中有什么特殊的功能吗？

- 自动补全变量或者函数名

### 5. 请问下面代码为什么不能正常执行？

- 异常代码

  ```python
  """ 用Python设计第一个游戏 """
  
  temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
  guess = int(temp)
  
  if guess = 8:
      print("你是小甲鱼心里的蛔虫嘛？！")
      print("哼，猜中了也没奖励！")
  else:
      print("猜错啦，小甲鱼现在心里想的是8！")
      
  print("游戏结束，不玩啦^_^")
  ```

- 修改错误

  ```python
  """ 用Python设计第一个游戏 """
  
  temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
  guess = int(temp)
  
  if guess = 8:  # 应该使用 ==(表示等于);而不是 =(赋值运算符)
      print("你是小甲鱼心里的蛔虫嘛？！")
      print("哼，猜中了也没奖励！")
  else:
      print("猜错啦，小甲鱼现在心里想的是8！")
      
  print("游戏结束，不玩啦^_^")
  ```

## 动动手

### 0. 请在 IDLE 的交互模式中，计算一年有多少秒？

- 交互模式下 

  ```python
  >>> seconds = 365 * 24 * 60 * 60
  >>> print(seconds)
  31536000
  ```

### 1. 按下面要求修改课堂中的 game.py 代码。

- 让用户输入这次数学考试的成绩。
- 如果分数是 100 分，显示：好棒，你离女神又近了一步`^_^`
- 如果分数不是 100 分，显示：小子，想要幸福，就得努力！

- game.py

  ```python
  # -*- coding: utf-8 -*-
  # @Software: PyCharm
  # @Author: Ammoniaw
  # @FileName: game.py
  # @Date: 2026/8/1
  # @Description: 按照要求修改代码
  """请你输入数学成绩"""
  
  math_score = int(input("请输入这次数学考试成绩>"))
  
  if math_score == 100:
      print("好棒，你离女神又近了一步^_^。")
  else:
      print("小子，想要幸福，就得努力！")
  ```

  
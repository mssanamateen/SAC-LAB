Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> best_student="Jeevan"
>>> subject="SAC"
>>> goal=best_student+" will do well in "+subject
>>> goal
'Jeevan will do well in SAC'
>>> marks=92
>>> score=92+"marks in SAC"
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    score=92+"marks in SAC"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> score=str(92)+"marks in SAC"
>>> score
'92marks in SAC'
>>> quote="u can do this"*5
>>> quote
'u can do thisu can do thisu can do thisu can do thisu can do this'
>>> fruit="apple"*5
>>> fruit
'appleappleappleappleapple'
>>> msg="hi"
>>> name="alice"
>>> full_msg=msg+" "+name
>>> full_msg
'hi alice'

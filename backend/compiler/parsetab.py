
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVIDE LPAREN MINUS NAME NUMBER PLUS RPAREN TIMESstatement : expressionexpression : expression PLUS expression\n| expression MINUS expression\n| expression TIMES expression\n| expression DIVIDE expressionexpression : LPAREN expression RPARENexpression : NUMBERexpression : NAME'
    
_lr_action_items = {'LPAREN':([0,3,6,7,8,9,],[3,3,3,3,3,3,]),'NUMBER':([0,3,6,7,8,9,],[4,4,4,4,4,4,]),'NAME':([0,3,6,7,8,9,],[5,5,5,5,5,5,]),'$end':([1,2,4,5,11,12,13,14,15,],[0,-1,-7,-8,-2,-3,-4,-5,-6,]),'PLUS':([2,4,5,10,11,12,13,14,15,],[6,-7,-8,6,6,6,6,6,-6,]),'MINUS':([2,4,5,10,11,12,13,14,15,],[7,-7,-8,7,7,7,7,7,-6,]),'TIMES':([2,4,5,10,11,12,13,14,15,],[8,-7,-8,8,8,8,8,8,-6,]),'DIVIDE':([2,4,5,10,11,12,13,14,15,],[9,-7,-8,9,9,9,9,9,-6,]),'RPAREN':([4,5,10,11,12,13,14,15,],[-7,-8,15,-2,-3,-4,-5,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,3,6,7,8,9,],[2,10,11,12,13,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement_expr','parser.py',5),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',9),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',10),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser.py',11),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',12),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',23),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',27),
  ('expression -> NAME','expression',1,'p_expression_name','parser.py',31),
]

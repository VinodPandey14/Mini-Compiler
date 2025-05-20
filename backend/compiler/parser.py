import ply.yacc as yacc
from compiler.lexer import tokens

def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = f"({p[1]} {p[2]} {p[3]})"

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = str(p[1])

def p_expression_name(p):
    'expression : NAME'
    p[0] = p[1]

def p_error(p):
    raise SyntaxError(f"Syntax error at '{p.value}'")

def build_parser():
    parser = yacc.yacc()
    return parser

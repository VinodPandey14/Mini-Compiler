import ply.yacc as yacc  # type: ignore
from compiler.lexer import tokens

def make_node(name, children=None):
    return {
        "name": name,
        "children": children if children else []
    }

def p_program(p):
    '''program : statement_list'''
    p[0] = make_node("program", p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : assignment SEMICOLON
                 | if_statement
                 | while_statement
                 | for_statement
                 | switch_statement
                 | BREAK SEMICOLON
                 | block
                 | declaration'''
    if p.slice[1].type == 'BREAK':
        p[0] = make_node("break")
    else:
        p[0] = p[1]

def p_declaration(p):
    '''declaration : TYPE NAME SEMICOLON'''
    p[0] = make_node("declare", [make_node(p[1]), make_node(p[2])])

def p_block(p):
    '''block : LBRACE statement_list RBRACE'''
    p[0] = make_node("block", p[2])

def p_assignment(p):
    '''assignment : NAME EQUALS expression'''
    p[0] = make_node("assign", [make_node("var", [make_node(p[1])]), p[3]])

def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN statement ELSE statement'''
    p[0] = make_node("if", [p[3], p[5], p[7]])

def p_while_statement(p):
    '''while_statement : WHILE LPAREN expression RPAREN statement'''
    p[0] = make_node("while", [p[3], p[5]])

def p_for_statement(p):
    '''for_statement : FOR LPAREN assignment SEMICOLON expression SEMICOLON assignment RPAREN statement'''
    init = p[3]
    cond = p[5]
    update = p[7]
    body = p[9]
    p[0] = make_node("for", [init, cond, update, body])

def p_switch_statement(p):
    '''switch_statement : SWITCH LPAREN expression RPAREN LBRACE case_list RBRACE'''
    p[0] = make_node("switch", [p[3]] + p[6])

def p_case_list(p):
    '''case_list : case_list case
                 | case'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_case(p):
    '''case : CASE expression COLON statement_list
            | DEFAULT COLON statement_list'''
    if p[1] == 'default':
        p[0] = make_node("default", p[3])
    else:
        p[0] = make_node("case", [p[2]] + p[4])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression EQ expression
                  | expression NE expression
                  | expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression'''
    p[0] = make_node(p[2], [p[1], p[3]])

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER
                  | FLOAT'''
    p[0] = make_node("num", [make_node(str(p[1]))])

def p_expression_name(p):
    '''expression : NAME'''
    p[0] = make_node("var", [make_node(p[1])])

def p_expression_function_call(p):
    '''expression : NAME LPAREN argument_list RPAREN'''
    p[0] = make_node("call", [make_node(p[1])] + p[3])

def p_argument_list(p):
    '''argument_list : argument_list COMMA expression
                     | expression
                     | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2 and p[1] is not None:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    raise SyntaxError(f"Syntax error at '{p.value}'" if p else "Syntax error at EOF")

def build_parser():
    return yacc.yacc()

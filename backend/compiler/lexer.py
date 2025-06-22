import ply.lex as lex  # type: ignore

# Reserved keywords
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'break': 'BREAK',
    'int': 'TYPE',
    'float': 'TYPE'
}

# List of token names
tokens = (
    'NAME', 'NUMBER', 'FLOAT',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
    'EQ', 'NE', 'LT', 'GT', 'LE', 'GE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMICOLON', 'COLON', 'COMMA',
    'TYPE'
) + tuple(v for k, v in reserved.items() if v not in ('TYPE',))  # Avoid duplicate 'TYPE'

# Regular expression rules for simple tokens
t_PLUS       = r'\+'
t_MINUS      = r'-'
t_TIMES      = r'\*'
t_DIVIDE     = r'/'
t_EQUALS     = r'='
t_EQ         = r'=='
t_NE         = r'!='
t_LE         = r'<='
t_GE         = r'>='
t_LT         = r'<'
t_GT         = r'>'
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LBRACE     = r'\{'
t_RBRACE     = r'\}'
t_SEMICOLON  = r';'
t_COLON      = r':'
t_COMMA      = r','

# Float literal
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Integer literal
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Identifier or reserved keyword
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'NAME')  # Check for reserved words and TYPE
    return t

# Ignore spaces and tabs
t_ignore = ' \t'

# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    raise SyntaxError(f"Illegal character '{t.value[0]}' at line {t.lineno}")

# Build the lexer
def build_lexer():
    return lex.lex()

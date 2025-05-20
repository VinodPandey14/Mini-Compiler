from compiler.lexer import build_lexer
from compiler.parser import build_parser
from compiler.generator import generate_ir

def process_code(code, grammar):
    lexer = build_lexer()
    lexer.input(code)

    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append((tok.type, tok.value))

    parser = build_parser()
    try:
        parsed_result = parser.parse(code, lexer=build_lexer())
    except Exception as e:
        return {
            'tokens': tokens,
            'parsed': 'Parsing failed',
            'ir': str(e)
        }

    ir = generate_ir(parsed_result)

    return {
        'tokens': [f"{typ}({val})" for typ, val in tokens],
        'parsed': parsed_result,
        'ir': ir
    }

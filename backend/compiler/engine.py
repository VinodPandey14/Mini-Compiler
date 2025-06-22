from compiler.lexer import build_lexer
from compiler.parser import build_parser
from compiler.generator import generate_ir
from compiler.semantic_analyzer import analyze_semantics
from compiler.target_generator import generate_target_code

def process_code(code, grammar):
    # --- Lexical Analysis ---
    lexer = build_lexer()
    lexer.input(code)

    type_map = {
        'IF': 'keyword', 'ELSE': 'keyword', 'WHILE': 'keyword', 'FOR': 'keyword',
        'SWITCH': 'keyword', 'CASE': 'keyword', 'DEFAULT': 'keyword', 'BREAK': 'keyword',
        'TYPE': 'keyword', 'NAME': 'identifier', 'NUMBER': 'integer', 'FLOAT': 'float',
        'PLUS': 'operator', 'MINUS': 'operator', 'TIMES': 'operator', 'DIVIDE': 'operator',
        'EQUALS': 'operator', 'EQ': 'operator', 'NE': 'operator', 'LT': 'operator',
        'GT': 'operator', 'LE': 'operator', 'GE': 'operator',
        'LPAREN': 'separator', 'RPAREN': 'separator', 'LBRACE': 'separator',
        'RBRACE': 'separator', 'SEMICOLON': 'separator', 'COLON': 'separator', 'COMMA': 'separator'
    }

    tokens = []
    try:
        while True:
            tok = lexer.token()
            if not tok:
                break
            category = type_map.get(tok.type, 'unknown')
            tokens.append({"type": category, "value": tok.value})
    except Exception as e:
        return {
            'tokens': [],
            'parsed': None,
            'ir': None,
            'semanticErrors': ["Lexical analysis failed."],
            'targetCode': None
        }

    # --- Syntax Parsing ---
    parsed_result = None
    try:
        parser = build_parser()
        parsed_result = parser.parse(code, lexer=build_lexer())
    except Exception as e:
        print("[DEBUG] Parser Exception:", str(e))
        return {
            'tokens': tokens,
            'parsed': None,
            'ir': f"Parsing Error: {str(e)}",
            'semanticErrors': ["Semantic analysis skipped due to parsing error."],
            'targetCode': None
        }

    # --- Semantic Analysis ---
    semantic_errors = []
    try:
        semantic_errors = analyze_semantics(parsed_result)
    except Exception as e:
        semantic_errors = [f"Semantic Analysis Error: {str(e)}"]

    # --- IR Generation ---
    ir = None
    try:
        ir = generate_ir(parsed_result)
        print("\n[DEBUG] Generated IR:\n", ir)
    except Exception as e:
        import traceback
        traceback.print_exc()
        ir = f"IR Generation Error: {str(e)}"

    # --- Target Code Generation ---
    target_code = None
    try:
        if ir and not ir.startswith("IR Generation Error"):
            ir_lines = ir.strip().splitlines()
            print("\n[DEBUG] IR Lines:\n", ir_lines)
            target_code = generate_target_code(ir_lines)
            print("\n[DEBUG] Target Code:\n", target_code)
    except Exception as e:
        import traceback
        traceback.print_exc()
        target_code = f"Target Code Generation Error: {str(e)}"

    return {
        'tokens': tokens,
        'parsed': parsed_result,
        'ir': ir,
        'semanticErrors': semantic_errors,
        'targetCode': target_code
    }

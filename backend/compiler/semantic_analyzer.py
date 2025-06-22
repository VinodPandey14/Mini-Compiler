class SymbolTable:
    def __init__(self):
        self.table = {}
        self.errors = []

    def declare(self, name, var_type, lineno):
        if name in self.table:
            self.errors.append({
                "message": f"Redeclaration of variable '{name}'",
                "line": lineno
            })
        else:
            self.table[name] = {"type": var_type, "line": lineno}

    def use(self, name, lineno):
        if name not in self.table:
            self.errors.append({
                "message": f"Use of undeclared variable '{name}'",
                "line": lineno
            })

    def assign(self, name, value_type, lineno):
        if name not in self.table:
            self.errors.append({
                "message": f"Assignment to undeclared variable '{name}'",
                "line": lineno
            })
        else:
            declared_type = self.table[name]["type"]
            if declared_type != value_type and declared_type != "unknown":
                self.errors.append({
                    "message": f"Type mismatch in assignment to '{name}' (expected {declared_type}, got {value_type})",
                    "line": lineno
                })

    def get_errors(self):
        return self.errors


def analyze_semantics(ast):
    symbol_table = SymbolTable()
    traverse(ast, symbol_table)
    return symbol_table.get_errors()


def traverse(node, symbol_table, current_type=None):
    if not node or not isinstance(node, dict):
        return

    name = node.get("name")
    children = node.get("children", [])
    lineno = node.get("lineno", 0)

    if name == "assign":
        var_node = children[0]["children"][0]["name"]
        expr_node = children[1]
        expr_type = evaluate_expr_type(expr_node, symbol_table)
        symbol_table.assign(var_node, expr_type, lineno)
        traverse(expr_node, symbol_table)

    elif name == "var":
        var_name = children[0]["name"]
        symbol_table.use(var_name, lineno)

    elif name == "declare":
        var_type = children[0]["name"]
        var_name = children[1]["name"]
        symbol_table.declare(var_name, var_type, lineno)

    for child in children:
        traverse(child, symbol_table)


def evaluate_expr_type(expr, symbol_table):
    if expr["name"] == "num":
        val = expr["children"][0]["name"]
        return "float" if '.' in val else "int"

    elif expr["name"] == "var":
        var_name = expr["children"][0]["name"]
        if var_name in symbol_table.table:
            return symbol_table.table[var_name]["type"]
        else:
            return "unknown"

    elif expr["name"] in ['+', '-', '*', '/', 'EQ', 'NE', 'LT', 'LE', 'GT', 'GE']:
        left = evaluate_expr_type(expr["children"][0], symbol_table)
        right = evaluate_expr_type(expr["children"][1], symbol_table)
        if left == "float" or right == "float":
            return "float"
        return "int"

    return "unknown"

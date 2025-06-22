temp_counter = 0
label_counter = 0

def new_temp():
    global temp_counter
    temp = f"t{temp_counter}"
    temp_counter += 1
    return temp

def new_label():
    global label_counter
    label = f"L{label_counter}"
    label_counter += 1
    return label

def generate_ir(node):
    global temp_counter, label_counter
    temp_counter = 0
    label_counter = 0
    code = []
    context_stack = []

    def emit(line):
        code.append(line)

    def walk(n):
        if n["name"] == "program":
            for child in n["children"]:
                walk(child)

        elif n["name"] == "declare":
            var_type = n["children"][0]["name"]
            var_name = n["children"][1]["name"]
            emit(f"DECLARE {var_name} : {var_type}")

        elif n["name"] == "assign":
            var_name = walk(n["children"][0])
            value = walk(n["children"][1])
            emit(f"{var_name} = {value}")

        elif n["name"] == "if":
            cond = walk(n["children"][0])
            label_true = new_label()
            label_false = new_label()
            label_end = new_label()

            emit(f"IF {cond} GOTO {label_true}")
            emit(f"GOTO {label_false}")
            emit(f"{label_true}:")
            walk(n["children"][1])
            emit(f"GOTO {label_end}")
            emit(f"{label_false}:")
            walk(n["children"][2])
            emit(f"{label_end}:")

        elif n["name"] == "while":
            label_start = new_label()
            label_exit = new_label()
            context_stack.append({"break": label_exit})

            emit(f"{label_start}:")
            cond = walk(n["children"][0])
            emit(f"IF NOT {cond} GOTO {label_exit}")
            walk(n["children"][1])
            emit(f"GOTO {label_start}")
            emit(f"{label_exit}:")

            context_stack.pop()

        elif n["name"] == "for":
            walk(n["children"][0])  # init
            label_check = new_label()
            label_body = new_label()
            label_end = new_label()
            context_stack.append({"break": label_end})

            emit(f"{label_check}:")
            cond = walk(n["children"][1])
            emit(f"IF {cond} GOTO {label_body}")
            emit(f"GOTO {label_end}")
            emit(f"{label_body}:")
            walk(n["children"][3])  # body
            walk(n["children"][2])  # update
            emit(f"GOTO {label_check}")
            emit(f"{label_end}:")

            context_stack.pop()

        elif n["name"] == "switch":
            expr = walk(n["children"][0])
            end_label = new_label()
            context_stack.append({"break": end_label})
            case_labels = []
            default_label = None

            for child in n["children"][1:]:
                if child["name"] == "case":
                    val = walk(child["children"][0])
                    label = new_label()
                    emit(f"IF {expr} == {val} GOTO {label}")
                    case_labels.append((label, child["children"][1:]))
                elif child["name"] == "default":
                    default_label = new_label()
                    emit(f"GOTO {default_label}")
                    case_labels.append((default_label, child["children"]))

            for label, stmts in case_labels:
                emit(f"{label}:")
                for stmt in stmts:
                    walk(stmt)
            emit(f"{end_label}:")

            context_stack.pop()

        elif n["name"] == "break":
            if context_stack:
                emit(f"GOTO {context_stack[-1]['break']}")
            else:
                emit("# Error: 'break' outside of loop or switch")

        elif n["name"] == "block":
            for stmt in n["children"]:
                walk(stmt)

        elif n["name"] == "call":
            args = [walk(arg) for arg in n["children"][1:]]
            temp = new_temp()
            emit(f"{temp} = CALL {n['children'][0]['name']}({', '.join(args)})")
            return temp

        elif n["name"] in {"+", "-", "*", "/", ">", "<", ">=", "<=", "==", "!="}:
            left = walk(n["children"][0])
            right = walk(n["children"][1])
            temp = new_temp()
            emit(f"{temp} = {left} {n['name']} {right}")
            return temp

        elif n["name"] == "num":
            return str(n["children"][0]["name"])

        elif n["name"] == "var":
            return str(n["children"][0]["name"])

        else:
            emit(f"# Unknown node type: {n['name']}")
            return "?"

    walk(node)
    return "\n".join(code)

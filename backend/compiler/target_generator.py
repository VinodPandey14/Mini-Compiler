def generate_target_code(ir_lines):
    assembly = []
    temp_map = {}
    reg_counter = 0

    def get_register(var):
        nonlocal reg_counter
        if var not in temp_map:
            temp_map[var] = f"$t{reg_counter}"
            reg_counter += 1
        return temp_map[var]

    for line in ir_lines:
        line = line.strip()

        if not line or line.startswith("DECLARE"):
            continue

        # Label
        if line.endswith(":"):
            assembly.append(line)
            continue

        # GOTO
        if line.startswith("GOTO"):
            parts = line.split()
            if len(parts) == 2:
                assembly.append(f"j {parts[1]}")
            else:
                assembly.append(f"# Malformed GOTO: {line}")
            continue

        # IF condition
        if line.startswith("IF"):
            parts = line.split()

            # Case: IF NOT cond GOTO label
            if len(parts) == 5 and parts[1] == "NOT" and parts[3] == "GOTO":
                cond = get_register(parts[2])
                label = parts[4]
                assembly.append(f"beq {cond}, $zero, {label}")
                continue

            # Case: IF a OP b GOTO label
            if len(parts) == 6 and parts[4] == "GOTO":
                a = get_register(parts[1])
                op = parts[2]
                b = get_register(parts[3])
                label = parts[5]

                if op == "==":
                    assembly.append(f"beq {a}, {b}, {label}")
                elif op == "!=":
                    assembly.append(f"bne {a}, {b}, {label}")
                elif op == "<":
                    assembly.append(f"blt {a}, {b}, {label}")
                elif op == "<=":
                    assembly.append(f"ble {a}, {b}, {label}")
                elif op == ">":
                    assembly.append(f"bgt {a}, {b}, {label}")
                elif op == ">=":
                    assembly.append(f"bge {a}, {b}, {label}")
                else:
                    assembly.append(f"# Unsupported comparison op: {op}")
                continue

            # Case: IF cond GOTO label
            if len(parts) == 4 and parts[2] == "GOTO":
                cond = get_register(parts[1])
                label = parts[3]
                assembly.append(f"bnez {cond}, {label}")
                continue

            # Malformed
            assembly.append(f"# Malformed IF: {line}")
            continue

        # Assignment
        if '=' in line:
            try:
                lhs, rhs = [x.strip() for x in line.split('=', 1)]

                # Binary operation
                if any(op in rhs for op in ['+', '-', '*', '/']):
                    parts = rhs.split()
                    if len(parts) == 3:
                        op1 = get_register(parts[0])
                        operator = parts[1]
                        op2 = get_register(parts[2])
                        dest = get_register(lhs)

                        if operator == '+':
                            assembly.append(f"add {dest}, {op1}, {op2}")
                        elif operator == '-':
                            assembly.append(f"sub {dest}, {op1}, {op2}")
                        elif operator == '*':
                            assembly.append(f"mul {dest}, {op1}, {op2}")
                        elif operator == '/':
                            assembly.append(f"div {op1}, {op2}")
                            assembly.append(f"mflo {dest}")
                        else:
                            assembly.append(f"# Unsupported operator: {operator}")
                    else:
                        assembly.append(f"# Malformed binary operation: {rhs}")
                else:
                    # Simple assignment
                    dest = get_register(lhs)
                    if rhs.isdigit():
                        assembly.append(f"li {dest}, {rhs}")
                    else:
                        src = get_register(rhs)
                        assembly.append(f"move {dest}, {src}")
            except Exception as e:
                assembly.append(f"# Error parsing assignment: {line} ({str(e)})")
            continue

        # Unrecognized IR line
        assembly.append(f"# Unrecognized IR: {line}")

    return "\n".join(assembly)

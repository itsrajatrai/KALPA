import re

def parse_line(line):
    line = line.strip()

    # Short Form
    if match := re.match(r"^(\w+) *= *(\d+|\w+|\".*?\")$", line):
        var, val = match.groups()
        val = val.strip('\"') if val.startswith('\"') else (int(val) if val.isdigit() else val)
        return {"type": "assignment", "variable": var, "value": val}

    if match := re.match(r"^(\w+) *= *(\w+) *([+\-*/]) *(\w+)$", line):
        target, left, op, right = match.groups()
        op_map = {"+": "plus", "-": "minus", "*": "times", "/": "divided by"}
        return {"type": "arithmetic", "target": target, "left": left, "operator": op_map[op], "right": right}

    if match := re.match(r"^print (.+)", line):
        val = match.group(1)
        val = val.strip('\"') if val.startswith('\"') else (int(val) if val.isdigit() else val)
        return {"type": "print", "value": val}

    if match := re.match(r"^if (\w+) *(>|<|==) *(\w+): *print (.+)", line):
        var, op, val, out = match.groups()
        op_map = {">": "greater than", "<": "less than", "==": "equal to"}
        val = val.strip('\"') if val.startswith('\"') else (int(val) if val.isdigit() else val)
        return {"type": "if", "variable": var, "operator": op_map[op], "value": val, "then": out.strip('\"')}

    if match := re.match(r"^repeat (\d+): *print (.+)", line):
        count, msg = match.groups()
        return {"type": "repeat", "count": int(count), "action": "print", "value": msg.strip('\"')}

    # Long Form fallback
    if match := re.match(r"Let (\w+) be (\w+) (plus|minus|times|divided by) (\w+)", line):
        target, left, op, right = match.groups()
        return {"type": "arithmetic", "target": target, "left": left, "operator": op, "right": right}

    if match := re.match(r"Let (\w+) be (.+)", line):
        var, val = match.groups()
        val = val.strip('\"') if val.startswith('\"') else (int(val) if val.isdigit() else val)
        return {"type": "assignment", "variable": var, "value": val}

    if match := re.match(r"If (\w+) is (greater than|less than|equal to) (.+), then print (.+)", line):
        var, op, value, output = match.groups()
        value = value.strip('\"') if value.startswith('\"') else (int(value) if value.isdigit() else value)
        return {"type": "if", "variable": var, "operator": op, "value": value, "then": output.strip('\"')}

    if match := re.match(r"Repeat (\d+) times: print (.+)", line):
        count, message = match.groups()
        return {"type": "repeat", "count": int(count), "action": "print", "value": message.strip('\"')}

    return {"type": "unknown", "raw": line}

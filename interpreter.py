variables = {}

def interpret(parsed_lines):
    for instruction in parsed_lines:
        if instruction['type'] == 'assignment':
            variables[instruction['variable']] = instruction['value']

        elif instruction['type'] == 'arithmetic':
            left = variables.get(instruction['left'], instruction['left'])
            right = variables.get(instruction['right'], instruction['right'])

            if isinstance(left, str) and left.isdigit():
                left = int(left)
            if isinstance(right, str) and right.isdigit():
                right = int(right)

            if instruction['operator'] == 'plus':
                result = left + right
            elif instruction['operator'] == 'minus':
                result = left - right
            elif instruction['operator'] == 'times':
                result = left * right
            elif instruction['operator'] == 'divided by':
                result = left // right if right != 0 else 0
            else:
                result = None

            variables[instruction['target']] = result

        elif instruction['type'] == 'print':
            val = instruction['value']
            print(variables[val] if val in variables else val)

        elif instruction['type'] == 'if':
            var_value = variables.get(instruction['variable'], 0)
            target_value = instruction['value']

            if isinstance(target_value, str) and target_value in variables:
                target_value = variables[target_value]

            if isinstance(var_value, str) and var_value.isdigit():
                var_value = int(var_value)
            if isinstance(target_value, str) and target_value.isdigit():
                target_value = int(target_value)

            condition = {
                "greater than": var_value > target_value,
                "less than": var_value < target_value,
                "equal to": var_value == target_value,
            }.get(instruction['operator'], False)

            if condition:
                print(instruction['then'])

        elif instruction['type'] == 'repeat':
            for _ in range(instruction['count']):
                if instruction['action'] == 'print':
                    val = instruction['value']
                    print(variables[val] if val in variables else val)

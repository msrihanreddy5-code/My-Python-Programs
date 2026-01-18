def interpret(code):
    vars = {}
    for line in code.splitlines():
        if "=" in line:
            k,v = line.split("=")
            vars[k.strip()] = int(v)
        else:
            print(vars.get(line.strip(), "Undefined"))

program = """
x = 10
y = 20
x
y
"""
interpret(program)

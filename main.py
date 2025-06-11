from parser import parse_line
from interpreter import interpret

# Load KALPA script from file
with open("examples/sample.kalpa", "r") as f:
    lines = f.readlines()

# Parse and interpret
parsed = [parse_line(line.strip()) for line in lines if line.strip()]
interpret(parsed)

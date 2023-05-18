from latex2sympy2 import latex2sympy, latex2latex

import re

def parse_and_calculate(text, calculate):
    # Find all placeholders
    matches = re.findall(r'{{(.*?)}}', text)

    for match in matches:
        # Calculate result for each placeholder
        result = calculate(match)

        # Replace placeholder with result in LaTeX format
        text = text.replace(f'{{{{{match}}}}}', f'$${result}$$')

    return text


def calculate(expression):
    return latex2latex(expression)

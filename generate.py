import random
import sys

def generate_bingo_card(words, num_cards=1):
    # Define the LaTeX header as a separate string
    latex_header = r"""
\documentclass{article}
\usepackage[margin=1in]{geometry}
\usepackage{array}
\begin{document}
"""

    # Initialize an empty string to store the complete LaTeX code
    latex_code = latex_header

    for card_number in range(1, num_cards + 1):
        random.shuffle(words)
        card = [words[i:i + 5] for i in range(0, 25, 5)]

        if card_number > 1:
            latex_code += "\\newpage\n"  # Start a new page for each bingo card


        for i, row in enumerate(card):
            latex_code += "\\begin{center}\n"
            latex_code += "\\begin{tabular}{|c|c|c|c|c|}\n"
            latex_code += "\\hline\n"

            for r in row:
                latex_code += r + " & "
            latex_code = latex_code[:-2]  # Remove the last "&" and space
            latex_code += " \\\\\n"
            latex_code += "\\hline\n"

            latex_code += "\\end{tabular}\n"
            latex_code += "\\end{center}\n"

    latex_code += "\\end{document}\n"

    return latex_code

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate.py <number_of_cards> <output_file.tex>")
        sys.exit(1)

    num_cards = int(sys.argv[1])  # Number of bingo cards to generate
    output_file = sys.argv[2]  # Output file name

    bingo_words = ["Word1", "Word2", "Word3", "Word4", "Word5",
                   "Word6", "Word7", "Word8", "Word9", "Word10",
                   "Word11", "Word12", "Word13", "Word14", "Word15",
                   "Word16", "Word17", "Word18", "Word19", "Word20",
                   "Word21", "Word22", "Word23", "Word24", "Word25"]

    bingo_cards_latex = generate_bingo_card(bingo_words, num_cards)

    with open(output_file, "w") as file:
        file.write(bingo_cards_latex)

    print(f"{num_cards} Bingo cards LaTeX code has been saved to {output_file}")


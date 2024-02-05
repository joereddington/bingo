import random
import sys

def generate_bingo_card(words, num_cards=1):
    # Define the LaTeX header as a separate string
    latex_header = r"""
\documentclass{report}
\usepackage[margin=1in]{geometry}
\usepackage{array}
\usepackage{tabularx}
\begin{document}
"""

    # Initialize an empty string to store the complete LaTeX code
    latex_code = latex_header

    for card_number in range(1, num_cards + 1):
        random.shuffle(words)
        card = [words[i:i + 5] for i in range(0, 25, 5)]

        if card_number > 1:
            latex_code += "\\newpage\n"  # Start a new page for each bingo card

        latex_code += "\\huge\n"
        latex_code += "\\chapter*{Badly spaced Bingo!}\n"
        latex_code += "Cross off a square when the event happens. There are prizes for completing rows, columns, and the whole square"
        latex_code += "\\begin{center}\n"
        latex_code += "\\huge"
        latex_code += "\\begin{tabularx}{\\textwidth}{|X|X|X|X|X|}"
        latex_code += "\\hline\n"

        for row in range(0,4):

            for col in range(0,4): 
                latex_code += words[row*5+col] + " & "
            latex_code = latex_code[:-2]  # Remove the last "&" and spac
            latex_code += " \\\\\n"
            latex_code += "\\hline\n"

        latex_code += "\\end{tabularx}\n"
        latex_code += "\\end{center}\n"

    latex_code += "\\end{document}\n"

    return latex_code

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate.py <number_of_cards> <output_file.tex>")
        sys.exit(1)

    num_cards = int(sys.argv[1])  # Number of bingo cards to generate
    output_file = sys.argv[2]  # Output file name

    bingo_words = ["Someone is late", "Joe doesn't know the answer to the question", "A typo is found on a slide", "A deadline is extended", "One student replies to another's question",
                   "Not a question more a comment", "A slide is skipped", "A student gives an example from their own experience", "The class point to a wall", "A link is shared in teams",
                   "Lecture slides are different from uploaded slides", "Attendance is more than 60", "One student asks a question on behalf of another", "Some information is useful but off-topic", "Student phone rings",
                   "Slide text is too small", "We'll talk about this later in the course", "A definition that might be on the exam", "Reference to a pop culture event before 2001", "Slide is 'funny' ",
                   "Joe can't work a computer", "Class consulted on course structure", "Being a manager sounds hard", "Computer correctly locked at break", "Joe walks too far from the microphone"]

    bingo_cards_latex = generate_bingo_card(bingo_words, num_cards)

    with open(output_file, "w") as file:
        file.write(bingo_cards_latex)

    print(f"{num_cards} Bingo cards LaTeX code has been saved to {output_file}")


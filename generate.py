import sys
import random


#TODO 
# * Sort the events into easy/medium/hard
# * Sort the events into week1/week2/ect 
#    * Go and get the old events from previous git commits
# (Might only be able to do one of the above) 
# * Put the events into a separate text file 
# Add '10 questions asked'

def make_table(words, size_of_square=4):
    random.shuffle(words)
    latex_code =""
    latex_code += "\\begin{center}\n"
    latex_code += "\\Large"
    latex_code += "\\begin{tabularx}{\\textwidth}{|X|X|X|X|X|}"
    latex_code += "\\hline\n"

    for row in range(0,size_of_square):

        for col in range(0,size_of_square): 
            latex_code += words[(row*size_of_square+1)+col] + " & "
        latex_code = latex_code[:-2]  # Remove the last "&" and spac
        latex_code += " \\\\\n"
        latex_code += "\\hline\n"

    latex_code += "\\end{tabularx}\n"
    latex_code += "\\end{center}\n"
    return latex_code


def generate_bingo_card(words, num_students=1):
    # Define the LaTeX header as a separate string
    lc = r"""
\documentclass{report}
\usepackage[margin=1in]{geometry}
\usepackage{array}
\usepackage{tabularx}
\begin{document}
\large
"""
    for card_number in range(1, num_students + 1):
        if card_number > 1:
            lc += "\\newpage\n"  # Start a new page for each bingo card
        lc += "\\chapter*{IY3501 Bingo!}\n"
        lc += "Cross off a square when the event happens. There are prizes for completing rows, columns, and the whole square."
        lc += "\\section*{First half of lecture}\n"
        lc += make_table(words)
        lc += "\\newpage\n"  
        lc += "\\section*{Second half of lecture}\n"
        lc += make_table(words)
        lc += r"""\vspace{2cm}\begin{tabular}{|p{0.3\textwidth}|p{0.7\textwidth}|}
\hline
Name: & \\
\hline
Date: & \\
\hline
\end{tabular}"""

    return lc + "\\end{document}\n"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate.py <number_of_cards> <output_file.tex>")
        sys.exit(1)

    num_cards = int(sys.argv[1])  # Number of bingo cards to generate
    output_file = sys.argv[2]  # Output file name

    bingo_words_medium = ["Joe walks too far from the microphone", "Joe doesn't know the answer to the question", "Typo pointed out on slide", "A student asks a question based on the reading.", "One student replies to another's question from at least four people/rows away",
                   "Not a question more a comment", "Someone asks a question for the first time in the course", "A student gives an example from their own experience", "The class point to a wall", "A relevant link is shared in teams", "management seams hard", "management seems like fun",  
                   "Student requests a (none-typo) change to slide content", "Attendance is more than 50", "One student asks a question on behalf of another", "Some information is useful but off-topic",
                   "Slide text is too small", "We'll talk about this later in the course", "A definition that might be on the exam", "Reference to a pop culture event before 2000", "I personally have done the reading",
                   "Joe can't work a computer", "Class consulted on course structure", "It's a registered member of the course's first time seeing the lecturer in person.", "Lego model assembled during break (on document cam)", "More students in the front half of the room than the back {\em during} the lecture"]
    bingo_words_hard = ["There are four students in the room not registered on the course", "Joe doesn't know the answer to the question", "A typo is found on a slide", "A student asks a question based on the reading.", "One student replies to another's question from at least four people/rows away",
                   "Not a question more a comment", "Someone asks a question for the first time in the course", "A student gives an example from their own experience", "The class point to a wall", "A relevant link is shared in teams",
                   "Student requests a (none-typo) change to slide content", "Attendance is more than 60", "One student asks a question on behalf of another", "Some information is useful but off-topic", "Student phone rings",
                   "Slide text is too small", "We'll talk about this later in the course", "A definition that might be on the exam", "Reference to a pop culture event before 1990", "I personally have done the reading",
                   "Joe can't work a computer", "Class consulted on course structure", "It's a registered member of the course's first time seeing the lecturer in person.", "Lego model assembled during break (on document cam)", "More students in the front half of the room than the back {\em during} the lecture"]

    bingo_cards_latex = generate_bingo_card(bingo_words_medium, num_cards)
    with open(output_file, "w") as file:
        file.write(bingo_cards_latex)

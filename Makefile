# Makefile for generating bingo cards and compiling them into PDFs

# Number of bingo cards to generate
NUM_CARDS := 5

# List of bingo words or phrases
BINGO_WORDS := "Word1" "Word2" "Word3" "Word4" "Word5" "Word6" "Word7" "Word8" "Word9" "Word10" "Word11" "Word12" "Word13" "Word14" "Word15"

.PHONY: all clean

all: bingo_cards.pdf

bingo_cards.tex:
	python3 generate.py 5 bingo_cards.tex

bingo_cards.pdf: bingo_cards.tex
	pdflatex bingo_cards.tex
	pdflatex bingo_cards.tex  # Run twice to resolve references

clean:
	rm -f bingo_cards.tex bingo_cards.pdf *.aux *.log *.out


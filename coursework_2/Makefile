
MDFILES := coursework.md feedback_yr3.md feedback_msc.md
PDFS := $(patsubst %.md,%.pdf, $(MDFILES))

all: $(PDFS)

feedback_%.pdf: feedback_%.md
	pandoc -V geometry:landscape -t latex -o $@ $<

%.pdf: %.md
	pandoc -t latex -o $@ $<

clean:
	rm -f $(PDFS)


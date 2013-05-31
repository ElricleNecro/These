VIEWER=xpdf
LATEXMK=latex-mk
LATEXMKOPT=--pdflatex

MASTER=master.tex

PDF=$(MASTER:.tex=.pdf)

%.pdf:%.tex
	$(LATEXMK) $(LATEXMKOPT) $<

all:pdf

pdf:$(PDF)

view:$(PDF)
	$(VIEWER) $(PDF) &

clean:
	$(LATEXMK) $(LATEXMKOPT) --clean $(MASTER)
	$(RM) *.{aux,bbl,blg,lof,log,lot,maf,mtc*,out,toc}


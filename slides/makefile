TEX = $(wildcard *.tex)
PDF = $(TEX:.tex=.pdf)

all: $(PDF)

figures:
	$(MAKE) -C figures

%.pdf: %.tex figures
	latexmk -pdf $<

clean:
	rm -f *.{aux,bbl,blg,fdb_latexmk,fls,log,out,lof,dvi}
	rm -f *.{bcf,run.xml}
	rm -f *.{toc,snm,nav}
	rm -f *.gz*

cleanall: clean
	$(MAKE) clean -C figures
	rm -f $(PDF)

.PHONY: all figures clean cleanall

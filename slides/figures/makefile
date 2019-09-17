EPS = $(wildcard *.eps)
SVG = $(wildcard *.svg)
ODG = $(wildcard *.odg)
PY = $(wildcard *.py)
PDF = $(EPS:.eps=.pdf) $(SVG:.svg=.pdf) $(ODG:.odg=.pdf) $(PY:.py=.pdf)

all: $(PDF)

%.pdf: %.eps
	-epstopdf $<
	pdfcrop $@ $@

%.pdf: %.svg
	inkscape -D -z --file=$< --export-pdf=$@
	pdfcrop $@ $@

%.pdf: %.odg
	libreoffice --headless \
		"-env:UserInstallation=file:///tmp/libreoffice_conversion_${USER}" \
		--convert-to pdf $<
	pdfcrop $@ $@

%.pdf: %.py
	python $<
	pdfcrop $@ $@

clean:
	rm -f $(PDF)

.PHONY: all clean

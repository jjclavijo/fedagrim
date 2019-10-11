pres_tmp.html: presentacion.md
	pandoc -t html5 -o pres_tmp.html presentacion.md

slides/comp_time: pres_tmp.html
	./split_slides.py
	date > slides/comp_time

pdf/comp_time: slides/comp_time
	-@rm pdf/*
	for i in slides/*.html;\
	do touch pdf/$$(basename $${i%%.*}).pdf;\
	done

.PHONY: pdf/%.pdf

pdf/%.pdf: slides/%.html pdf/comp_time
	wkhtmltopdf -O Landscape $< $@.1
	cd pdf ;\
	pdftk A=$*.pdf.1 cat A1 output $*.pdf; \
	pdfcrop $*.pdf; \
	rm $*.pdf; \
	mv $*-crop.pdf $*.pdf; \
	rm $*.pdf.1

presentacion.pdf: pdf/comp_time 
	pdftk Portada.pdf pdf/*.pdf cat output presentacion.pdf

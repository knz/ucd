PYTHON = python3.3

TABLES = \
	tables/ucd.json \
	tables/ucd.html \
	tables/ucd.h \
	tables/ucd.py \
	tables/ucd.txt

all: $(TABLES)

NamesList.txt:
	wget -O $@ http://www.unicode.org/Public/UCD/latest/ucd/NamesList.txt

tables/ucd.json: NamesList.txt
	mkdir -p tables
	$(PYTHON) uniconvert.py $< $@

.SUFFIXES: .json .h .html .txt .py

.json.h:
	$(PYTHON) unidefine.py $< >$@

.json.html:
	$(PYTHON) unihtml.py $< >$@

.json.txt:
	$(PYTHON) uniprint.py $< >$@

.json.py:
	$(PYTHON) unipy.py $< >$@

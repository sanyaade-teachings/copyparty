all: $(addsuffix .gz, $(wildcard *.*))

%.gz: %
	pigz -11 -J 34 -I 573 $<

# pigz -11 -J 34 -I 100 -F < $< > $@.first

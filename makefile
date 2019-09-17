NB = $(sort $(wildcard *.ipynb))
DIRS = $(wildcard */)
CLEANDIRS = $(DIRS:%=clean-%)

run: $(NB) $(DIRS)

$(NB):
	jupyter nbconvert --inplace --execute --ExecutePreprocessor.timeout=-1 $@

$(DIRS):
	$(MAKE) -C $@

clean: $(CLEANDIRS)
	jupyter nbconvert --inplace --ClearOutputPreprocessor.enabled=True $(NB)

$(CLEANDIRS):
	$(MAKE) clean -C $(@:clean-%=%)

readme:
	grip README.md

.PHONY: run $(NB) $(DIRS) clean $(CLEANDIRS) readme

# Installs this application for usage without needing to specify an absolute address for the program.

DEST=/usr/local/bin/

all: compile

compile:
	@echo Python files don't need compilation!

install:
	cp days_until.py daysuntil
	install daysuntil $(DEST)

clean:
	rm -f daysuntil


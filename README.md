# days-until
A CLI program to give you the number of days until or since certain events.

This program reads a file (by default `eventlist.txt`) and lists all events in the file by the number of days until (or since) the specified the event. The order of entries in the file does not matter, as the program will internally order all events by when they occurred/will occur.

### Usage
```
python days_until.py [-h] [-d DELTA] [-r] [-n] [-N] [input-file [input-file ...]]

List events by days since/until they happen(ed).

positional arguments:
  input-file            Specify a input file. If none are specified, then "eventlist.txt" is used.

optional arguments:
  -h, --help            Show this help message and exit
  -d, --delta DELTA
                        Only print events whose days since/until is less than
                        this argument. (0 for no limits)
  -D, --reverse-delta REVERSE_DELTA
                        Only print events whose days since/until is greater
                        than or equal to this argument. (default is 0)
  -r, --reverse         Print the events in reverse order.
  -n, --nopast          Don't print any events that have already happened.
  -N, --nofuture        Don't print any events that haven't happened yet.
```

Here are some examples:
* `python days_until.py -nd 30` will print all events that are going to happen within 30 days.
* `python days_until.py -Nr` will print all past events from most to least recent.
* `python days_until.py -d 100 -D 100` will print all events that happened within 100 days from today.

### Installation
On Unix-like systems, a `Makefile` is provided to "install" this program in your $PATH, by default at `/usr/local/bin/`. After installation, you can invoke this program by running `daysuntil` in your shell of choice.

To do so, in the top-level directory of this repo, invoke `make install`. Be sure you sufficient privileges to install the file.

### Event List File Format
All entries in the input file must be in the exact form `[3-Month] [2-Day] [4-Year] [Event name or description].` As an example, the following would be an appropriately-formatted event: `Jan 01 2000 Y2K happens`.

### Troubleshooting
The entries must be *exactly* in the specified format, and even minor deviations will not be recognized by the program. For example, the following, while similar, are invalid:
`January 01 2000 Y2K`
`Jan 1 2000 Y2K`
`Jan 01 00 Y2K`
`01 01 2000 Y2K`

Events that occurred before 1 AD or after 9999 AD will not be accepted.


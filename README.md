# days-until
A CLI program to give you the number of days until or since certain events.

This program reads a file (by default `eventlist.txt`) and lists all events in the file by the number of days until (or since) the specified the event. The order of entries in the file does not matter, as the program will internally order all events by when they occurred/will occur.

### Usage
```
python days_until.py [-h] [-d DELTA] [-D RDELTA] [-r] [-n] [-N] [input-file [input-file ...]]

List events by days since/until they happen(ed).

positional arguments:
  input-file            Specify a input file. If none are specified, then
                        eventlist.txt is used.

optional arguments:
  -h, --help            show this help message and exit
  -d DELTA, --delta DELTA
                        Only print events whose days since/until is less than
                        this argument. (0 for no limits)
  -D RDELTA, --reverse-delta RDELTA
                        Only print events whose days since/until is greater
                        than or equal to this argument. (default is 0)
  -r, --reverse         Print the events in reverse order.
  -n, --nopast          Don't print any events that have already happened.
  -N, --nofuture        Don't print any events that haven't happened yet.
  -t, --totals-style [{none,simple,categories,both}]
                        Specify how you want days_until.py to print event
                        totals. (default is 'none')
  -T, --totals-only     Print only the event totals; do not print any events.
  -A, --total-all       When displaying totals, print them for all events in all
                        files, not just the ones that were printed.
```

The different choices available for `-t` are explained below:
  * none       - Do not print an event count. This is the default behavior.
  * simple     - Print one number that denotes the total number of events printed by the program.
  * categories - Print two numbers: one for the number of past events printed and another for future ones.
  * both       - Use both the 'simple' and 'categories' options.

Here are some examples:
* `python days_until.py` will print all events in `eventlist.txt`.
* `python days_until.py -` will take standard input and print all events found.
* `python days_until.py file1 file2` will print all events in both `file1` and `file2`.
* `python days_until.py -nd 30` will print all events that are going to happen within 30 days.
* `python days_until.py -Nr` will print all past events from most to least recent.
* `python days_until.py -Nd 365` will print all events that happened at least a year ago.
* `python days_until.py -n -d 7 -D 14` will print all events that are going to happen next week.

### Installation
On Unix-like systems, a `Makefile` is provided to "install" this program in your `$PATH`, by default at `/usr/local/bin/`. After installation, you can invoke this program by running `daysuntil` in your shell of choice.

To do so, in the top-level directory of this repo, invoke `make install`. Be sure you sufficient privileges to install the file.

### Event List File Format
All entries in the input file must be in the exact form `[3-Month] [2-Day] [4-Year] [Event name or description].` As an example, the following would be an appropriately-formatted event: `Jan 01 2000 Y2K happens`.

The entries must be *exactly* in the specified format, and even minor deviations will not be recognized by the program. For example, the following, while similar, are invalid:
* `January 01 2000 Y2K`
* `Jan 1 2000 Y2K`
* `Jan 01 00 Y2K`
* `01 01 2000 Y2K`

You may also specify recurring events like Christmas by replacing the 'year' field with dashes. For example:
* `Dec 25 ---- Christmas Day`
* `Feb 14 ---- Valentine's Day`
<br> Like noted above, the format is very strict, so the year field must contain exactly four dashes.

*Why is the format so unforgiving?* <br>
Because I'm using `datetime.strptime`, which takes formatted time in a certain format. Also, this way it looks nicer if you view your `eventlist.txt` with a monospaced font.

### Known Issues
* Events that occurred before 1 AD or after 9999 AD will not be accepted.
* The program does not accept passsing `--` as a flag to specify the end of command-line arguments.


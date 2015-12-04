# days-until
A CLI program to give you the number of days until or since certain events.

This program reads a file (by default `eventlist.txt`) and lists all events in the file by the number of days until (or since) the specified the event. The order of entries in the file does not matter, as the program will internally order all events by when they occurred/will occur.

### Usage
```
days_until.py [-h] [-d DELTA] [-r] [-n] [-N] [input-file [input-file ...]]

List events by days since/until they happen(ed).

positional arguments:
  input-file            Specify a input file. If none are specified, then `eventlist.txt` is used.

optional arguments:
  -h, --help            Show this help message and exit
  -d, --delta DELTA     Only print events whose days since/until is less than
                        this argument. (0 for no limits)
  -r, --reverse         Print the events in reverse order.
  -n, --nopast          Don't print any events that have already happened.
  -N, --nofuture        Don't print any events that haven't happened yet.
```

### Event List File Format
All entries in the input file must be in the exact form `[3-Month] [2-Day] [4-Year] [Event name of description].` As an example, the following would be an appropriately-formatted event: `Jan 01 2000 Y2K happens`.

### Troubleshooting
The entries must be *exactly* in the specified format, and even minor deviations will not be recognized by the program. For example, the following, while similar, are invalid:
`January 01 2000 Y2K`
`Jan 1 2000 Y2K`
`Jan 01 00 Y2K`
`01 01 2000 Y2K`

Events that occurred before 1 AD or after 9999 AD will not be accepted.


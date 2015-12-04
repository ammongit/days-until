# days-until
A CLI program to give you the number of days until or since certain events.

This program reads a file (by default `eventlist.txt`) and lists all events in the file by the number of days until (or since) the specified the event. The order of entries in the file does not matter, as the program will internally order all events by when they occurred/will occur.

### Event List File Format
All entries in the input file must be in the exact form `[3-Month] [2-Day] [4-Year] [Event name of description].` As an example, the following would be an appropriately-formatted event: `Jan 01 2000 Y2K happens`.

### Troubleshooting
The entries must be *exactly* in this format, even minor deviations will not be recognized by the program. For example, the following, while similar, are invalid:
`January 01 2000 Y2K`
`Jan 1 2000 Y2K`
`Jan 01 00 Y2K`
`01 01 2000 Y2K`

Events that occurred before {date} or after {date} will not be accepted because of limitations in the time library used by the program.


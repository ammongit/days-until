#!/usr/bin/env python
from __future__ import print_function, with_statement
from datetime import datetime
import argparse, math, re, os, sys

DEFAULT_EVENT_FILE = os.path.dirname(sys.argv[0]) + os.sep + "eventlist.txt"
EVENT_FORMAT_RE = re.compile("([A-Z][a-z]{2} [0-9]{2} [0-9]{4}) (.*)\n")

def get_events(fns):
    if not fns:
        fns = {DEFAULT_EVENT_FILE}
    else:
        fns = set(fns)

    past = []
    future = []

    for fn in fns:
        try:
            if fn == "-": # Read from stdin
                parse_file(sys.stdin, past, future)
            else:
                with open(fn, 'r') as fh:
                    parse_file(fh, past, future)
        except StandardError as err:
            print(err, file=sys.stderr)
            exit(1)

    past.sort()
    future.sort()

    if not (past or future):
        # Event list is empty
        width = 1
    elif not past:
        # Past event list is empty
        width = math.ceil(math.log10(future[-1][0]))
    elif not future:
        # Future event list is empty
        width = math.ceil(math.log10(past[-1][0]))
    else:
        # Calculate number of digits
        width = math.ceil(math.log10(max(past[-1][0], future[-1][0])))
    return past[::-1], future, width # [::-1] reverses the collection

def parse_file(fh, past, future):
    line = fh.readline()
    while line:
        match = EVENT_FORMAT_RE.match(line)
        if match:
            date = datetime.strptime(match.group(1), "%b %d %Y")
            name = match.group(2)
            delta = (datetime.today() - date).days
            if delta >= 0:
                past.append((delta, name))
            else:
                future.append((-delta, name))
        line = fh.readline()
    return past, future

def in_range(args, event):
    return (not args.delta or event[0] <= args.delta) and \
           event[0] >= args.rdelta

def print_past_events(args, past, width):
    count = 0
    if not args.nopast:
        form = "%%%dd day%%c since %%s" % width
        for event in past:
            if in_range(args, event):
                fargs = (event[0], ' ' if event[0] == 1 else 's', event[1])
                count += 1
                print(form % fargs)
    return count

def print_future_events(args, future, width):
    count = 0
    if not args.nofuture:
        form = "%%%dd day%%c until %%s" % width
        for event in future:
            if in_range(args, event):
                fargs = (event[0], ' ' if event[0] == 1 else 's', event[1])
                count += 1
                print(form % fargs)
    return count

def print_totals(style, reverse, future, past):
    if style == "none":
        return
    elif style == "simple":
        count = future + past
        print("Total: %d event%s." % (count, ' ' if count == 1 else 's'))
    elif style == "categories" and reverse:
        print("%d future event%s." % (future, ' ' if future == 1 else 's'))
        print("%d past event%s." % (past, ' ' if past == 1 else 's'))
    elif style == "categories":
        print("%d past event%s." % (past, ' ' if past == 1 else 's'))
        print("%d future event%s." % (future, ' ' if future == 1 else 's'))
    elif style == "both":
        print_totals("categories", reverse, future, past)
        print_totals("simple", reverse, future, past)

if __name__ == "__main__":
    # Parse options with argparse
    argparser = argparse.ArgumentParser(description="List events by days since/until they happen(ed).")
    argparser.add_argument("-d", "--delta", type=int, default=0, help="Only print events whose days since/until is less than this argument. (0 for no limits)")
    argparser.add_argument("-D", "--reverse-delta", type=int, default=0, dest='rdelta', help="Only print events whose days since/until is greater than or equal to this argument. (default is 0)")
    argparser.add_argument("-r", "--reverse", action="store_true", help="Print the events in reverse order.")
    argparser.add_argument("-n", "--nopast", action="store_true", help="Don't print any events that have already happened.")
    argparser.add_argument("-N", "--nofuture", action="store_true", help="Don't print any events that haven't happened yet.")
    argparser.add_argument("-t", "--totals-style", nargs='?', choices=("none", "simple", "categories", "both"), default="none", dest="tstyle", help="Specify how you want %(prog)s to print event totals.")
    argparser.add_argument("-T", "--totals-only", action="store_false", dest="print_events", help="Print only the event totals; do not print any events.")
    argparser.add_argument("-A", "--total-all", action="store_true", dest="total_all", help="When printing totals, print them for all events in all files, not just the ones that were printed.")
    argparser.add_argument("input-file", nargs='*', help="Specify a input file. If none are specified, then eventlist.txt is used.")
    args = argparser.parse_args()

    # Perform sanity checks on arguments
    if args.delta < 0:
        print("The delta must be a positive integer.", file=sys.stderr)
        exit(1)

    if args.rdelta < 0:
        print("The reverse delta must be a positive integer.", file=sys.stderr)
        exit(1)

    if args.delta < args.rdelta:
        print("Warning: the deltas you specified will result in no events being printed.", file=sys.stderr)

    # Fetch event data
    past, future, width = get_events(getattr(args, "input-file"))

    if args.reverse:
        if args.print_events:
            future_total = print_future_events(args, reversed(future), width)
            past_total = print_past_events(args, reversed(past), width)

        if args.total_all:
            print_totals(args.tstyle, True, len(future), len(past))
        else:
            print_totals(args.tstyle, True, future_total, past_total)
    else:
        if args.print_events:
            future_total = print_past_events(args, past, width)
            past_total = print_future_events(args, future, width)

        if args.total_all:
            print_totals(args.tstyle, False, len(future), len(past))
        else:
            print_totals(args.tstyle, False, future_total, past_total)


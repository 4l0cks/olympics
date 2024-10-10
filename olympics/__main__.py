"""CLI public options."""

import argparse

from . import cli

parser = argparse.ArgumentParser(
    prog='olympics',
    description='Display various information about Olympics results',
)
parser.add_argument(
    'command',
    help='command to launch',
    choices=('countries', 'collective', 'individual'),
)
parser.add_argument(
    '--top',
    help='number of top elements to display',
    type=float,
    default=10,
)

def main(argv=None):
    args = parser.parse_args(argv)
    if (top := int(args.top)) < 0:
        raise argparse.ArgumentTypeError(f'{top} is not a positive number') #this line was a miss i had to implement a test to trigger the coverage on it
    match args.command:
        case 'countries':
            cli.top_countries(top) #was a miss
        case 'collective':
            cli.top_collective(top) #was a miss
        case 'individual':
            cli.top_individual(top) #was a miss


if __name__ == '__main__':  # pragma: no cover
    main()

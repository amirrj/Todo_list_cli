import functions
from parsers import parser


def main():
    # load data
    data = functions.load_data()
    # load args
    args = parser.parse_args()
    # execute functions
    args.func(args, data)


if __name__ == '__main__':
    main()

import argparse

def initialize_parser():
    
    parser = argparse.ArgumentParser()
    # parser.add_argument("-a", "--playadd",
    #                     help="Player Address",
    #                     required=False,
    #                     type=str)
    parser.add_argument("-p", "--players ",
                        help="Number of playing players",
                        required=True,
                        type=int)

    return parser.parse_args()
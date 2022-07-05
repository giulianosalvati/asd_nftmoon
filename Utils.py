import argparse

def initialize_parser():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--playadd",
                        help="Player Address",
                        required=True,
                        type=str)
    parser.add_argument("-20", "--erc20add ",
                        help="ERC20 Contract Address",
                        required=True,
                        type=str)
    parser.add_argument("-721", "--erc721 ",
                        help=" ERC721 Contract Address",
                        required=True,
                        type=str)

    return parser.parse_args()
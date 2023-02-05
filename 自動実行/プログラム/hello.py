import argparse

parser = argparse.ArgumentParser()
parser.add_argument('message', type=str)
args = parser.parse_args()

print("Hello {}.".format(args.message))

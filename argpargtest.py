import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("required", type=str)
    parser.add_argument("-hw", "--hello-world", type=int)
    parser.add_argument("-c", "--count", type=int)
    parser.add_argument("--text-color", type=int, nargs=3, metavar=("R", "G", "B"))

    args = parser.parse_args()
    print(args)

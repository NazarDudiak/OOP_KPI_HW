import argparse


def main():
    parser = argparse.ArgumentParser(description="Lab 02")
    parser.add_argument("sym", help="Type of operation")
    parser.add_argument("arg_1", help="The first argument to the operation")
    parser.add_argument("arg_2", help="The second argument to the operation")

    arg_1, sym, arg_2 = parser.parse_args().arg_1, parser.parse_args().sym, parser.parse_args().arg_2

    if arg_1.isnumeric() and arg_2.isnumeric():
        if sym == "add":
            print(int(arg_1) + int(arg_2))
        elif sym == "minus":
            print(int(arg_1) - int(arg_2))
        elif sym == "multiply":
            print(int(arg_1) * int(arg_2))
        elif sym == "devided":
            print(int(arg_1) / int(arg_2))
        else:
            print("Error! Unsupported operation.")
    else:
        print("Arguments are not numbers.")


if __name__ == "__main__":
    main()

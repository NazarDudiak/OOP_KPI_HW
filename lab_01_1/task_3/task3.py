import argparse


def main():
    parser = argparse.ArgumentParser(description="Lab 03")
    parser.add_argument("input_string", help="Input string")

    input_string = parser.parse_args().input_string
    list4equal = [""]
    status = True

    for i in range(0, len(input_string)):
        elem = input_string[i]

        if (elem != "-") and (elem != "+"):
            # print(">>>", elem)
            list4equal[len(list4equal)-1] = list4equal[len(list4equal)-1] + elem
        else:
            # print("<<<", elem)
            if list4equal[len(list4equal) - 1] == "-" or list4equal[len(list4equal) - 1] == "+":
                status = False
                break
            else:
                list4equal.append("")
                list4equal[len(list4equal) - 1] = list4equal[len(list4equal) - 1] + elem
    for i in list4equal:
        try:
            int(i)
        except ValueError:
            status = False
            break

    if status:
        print((status, sum(map(int, list4equal))))
    if not status:
        print((status, None))


if __name__ == "__main__":
    main()

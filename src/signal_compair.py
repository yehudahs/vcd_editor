import argparse
import re

# def find_next_match_scope(line_iter):
#     while line_iter
#
# def find_signal_alias_name(file, signal_path):
#     signal_list = signal_path.split('.')
#     curr_ident_level = 1
#     with open(file,'r') as f:
#         for line in f:
#             identation_level = line.find("$scope module ")
#             if identation_level != -1:  # we found a new scope
#                 scope_name = re.search(r"\$scope module (\S)+")
#                 if signal_list[identation_level] == scope_name:
#
#
#
#
# def find_first_diff(file1, file2, signal_alias):


def find_alias_in_cycle(alias, file):
    line = file.readline()
    while not line.startswith('#'):
        if line.rstrip().endswith(alias):
            return line
        line = file.readline()

    return None


def go_to_cycle(cycle, file):
    line = file.readline()
    while line:
        if line.startswith('#'):
            print(line)
        if not line.startswith('#' + cycle):
            line = file.readline()
            continue
        return line
    return None


def ffd(f1, f2, start1_cycle, start2_cycle, signal_alias):
    with open(f1) as file1, open(f2) as file2:

        line1 = file1.readline()
        line2 = file2.readline()
        val1 = line1
        val2 = line2
        while line1 and line2:

            # if we found some thing in val1, we need to go to the next cycles and
            # start searching from that location
            if val1:
                if not go_to_cycle(start1_cycle, file1):
                    print("didn't find the needed cycles in file1")

            # if we found some thing in val2, we need to go to the next cycles and
            # start searching from that location
            if val2:
                if not go_to_cycle(start2_cycle, file2):
                    print("didn't find the needed cycles in file1")
            print("continue on cycles {}(f1) and {}(f2)".format(start1_cycle, start2_cycle))

            val1 = find_alias_in_cycle(signal_alias, file1)
            val2 = find_alias_in_cycle(signal_alias, file2)

            if val1 != val2:
                print('start compair from cycle1 {} and cycle2 {}'.format(start1_cycle, start2_cycle))

            start1_cycle = str(int(start1_cycle) + 1)
            start2_cycle = str(int(start2_cycle) + 1)


def main():
    parser = argparse.ArgumentParser(description='Process args for banc')
    parser.add_argument('-f1', '--file1', required=True, help='the first file')
    parser.add_argument('-f2', '--file2', required=True, help='the second file')
    parser.add_argument('-st1', '--start1', required=True, help='the first cycle to search')
    parser.add_argument('-st2', '--start2', required=True, help='the second cycle to search')
    parser.add_argument('-s', '--signal_name', required=True,
                        help='signal path the need to tracked and compaired between the 2 files')
    args = parser.parse_args()
    ffd(args.file1, args.file2, args.start1, args.start2, args.signal_name)


if __name__ == '__main__':
    main()

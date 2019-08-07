from Verilog_VCD.Verilog_VCD import parse_vcd
import deepdiff
import json

import argparse

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


def ffd(f1, f2):
    siglist = list()
    for r in range(2, 4):
        for c in range(2, 4):
            for alu_inst in range(0, 8):
                siglist.append(hier)

    vcd1 = parse_vcd(f1, siglist=siglist)
    vcd2 = parse_vcd(f2, siglist=siglist)

    diff = deepdiff.DeepDiff(vcd1, vcd2)
    print(json.dumps(diff, indent=4))

    return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f1', '--file1', required=True, help='the first file')
    parser.add_argument('-f2', '--file2', required=True, help='the second file')
    args = parser.parse_args()
    ffd(args.file1, args.file2)


if __name__ == '__main__':
    main()

import os
import argparse


def clip(file, from_cycle, to_cycle):
    output_file, ext = os.path.splitext(os.path.basename(file))
    output_file = output_file + '-' + from_cycle + '-' + to_cycle + ext
    output_file = os.path.join(os.path.dirname(file), output_file)

    is_header = True
    is_body = False
    in_clip = False
    with open(file, 'r') as input_f, open(output_file, 'w') as output_f:
        for line in input_f:
            if line.startswith('#'):
                print('clipping cycle {}'.format(line))
                is_header = False
                is_body = True
                curr_cycle = line[1:].rstrip()
                if curr_cycle == from_cycle:
                    in_clip = True
                if curr_cycle == to_cycle:
                    break
            if is_header:
                output_f.write(line)

            if is_body:
                if in_clip:
                    output_f.write(line)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, help='the first file')
    parser.add_argument('-fr', '--from_cycle', required=True, help='clip from cycle')
    parser.add_argument('-to', '--to_cycle', required=True, help='clip to cycle')
    args = parser.parse_args()
    clip(args.file, args.from_cycle, args.to_cycle)


if __name__ == '__main__':
    main()

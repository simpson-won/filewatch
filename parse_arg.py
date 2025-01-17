"""args library"""
import argparse


def parse_args():
    """parse args and return values."""
    parser = argparse.ArgumentParser(
            prog='ProgramName',
            description='What the program does')
    parser.add_argument('-m', '--mode', action='store',
            dest='mode', type=str, default='unknown',
            help="allowed : walk or dog")
    parser.add_argument('-r', '--root', action='store',
            dest='root', type=str, default="/home/nfs_client")
    parser.add_argument('-f', '--filelist', action='store',
            dest='filelist', type=str, default="list1.txt")
    parser.add_argument('-p', '--perf', action='store',
            dest='perf', type=int, default=0)
    args = parser.parse_args()

    return args.mode, (args.root, args.filelist, args.perf)

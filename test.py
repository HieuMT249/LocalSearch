from search import LocalSearchStrategy
import argparse


parser = argparse.ArgumentParser(description='Run algorithm to visualize results with graphs containing surfaces and paths.')
parser.add_argument('--algorithm', type=str, choices=['RRH', 'SAS', 'LBS'], default='RRH', help='Algorithm to use (RRH, SAS, LBS)')
args = parser.parse_args()
LocalSearchStrategy.run_algorithm(args.algorithm)


mport argparse
import matplotlib.pyplot as plt
import os
import pandas as pd


def plot_length_distribution(input_file, out_path):
    df = pd.read_csv(input_file, sep='\t', header=None)
    lengths = df.iloc[:, 2] - df.iloc[:, 1]

    plt.hist(lengths, bins=20, rwidth=0.9)
    plt.xlabel('Sequence Length')
    plt.ylabel('Frequency')
    filename = os.path.basename(input_file)
    plt.title(f'Sequence Length Frequency for: {filename}')
    img_path = os.path.join(out_path, 'sequence_lengths.png')
    plt.savefig(img_path, format='png', dpi=300)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='plot_length_distribution',
                                     description='Plot a distribution of length in a bed file.')
    parser.add_argument('-f', help='input .bed file')
    parser.add_argument('-o', help='output dir where the histogram plot will be exported')
    args = parser.parse_args()
    plot_length_distribution(args.f, args.o)

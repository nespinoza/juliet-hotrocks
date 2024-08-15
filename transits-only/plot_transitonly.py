import matplotlib.pyplot as plt
import numpy as np
import juliet

def compare_data_with_model(dataset, results, instrument):

    t, f, ferr = dataset.times_lc[instrument], \
                 dataset.data_lc[instrument],\
                 dataset.errors_lc[instrument]

    model = results.lc.evaluate(instrument)

    plt.errorbar(t, f, ferr, fmt = '.', zorder = 1)
    plt.plot(t, model, 'r-', zorder =2)
    plt.show()

    plt.errorbar(t, (f - model) * 1e6, ferr*1e6, fmt = '.')
    plt.show()

if __name__ == '__main__':

    dataset = juliet.load(input_folder = 'transitonly', ld_laws = 'quadratic')
    results = dataset.fit(sampler = 'dynamic_dynesty', nthreads = 10, ecclim = 0.5, bound = 'multi', sample = 'rslice', n_live_points = 2000)

    # Check NIRSpec lightcurve fit:
    compare_data_with_model(dataset, results, 'NRS1') 

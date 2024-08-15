import numpy as np
import juliet

if __name__ == '__main__':

    dataset = juliet.load(input_folder = 'priors-and-posteriors', ld_laws = 'quadratic')
    dataset.fit(sampler = 'dynamic_dynesty', nthreads = 5, ecclim = 0.5)


def bootstrap(df, num_observations, resamples=1000):
    """Draw bootstrap resamples from the data frame from one ratings column.

    Parameters
    ----------
    num_observations: int
        The number of obserations you want to pull.

    resamples: int
      The number of bootstrap samples to draw from data frame.

    Returns
    -------
    bootstrap_samples: List[np.array]
      The bootsrap resamples from the column in the data frame.
      Each array is a single bootstrap sample.
    """
    bootstrap_samples = []
    for k in range(resamples):
        boot_indxs = np.random.randint(num_observations, size=num_observations)
        boot_sample = df[boot_indxs]
        bootstrap_samples.append(boot_sample)
    return bootstrap_samples

def bootstrap_confidence_interval(boostrap_samples, stat_function=np.mean, ci=95):
    """Calculate the CI of chosen sample statistic using bootstrap sampling.

    CI = confidence interval

    Parameters
    ----------
    bootstrap_sample: Numpy array
        Array of samples from bootstrap method

    stat_function: function, optional (default=np.mean)
        Function for calculating as sample statistic on data

    ci: int, optional (default=95)
        Percent of distribution encompassed by CI, 0<ci<100

    Returns
    -------
    tuple: lower_ci(float), upper_ci(float), bootstrap_samples_statistic(array)
        Lower and upper bounds of CI, sample stat from each bootstrap sample
    """
    bootstrap_samples_stat = list(map(stat_function, boostrap_samples))
    low_bound = (100. - ci) / 2
    high_bound = 100. - low_bound
    lower_ci, upper_ci = np.percentile(bootstrap_samples_stat,
                                       [low_bound, high_bound])
    return lower_ci, upper_ci, bootstrap_samples_stat

print(help("statistics"))

"""
O/p: Help on module statistics:
     
     NAME
         statistics - Basic statistics module.
     
     MODULE REFERENCE
         https://docs.python.org/3.12/library/statistics.html
     
         The following documentation is automatically generated from the Python
         source files.  It may be incomplete, incorrect or include features that
         are considered implementation detail and may vary between Python
         implementations.  When in doubt, consult the module reference at the
         location listed above.
     
     DESCRIPTION
         This module provides functions for calculating statistics of data, including
         averages, variance, and standard deviation.
     
         Calculating averages
         --------------------
     
         ==================  ==================================================
         Function            Description
         ==================  ==================================================
         mean                Arithmetic mean (average) of data.
         fmean               Fast, floating point arithmetic mean.
         geometric_mean      Geometric mean of data.
         harmonic_mean       Harmonic mean of data.
         median              Median (middle value) of data.
         median_low          Low median of data.
         median_high         High median of data.
         median_grouped      Median, or 50th percentile, of grouped data.
         mode                Mode (most common value) of data.
         multimode           List of modes (most common values of data).
         quantiles           Divide data into intervals with equal probability.
         ==================  ==================================================
     
         Calculate the arithmetic mean ("the average") of data:
     
         >>> mean([-1.0, 2.5, 3.25, 5.75])
         2.625
     
     
         Calculate the standard median of discrete data:
     
         >>> median([2, 3, 4, 5])
         3.5
     
     
         Calculate the median, or 50th percentile, of data grouped into class intervals
         centred on the data values provided. E.g. if your data points are rounded to
         the nearest whole number:
     
         >>> median_grouped([2, 2, 3, 3, 3, 4])  #doctest: +ELLIPSIS
         2.8333333333...
     
         This should be interpreted in this way: you have two data points in the class
         interval 1.5-2.5, three data points in the class interval 2.5-3.5, and one in
         the class interval 3.5-4.5. The median of these data points is 2.8333...
     
     
         Calculating variability or spread
         ---------------------------------
     
         ==================  =============================================
         Function            Description
         ==================  =============================================
         pvariance           Population variance of data.
         variance            Sample variance of data.
         pstdev              Population standard deviation of data.
         stdev               Sample standard deviation of data.
         ==================  =============================================
     
         Calculate the standard deviation of sample data:
     
         >>> stdev([2.5, 3.25, 5.5, 11.25, 11.75])  #doctest: +ELLIPSIS
         4.38961843444...
     
         If you have previously calculated the mean, you can pass it as the optional
         second argument to the four "spread" functions to avoid recalculating it:
     
         >>> data = [1, 2, 2, 4, 4, 4, 5, 6]
         >>> mu = mean(data)
         >>> pvariance(data, mu)
         2.5
     
     
         Statistics for relations between two inputs
         -------------------------------------------
     
         ==================  ====================================================
         Function            Description
         ==================  ====================================================
         covariance          Sample covariance for two variables.
         correlation         Pearson's correlation coefficient for two variables.
         linear_regression   Intercept and slope for simple linear regression.
         ==================  ====================================================
     
         Calculate covariance, Pearson's correlation, and simple linear regression
         for two inputs:
     
         >>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
         >>> y = [1, 2, 3, 1, 2, 3, 1, 2, 3]
         >>> covariance(x, y)
         0.75
         >>> correlation(x, y)  #doctest: +ELLIPSIS
         0.31622776601...
         >>> linear_regression(x, y)  #doctest:
         LinearRegression(slope=0.1, intercept=1.5)
     
     
         Exceptions
         ----------
     
         A single exception is defined: StatisticsError is a subclass of ValueError.
     
     CLASSES
         builtins.ValueError(builtins.Exception)
             StatisticsError
         builtins.object
             NormalDist
     
         class NormalDist(builtins.object)
          |  NormalDist(mu=0.0, sigma=1.0)
          |
          |  Normal distribution of a random variable
          |
          |  Methods defined here:
          |
          |  __add__(x1, x2)
          |      Add a constant or another NormalDist instance.
          |
          |      If *other* is a constant, translate mu by the constant,
          |      leaving sigma unchanged.
          |
          |      If *other* is a NormalDist, add both the means and the variances.
          |      Mathematically, this works only if the two distributions are
          |      independent or if they are jointly normally distributed.
          |
          |  __eq__(x1, x2)
          |      Two NormalDist objects are equal if their mu and sigma are both equal.
          |
          |  __getstate__(self)
          |      Helper for pickle.
          |
          |  __hash__(self)
          |      NormalDist objects hash equal if their mu and sigma are both equal.
          |
          |  __init__(self, mu=0.0, sigma=1.0)
          |      NormalDist where mu is the mean and sigma is the standard deviation.
          |
          |  __mul__(x1, x2)
          |      Multiply both mu and sigma by a constant.
          |
          |      Used for rescaling, perhaps to change measurement units.
          |      Sigma is scaled with the absolute value of the constant.
          |
          |  __neg__(x1)
          |      Negates mu while keeping sigma the same.
          |
          |  __pos__(x1)
          |      Return a copy of the instance.
          |
          |  __radd__ = __add__(x1, x2)
          |
          |  __repr__(self)
          |      Return repr(self).
          |
          |  __rmul__ = __mul__(x1, x2)
          |
          |  __rsub__(x1, x2)
          |      Subtract a NormalDist from a constant or another NormalDist.
          |
          |  __setstate__(self, state)
          |
          |  __sub__(x1, x2)
          |      Subtract a constant or another NormalDist instance.
          |
          |      If *other* is a constant, translate by the constant mu,
          |      leaving sigma unchanged.
          |
          |      If *other* is a NormalDist, subtract the means and add the variances.
          |      Mathematically, this works only if the two distributions are
          |      independent or if they are jointly normally distributed.
          |
          |  __truediv__(x1, x2)
          |      Divide both mu and sigma by a constant.
          |
          |      Used for rescaling, perhaps to change measurement units.
          |      Sigma is scaled with the absolute value of the constant.
          |
          |  cdf(self, x)
          |      Cumulative distribution function.  P(X <= x)
          |
          |  inv_cdf(self, p)
          |      Inverse cumulative distribution function.  x : P(X <= x) = p
          |
          |      Finds the value of the random variable such that the probability of
          |      the variable being less than or equal to that value equals the given
          |      probability.
          |
          |      This function is also called the percent point function or quantile
          |      function.
          |
          |  overlap(self, other)
          |      Compute the overlapping coefficient (OVL) between two normal distributions.
          |
          |      Measures the agreement between two normal probability distributions.
          |      Returns a value between 0.0 and 1.0 giving the overlapping area in
          |      the two underlying probability density functions.
          |
          |          >>> N1 = NormalDist(2.4, 1.6)
          |          >>> N2 = NormalDist(3.2, 2.0)
          |          >>> N1.overlap(N2)
          |          0.8035050657330205
          |
          |  pdf(self, x)
          |      Probability density function.  P(x <= X < x+dx) / dx
          |
          |  quantiles(self, n=4)
          |      Divide into *n* continuous intervals with equal probability.
          |
          |      Returns a list of (n - 1) cut points separating the intervals.
          |
          |      Set *n* to 4 for quartiles (the default).  Set *n* to 10 for deciles.
          |      Set *n* to 100 for percentiles which gives the 99 cuts points that
          |      separate the normal distribution in to 100 equal sized groups.
          |
          |  samples(self, n, *, seed=None)
          |      Generate *n* samples for a given mean and standard deviation.
          |
          |  zscore(self, x)
          |      Compute the Standard Score.  (x - mean) / stdev
          |
          |      Describes *x* in terms of the number of standard deviations
          |      above or below the mean of the normal distribution.
          |
          |  ----------------------------------------------------------------------
          |  Class methods defined here:
          |
          |  from_samples(data)
          |      Make a normal distribution instance from sample data.
          |
          |  ----------------------------------------------------------------------
          |  Readonly properties defined here:
          |
          |  mean
          |      Arithmetic mean of the normal distribution.
          |
          |  median
          |      Return the median of the normal distribution
          |
          |  mode
          |      Return the mode of the normal distribution
          |
          |      The mode is the value x where which the probability density
          |      function (pdf) takes its maximum value.
          |
          |  stdev
          |      Standard deviation of the normal distribution.
          |
          |  variance
          |      Square of the standard deviation.
     
         class StatisticsError(builtins.ValueError)
          |  Method resolution order:
          |      StatisticsError
          |      builtins.ValueError
          |      builtins.Exception
          |      builtins.BaseException
          |      builtins.object
          |
          |  Data descriptors defined here:
          |
          |  __weakref__
          |      list of weak references to the object
          |
          |  ----------------------------------------------------------------------
          |  Methods inherited from builtins.ValueError:
          |
          |  __init__(self, /, *args, **kwargs)
          |      Initialize self.  See help(type(self)) for accurate signature.
          |
          |  ----------------------------------------------------------------------
          |  Static methods inherited from builtins.ValueError:
          |
          |  __new__(*args, **kwargs) class method of builtins.ValueError
          |      Create and return a new object.  See help(type) for accurate signature.
          |
          |  ----------------------------------------------------------------------
          |  Methods inherited from builtins.BaseException:
          |
          |  __delattr__(self, name, /)
          |      Implement delattr(self, name).
          |
          |  __getattribute__(self, name, /)
          |      Return getattr(self, name).
          |
          |  __reduce__(...)
          |      Helper for pickle.
          |
          |  __repr__(self, /)
          |      Return repr(self).
          |
          |  __setattr__(self, name, value, /)
          |      Implement setattr(self, name, value).
          |
          |  __setstate__(...)
          |
          |  __str__(self, /)
          |      Return str(self).
          |
          |  add_note(...)
          |      Exception.add_note(note) --
          |      add a note to the exception
          |
          |  with_traceback(...)
          |      Exception.with_traceback(tb) --
          |      set self.__traceback__ to tb and return self.
          |
          |  ----------------------------------------------------------------------
          |  Data descriptors inherited from builtins.BaseException:
          |
          |  __cause__
          |      exception cause
          |
          |  __context__
          |      exception context
          |
          |  __dict__
          |
          |  __suppress_context__
          |
          |  __traceback__
          |
          |  args
     
     FUNCTIONS
         correlation(x, y, /, *, method='linear')
             Pearson's correlation coefficient
     
             Return the Pearson's correlation coefficient for two inputs. Pearson's
             correlation coefficient *r* takes values between -1 and +1. It measures
             the strength and direction of a linear relationship.
     
             >>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
             >>> y = [9, 8, 7, 6, 5, 4, 3, 2, 1]
             >>> correlation(x, x)
             1.0
             >>> correlation(x, y)
             -1.0
     
             If *method* is "ranked", computes Spearman's rank correlation coefficient
             for two inputs.  The data is replaced by ranks.  Ties are averaged
             so that equal values receive the same rank.  The resulting coefficient
             measures the strength of a monotonic relationship.
     
             Spearman's rank correlation coefficient is appropriate for ordinal
             data or for continuous data that doesn't meet the linear proportion
             requirement for Pearson's correlation coefficient.
     
         covariance(x, y, /)
             Covariance
     
             Return the sample covariance of two inputs *x* and *y*. Covariance
             is a measure of the joint variability of two inputs.
     
             >>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
             >>> y = [1, 2, 3, 1, 2, 3, 1, 2, 3]
             >>> covariance(x, y)
             0.75
             >>> z = [9, 8, 7, 6, 5, 4, 3, 2, 1]
             >>> covariance(x, z)
             -7.5
             >>> covariance(z, x)
             -7.5
     
         fmean(data, weights=None)
             Convert data to floats and compute the arithmetic mean.
     
             This runs faster than the mean() function and it always returns a float.
             If the input dataset is empty, it raises a StatisticsError.
     
             >>> fmean([3.5, 4.0, 5.25])
             4.25
     
         geometric_mean(data)
             Convert data to floats and compute the geometric mean.
     
             Raises a StatisticsError if the input dataset is empty,
             if it contains a zero, or if it contains a negative value.
     
             No special efforts are made to achieve exact results.
             (However, this may change in the future.)
     
             >>> round(geometric_mean([54, 24, 36]), 9)
             36.0
     
         harmonic_mean(data, weights=None)
             Return the harmonic mean of data.
     
             The harmonic mean is the reciprocal of the arithmetic mean of the
             reciprocals of the data.  It can be used for averaging ratios or
             rates, for example speeds.
     
             Suppose a car travels 40 km/hr for 5 km and then speeds-up to
             60 km/hr for another 5 km. What is the average speed?
     
                 >>> harmonic_mean([40, 60])
                 48.0
     
             Suppose a car travels 40 km/hr for 5 km, and when traffic clears,
             speeds-up to 60 km/hr for the remaining 30 km of the journey. What
             is the average speed?
     
                 >>> harmonic_mean([40, 60], weights=[5, 30])
                 56.0
     
             If ``data`` is empty, or any element is less than zero,
             ``harmonic_mean`` will raise ``StatisticsError``.
     
         linear_regression(x, y, /, *, proportional=False)
             Slope and intercept for simple linear regression.
     
             Return the slope and intercept of simple linear regression
             parameters estimated using ordinary least squares. Simple linear
             regression describes relationship between an independent variable
             *x* and a dependent variable *y* in terms of a linear function:
     
                 y = slope * x + intercept + noise
     
             where *slope* and *intercept* are the regression parameters that are
             estimated, and noise represents the variability of the data that was
             not explained by the linear regression (it is equal to the
             difference between predicted and actual values of the dependent
             variable).
     
             The parameters are returned as a named tuple.
     
             >>> x = [1, 2, 3, 4, 5]
             >>> noise = NormalDist().samples(5, seed=42)
             >>> y = [3 * x[i] + 2 + noise[i] for i in range(5)]
             >>> linear_regression(x, y)  #doctest: +ELLIPSIS
             LinearRegression(slope=3.09078914170..., intercept=1.75684970486...)
     
             If *proportional* is true, the independent variable *x* and the
             dependent variable *y* are assumed to be directly proportional.
             The data is fit to a line passing through the origin.
     
             Since the *intercept* will always be 0.0, the underlying linear
             function simplifies to:
     
                 y = slope * x + noise
     
             >>> y = [3 * x[i] + noise[i] for i in range(5)]
             >>> linear_regression(x, y, proportional=True)  #doctest: +ELLIPSIS
             LinearRegression(slope=3.02447542484..., intercept=0.0)
     
         mean(data)
             Return the sample arithmetic mean of data.
     
             >>> mean([1, 2, 3, 4, 4])
             2.8
     
             >>> from fractions import Fraction as F
             >>> mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])
             Fraction(13, 21)
     
             >>> from decimal import Decimal as D
             >>> mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
             Decimal('0.5625')
     
             If ``data`` is empty, StatisticsError will be raised.
     
         median(data)
             Return the median (middle value) of numeric data.
     
             When the number of data points is odd, return the middle data point.
             When the number of data points is even, the median is interpolated by
             taking the average of the two middle values:
     
             >>> median([1, 3, 5])
             3
             >>> median([1, 3, 5, 7])
             4.0
     
         median_grouped(data, interval=1.0)
             Estimates the median for numeric data binned around the midpoints
             of consecutive, fixed-width intervals.
     
             The *data* can be any iterable of numeric data with each value being
             exactly the midpoint of a bin.  At least one value must be present.
     
             The *interval* is width of each bin.
     
             For example, demographic information may have been summarized into
             consecutive ten-year age groups with each group being represented
             by the 5-year midpoints of the intervals:
     
                 >>> demographics = Counter({
                 ...    25: 172,   # 20 to 30 years old
                 ...    35: 484,   # 30 to 40 years old
                 ...    45: 387,   # 40 to 50 years old
                 ...    55:  22,   # 50 to 60 years old
                 ...    65:   6,   # 60 to 70 years old
                 ... })
     
             The 50th percentile (median) is the 536th person out of the 1071
             member cohort.  That person is in the 30 to 40 year old age group.
     
             The regular median() function would assume that everyone in the
             tricenarian age group was exactly 35 years old.  A more tenable
             assumption is that the 484 members of that age group are evenly
             distributed between 30 and 40.  For that, we use median_grouped().
     
                 >>> data = list(demographics.elements())
                 >>> median(data)
                 35
                 >>> round(median_grouped(data, interval=10), 1)
                 37.5
     
             The caller is responsible for making sure the data points are separated
             by exact multiples of *interval*.  This is essential for getting a
             correct result.  The function does not check this precondition.
     
             Inputs may be any numeric type that can be coerced to a float during
             the interpolation step.
     
         median_high(data)
             Return the high median of data.
     
             When the number of data points is odd, the middle value is returned.
             When it is even, the larger of the two middle values is returned.
     
             >>> median_high([1, 3, 5])
             3
             >>> median_high([1, 3, 5, 7])
             5
     
         median_low(data)
             Return the low median of numeric data.
     
             When the number of data points is odd, the middle value is returned.
             When it is even, the smaller of the two middle values is returned.
     
             >>> median_low([1, 3, 5])
             3
             >>> median_low([1, 3, 5, 7])
             3
     
         mode(data)
             Return the most common data point from discrete or nominal data.
     
             ``mode`` assumes discrete data, and returns a single value. This is the
             standard treatment of the mode as commonly taught in schools:
     
                 >>> mode([1, 1, 2, 3, 3, 3, 3, 4])
                 3
     
             This also works with nominal (non-numeric) data:
     
                 >>> mode(["red", "blue", "blue", "red", "green", "red", "red"])
                 'red'
     
             If there are multiple modes with same frequency, return the first one
             encountered:
     
                 >>> mode(['red', 'red', 'green', 'blue', 'blue'])
                 'red'
     
             If *data* is empty, ``mode``, raises StatisticsError.
     
         multimode(data)
             Return a list of the most frequently occurring values.
     
             Will return more than one result if there are multiple modes
             or an empty list if *data* is empty.
     
             >>> multimode('aabbbbbbbbcc')
             ['b']
             >>> multimode('aabbbbccddddeeffffgg')
             ['b', 'd', 'f']
             >>> multimode('')
             []
     
         pstdev(data, mu=None)
             Return the square root of the population variance.
     
             See ``pvariance`` for arguments and other details.
     
             >>> pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
             0.986893273527251
     
         pvariance(data, mu=None)
             Return the population variance of ``data``.
     
             data should be a sequence or iterable of Real-valued numbers, with at least one
             value. The optional argument mu, if given, should be the mean of
             the data. If it is missing or None, the mean is automatically calculated.
     
             Use this function to calculate the variance from the entire population.
             To estimate the variance from a sample, the ``variance`` function is
             usually a better choice.
     
             Examples:
     
             >>> data = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25]
             >>> pvariance(data)
             1.25
     
             If you have already calculated the mean of the data, you can pass it as
             the optional second argument to avoid recalculating it:
     
             >>> mu = mean(data)
             >>> pvariance(data, mu)
             1.25
     
             Decimals and Fractions are supported:
     
             >>> from decimal import Decimal as D
             >>> pvariance([D("27.5"), D("30.25"), D("30.25"), D("34.5"), D("41.75")])
             Decimal('24.815')
     
             >>> from fractions import Fraction as F
             >>> pvariance([F(1, 4), F(5, 4), F(1, 2)])
             Fraction(13, 72)
     
         quantiles(data, *, n=4, method='exclusive')
             Divide *data* into *n* continuous intervals with equal probability.
     
             Returns a list of (n - 1) cut points separating the intervals.
     
             Set *n* to 4 for quartiles (the default).  Set *n* to 10 for deciles.
             Set *n* to 100 for percentiles which gives the 99 cuts points that
             separate *data* in to 100 equal sized groups.
     
             The *data* can be any iterable containing sample.
             The cut points are linearly interpolated between data points.
     
             If *method* is set to *inclusive*, *data* is treated as population
             data.  The minimum value is treated as the 0th percentile and the
             maximum value is treated as the 100th percentile.
     
         stdev(data, xbar=None)
             Return the square root of the sample variance.
     
             See ``variance`` for arguments and other details.
     
             >>> stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
             1.0810874155219827
     
         variance(data, xbar=None)
             Return the sample variance of data.
     
             data should be an iterable of Real-valued numbers, with at least two
             values. The optional argument xbar, if given, should be the mean of
             the data. If it is missing or None, the mean is automatically calculated.
     
             Use this function when your data is a sample from a population. To
             calculate the variance from the entire population, see ``pvariance``.
     
             Examples:
     
             >>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
             >>> variance(data)
             1.3720238095238095
     
             If you have already calculated the mean of your data, you can pass it as
             the optional second argument ``xbar`` to avoid recalculating it:
     
             >>> m = mean(data)
             >>> variance(data, m)
             1.3720238095238095
     
             This function does not check that ``xbar`` is actually the mean of
             ``data``. Giving arbitrary values for ``xbar`` may lead to invalid or
             impossible results.
     
             Decimals and Fractions are supported:
     
             >>> from decimal import Decimal as D
             >>> variance([D("27.5"), D("30.25"), D("30.25"), D("34.5"), D("41.75")])
             Decimal('31.01875')
     
             >>> from fractions import Fraction as F
             >>> variance([F(1, 6), F(1, 2), F(5, 3)])
             Fraction(67, 108)
     
     DATA
         __all__ = ['NormalDist', 'StatisticsError', 'correlation', 'covariance...
         __annotations__ = {'_sqrt_bit_width': <class 'int'>}
     
     FILE
         d:\programming\python\python\interpreter\lib\statistics.py
     
     
     None
"""
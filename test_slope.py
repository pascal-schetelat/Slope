import pytest


def test_interval_plot():
    import matplotlib
    matplotlib.use('Agg')
    from plotSlope import slope
    import pandas as pd
    import os


    data_EU = pd.read_csv(os.path.join('data','EU_GDP_2007_2013.csv'),
                          index_col=0,
                          na_values='-')

    EU_color = {
        "France": 'b',
        'Germany': 'r',
        'Ireland': 'chocolate',
        'United Kingdom': 'purple'
    }

    if os.path.exists('test_interval.png'):
        os.remove('test_interval.png')


    f = slope(  data_EU.ix[:,:-3] / 1000,
                kind='interval',
                savename='test_interval.png', dpi=200,
                height=18,
                width=30,
                font_size=20,
                color=EU_color,
                title=  u'European GPD until 2010 and forecasts at market prices (billions of Euro) source : EUROSTAT')

    assert os.path.exists('test_interval.png')

    if os.path.exists('test_interval.png'):
        os.remove('test_interval.png')



def test_ordinal_plot():
    import matplotlib
    matplotlib.use('Agg')
    from plotSlope import slope
    import numpy as np
    import pandas as pd
    import os

    if os.path.exists('test_ordinal.png'):
        os.remove('test_ordinal.png')


    df = pd.DataFrame( np.random.normal(loc=np.ones(shape=[20,30])*np.arange(30)))
    df.rename(columns = lambda el : str(el),index =lambda el : str(el),inplace=True)

    f = slope(df.T,width =10,height= 8,kind='ordinal',savename='test_ordinal.png',dpi=200,color={'10':'red','27':'blue'},marker=None)

    assert os.path.exists('test_ordinal.png')

    if os.path.exists('test_ordinal.png'):
        os.remove('test_ordinal.png')
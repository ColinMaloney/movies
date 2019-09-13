def get_data_frames():
    '''
    This scrapes the site www.the-numbers.com for the years of 2009 until 2019
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    years = range(2009,2020)
    dfs = []
    for year in years:
        url = f'https://www.the-numbers.com/box-office-records/worldwide/all-movies/cumulative/released-in-{year}'
        time.sleep(2)
        html = requests.get(url, headers=headers) # avoid the 403
        yearly_df = pd.read_html(html.text)[1]
        yearly_df.dropna(inplace=True)
        yearly_df['year'] = year
        dfs.append(yearly_df)
    return dfs

frames = get_data_frames()
overall_df = pd.concat(frames, axis=0)

def get_domestic_per_year(dataframe):
    '''
    This function breaks out the Domestic Box Office Gorss numbers by year
    and returns the information in a dictionary
    '''
    domestic_gross_dict = OrderedDict()
    for year in range(2009,2020):
        key = 'year' + str(year)
        domestic_gross_dict[key] = years_split['year'+str(year)]['Domestic Box Office'].sum()
    return domestic_gross_dict

dom_gross = get_domestic_per_year(final_df)

def get_international_per_year(dataframe):
     '''
    This function breaks out the International Box Office Gorss numbers by year
    and returns the information in a dictionary
    '''
    inter_gross_dict = OrderedDict()
    for year in range(2009,2020):
        key = 'year' + str(year)
        inter_gross_dict[key] = years_split['year'+str(year)]['International Box Office'].sum()
    return inter_gross_dict

inter_gross = get_international_per_year(final_df)

#Graphing the two dictionaries
def plot_gross_dom_vs_inter(dict1,dict2):
    fig,ax = plt.subplots(figsize=(12,7),sharex=True,sharey=True)
    for year in range(2009,2020):
        ax.bar(year,dom_gross['year'+str(year)], color='blue')
        ax.bar(year,inter_gross['year'+str(year)], color='red',alpha=.5)
        if year ==2019:
            ax.bar(year,dom_gross['year'+str(year)], color='blue',label='Domestic')
            ax.bar(year,inter_gross['year'+str(year)], color='red',alpha=.5,label='International')
    ax.set_xlabel = ('Years')
    ax.set_ylabel('Money Grossed')
    ax.set_title('Domestic and International Gross Per Year')
    ax.legend(loc='best')
    return

plot_gross_dom_vs_inter(dom_gross,inter_gross)

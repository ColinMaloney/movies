def clean_money(value):
    return (int(value.replace('$','').replace(',','')))


final_df['Worldwide Box Office'] = final_df['Worldwide Box Office'].map(clean_money)
final_df['Domestic Box Office'] = final_df['Domestic Box Office'].map(clean_money)
final_df['International Box Office'] = final_df['International Box Office'].map(clean_money)

final_df['DomesticShare'] = final_df['DomesticShare'].map(lambda x : float(x.replace('%','')))

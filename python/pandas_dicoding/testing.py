import pandas as pd


# city_names = [['Jakarta', 'Bandung', 'Makassar',
#               'Surabaya', 'Medan', 'Yogyakarta']]

# df = pd.DataFrame(city_names, columns=[
#                   'kota', 'kabupaten', 'provinsi', 'negara', 'benua', 'bumi'])

# df_index = df(index)


city_names = ['Jakarta', 'Bandung', 'Makassar',
              'Surabaya', 'Medan', 'Yogyakarta']

df = pd.Series(city_names, index=[
    'kota', 'kabupaten', 'provinsi', 'negara', 'benua', 'bumi'])

print(df)

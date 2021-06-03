import pandas as pd


def get_age():
    df = pd.read_csv('data.csv')
    return df.age.astype('int')


ages = get_age()

print('STARTING TEST...')
assert all(isinstance(x, int) for x in ages)
print('...TEST FINISHED!!!')

import pandas

df = pandas.read_csv("dataset_students.csv")
exclude_enrolled = df.loc[df['Target'] != 'Enrolled']
sample = exclude_enrolled.sample(20)
sample.to_csv("sample.csv")
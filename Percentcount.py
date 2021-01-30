import pandas as pd
df = pd.read_csv('PK03-control_Unique_7aaSeqonly.csv')

sample = df[['Peptide1','Count']]
grouped = sample.groupby('Peptide1')

sum_grouped = grouped.sum()
total = sum_grouped['Count'].sum()

sum_grouped['Percentage'] = sum_grouped.Count / total * 100

print(sum_grouped)

writer = pd.ExcelWriter('PK03-control_7aaseqpercentcount.xlsx', engine='xlsxwriter')
sum_grouped.to_excel(writer, sheet_name='Sheet1')
writer.save()
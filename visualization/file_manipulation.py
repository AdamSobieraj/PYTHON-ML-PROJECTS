import pandas as pd
from xlsxwriter import Workbook

print("---------------------excel import---------------------------")
df = pd.read_excel('../dataset/fileman/myExcelFile.xlsx', sheet_name='my_data')
print(df)

print("---------------------excel write---------------------------")
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='my_dfs')
df.to_excel(writer, sheet_name='my_dfs', startcol=6, startrow=5, index=False)

writer._save()

print("---------------------excel write---------------------------")
writer = pd.ExcelWriter('many_sheets.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='my_df1')
df.to_excel(writer, sheet_name='my_df2')

writer._save()

print("---------------------excel write chart---------------------------")
writer = pd.ExcelWriter('add_chart.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='my_chart')

workbook = writer.book
worksheet = writer.sheets['my_chart']
#linear
chart = workbook.add_chart({'type':'line'})

def grab_series(df, sheet_name, colname, startcol=0, startrow=0):

    col_index = df.columns.tolist().index(colname)
    col_letter = chr(ord('@')+(col_index+2+startcol))
    first_row = startrow + 2
    last_row = startrow + 1 + len(df)
    return f"='{sheet_name}'!{col_letter}{first_row}:{col_letter}{last_row}"

chart.add_series({'values':grab_series(df,'my_chart','B')})

chart.set_x_axis({
    'name': 'x^2',
    'name_font': {'size': 14, 'bold': True},
    'num_font':  {'italic': True },
})

chart.set_legend({'none': True})

worksheet.insert_chart('F2', chart)

writer._save()
# workbook.close()

print("---------------------excel data manipulation---------------------------")
writer = pd.ExcelWriter('conditional_format.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='my_conditional')

workbook = writer.book
worksheet = writer.sheets['my_conditional']

format1 = workbook.add_format({'bg_color':   '#FFC7CE',
                               'font_color': '#9C0006'})

worksheet.conditional_format("D2:D12",{'type': 'cell',
                                      'criteria':'>=',
                                      'value':300,
                                      'format':format1})

worksheet.write_string('A16','Podaj liczbę całkowitą większą od 0:')

worksheet.data_validation('B16', {
    'validate':'integer',
    'criteria':'>',
    'value':0
})

worksheet.set_column('A:A',35)

writer._save()
# workbook.close()


print("---------------------excel end---------------------------")

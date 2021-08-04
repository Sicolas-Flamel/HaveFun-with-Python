# 说明： 
# normal  为 工厂库存 = 预期库存 一致的列表
# profit  为 工厂库存 > 预期库存 的列表
# loss    为 工厂库存 < 预期库存 一致的列表


name = 'factory'
df1 = pd.DataFrame({'正常': normal}) 
df2 = pd.DataFrame({'盘盈': profit}) 
df3 = pd.DataFrame({'盘亏': loss}) 

writer = pd.ExcelWriter('{}对比.xlsx'.format(name), engine='xlsxwriter')

df1.to_excel(writer, sheet_name = '正常', index = False)
df2.to_excel(writer, sheet_name = '盘盈', index = False)
df3.to_excel(writer, sheet_name = '盘亏', index = False)

writer.save()

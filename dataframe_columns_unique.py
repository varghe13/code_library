from pandas.api.dtype import is_numeric_dtype
def column_stat(df):
  col_stat ={}
  for col in df.columns:
    if not is_numeric_dtype(df[col]):
      col_stat.update({col:list(df[col].unique())})
  return col_stat

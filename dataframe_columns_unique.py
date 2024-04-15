col_stat ={}
def column_stat(df):
  for col in df.columns:
    if df[col].dtype=="object":
      col_stat.update({col:list(df[col].unique())})
  return col_stat

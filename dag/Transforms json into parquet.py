import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# write data
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
table = pa.Table.from_pandas(df, preserve_index=False)
pq.write_table(
    table, '/tmp/df.parquet', coerce_timestamps='ms',     
    allow_truncated_timestamps=True
)

# read data
df = pq.read_pandas('/tmp/df.parquet').to_pandas()
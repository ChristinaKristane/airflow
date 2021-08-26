from json2parquet import load_json, ingest_data, write_parquet, write_parquet_dataset

# Loading JSON to a PyArrow RecordBatch (schema is optional as above)
load_json(input_filename, schema)

# Working with a list of dictionaries
ingest_data(input_data, schema)

# Working with a list of dictionaries and custom field names
field_aliases = {'my_column': 'my_updated_column_name', "my_int": "my_integer"}
ingest_data(input_data, schema, field_aliases)

# Writing Parquet Files from PyArrow Record Batches
write_parquet(data, destination)

# You can also pass any keyword arguments that PyArrow accepts
write_parquet(data, destination, compression='snappy')

# You can also write partitioned date
write_parquet_dataset(data, destination_dir, partition_cols=["foo", "bar", "baz"])
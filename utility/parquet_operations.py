import pyarrow.parquet as pq
import pyarrow as pa
import pyarrow.compute as pc
from typing import List


# class to do operations on parquet tables
# TODO: Add support for multiple files in case of partitioned datasets
# TODO: Add support for compressed files
class ParquetOperations:
    def __init__(self, table: pa.Table) -> None:
        self.table = table

    # Function to define print function for the class
    def __str__(self) -> str:
        return f"ParquetOperations({self.table})"

    # Function to return the metadata of the parquet table
    def metadata(self) -> dict:
        return self.schema().metadata

    # Function to return the number of columns in the parquet table
    def num_columns(self) -> int:
        return self.table.num_columns

    # Function to return the number of rows in the parquet table
    def num_rows(self) -> int:
        return self.table.num_rows

    # Function to return the schema of the parquet table
    def schema(self) -> pa.Schema:
        return self.table.schema
    
    def column_names(self) -> list:
        return self.schema().names
    
    def table_columns(self) -> list:
        return [{"name": col, "label": col, "field": col} for col in self.column_names()]

    # Function to return rows as list of dictionaries
    def rows(self, limit: int = None) -> list:
        return self.table.to_pylist() if limit is None else self.table.take([i for i in range(min(limit,self.num_rows()))]).to_pylist()[:limit]
    
    # Function to return max and min lenghts of values in string columns
    def string_lengths(self) -> List[dict]:
        return [{col: pc.max(pc.binary_length(self.table[col])).as_py() for col in self.column_names() if self.table[col].type == pa.string()},
                {col: pc.min(pc.binary_length(self.table[col])).as_py() for col in self.column_names() if self.table[col].type == pa.string()}]
    
    # Function to return max and min lengths of numeric columns
    def numeric_lengths(self) -> List[dict]:
        return [{col: pc.max(self.table[col]).as_py() for col in self.column_names() if self.table[col].type != pa.string()},
                {col: pc.min(self.table[col]).as_py() for col in self.column_names() if self.table[col].type != pa.string()}]
    
    # Function to return the number of null values in each column
    def null_counts(self) -> dict:
        return {col: self.table[col].null_count for col in self.column_names()}
    

if __name__ == "__main__":
    records = [{
    "name": "Thomas",
    "age": 28
    },
    {   "name": "John","age": 30},
    {   "name": "James","age": 25}
    ]
    # Function to make pyarrow dataframe from records
    def make_dataframe(records) -> pa.Table:
        return pa.Table.from_pylist(records)
    
    df = make_dataframe(records)
    pq.write_table(df, 'test.parquet')
    # df.write_table('test.parquet')

from pathlib import Path
import pyogrio
import pyarrow as pa
import pyarrow.parquet as pq

# Project directories
project_dir = Path(__file__).resolve().parent.parent

gdb_path = (
    project_dir
    / "data"
    / "S_USA.Fire_FPA_FOD_7th_Fires.gdb"
    / "S_USA.Fire_FPA_FOD_7th_Fires.gdb"
)

output_path = project_dir / "data" / "wildfires.parquet"

chunk_size = 50000
total_records = 0
writer = None
schema = None

try:
    while True:
        # Read a chunk without geometry
        df = pyogrio.read_dataframe(
            gdb_path,
            layer="Fire_FPA_FOD_7th_Fires",
            skip_features=total_records,
            max_features=chunk_size,
            read_geometry=False
        )

        if df.empty:
            break

        # Convert the chunk to Arrow
        table = pa.Table.from_pandas(
            df,
            preserve_index=False
        )

        if writer is None:
            # Establish the schema with the first chunk
            schema = table.schema

            writer = pq.ParquetWriter(
                output_path,
                schema,
                compression="snappy"
            )
        else:
            # Make subsequent chunks match the original schema
            table = table.cast(schema)

        writer.write_table(table)

        total_records += len(df)
        print(f"Converted records: {total_records}")

finally:
    if writer is not None:
        writer.close()

print(f"\nConversion completed: {total_records} records")
print(f"Saved to: {output_path}")

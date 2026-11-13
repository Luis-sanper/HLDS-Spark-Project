
from pathlib import Path
import pyogrio

# Locate the project folder
project_dir = Path(__file__).resolve().parent.parent

# Locate the extracted geodatabase
gdb_path = (
    project_dir
    / "data"
    / "S_USA.Fire_FPA_FOD_7th_Fires.gdb"
    / "S_USA.Fire_FPA_FOD_7th_Fires.gdb"
)

print("Geodatabase found:", gdb_path.exists())

# Display available layers
layers = pyogrio.list_layers(gdb_path)

print("\nAvailable layers:")
for layer in layers:
    print(layer)

# Display information about each layer
for layer_name, geometry_type in layers:
    info = pyogrio.read_info(gdb_path, layer=layer_name)

    print(f"\nLayer: {layer_name}")
    print("Number of records:", info["features"])
    print("Geometry type:", geometry_type)
    print("Number of attributes:", len(info["fields"]))

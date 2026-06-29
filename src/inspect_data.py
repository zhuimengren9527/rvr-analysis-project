from pathlib import Path
import pandas as pd

def inspect_data(file_path):

    path = Path(file_path)

    if not path.exists():
        print("文件不存在")

        return
    
    print(f"文件名称:{path.name}")

    file_size = path.stat().st_size

    if file_size < 1024:
        print(f"文件大小为:{file_size} Byte")
    elif file_size < 1024**2:
        print(f"文件大小为:{file_size/1024:.2f} KB")
    elif file_size < 1024**3:
        print(f"文件大小为:{file_size/1024**2:.2f} MB")

    return
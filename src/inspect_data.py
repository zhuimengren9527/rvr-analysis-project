from datetime import datetime
from pathlib import Path
import pandas as pd

def inspect_data(file_path):

    # 创建文件对象
    path = Path(file_path)

    # 判断文件是否存在
    if not path.exists():
        print("文件不存在")

        return
    # 打印文件名称
    print(f"文件名称:{path.name}")

    # 获取文件大小
    file_size = path.stat().st_size

    if file_size < 1024:
        print(f"文件大小为:{file_size} Byte")
    elif file_size < 1024**2:
        print(f"文件大小为:{file_size/1024:.2f} KB")
    elif file_size < 1024**3:
        print(f"文件大小为:{file_size/1024**2:.2f} MB")
    else:
        print(f"文件大小为: {file_size / 1024**3:.2f} GB")

    print(f"文件类型:{path.suffix}")

    # 获取文件修改时间
    modified_time = path.stat().st_mtime
    modified_time = datetime.fromtimestamp(modified_time)
    print(f"文件修改时间:{modified_time:%Y-%m-%d %H:%M:%S}")
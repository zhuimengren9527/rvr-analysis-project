from datetime import datetime
from pathlib import Path
import pandas as pd


# ===================================================
# 提取文件信息（名称、大小、修改时间）
# ===================================================

def get_file_info(path):
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


    # =============================================================
    # 文件预览
    # =============================================================

def preview_file(path):

    with open(path,'r',encoding='latin1') as f:

        print(f"\n预览数据前10行:\n")
        lines = []
        for i in range(10):
            line = f.readline()
            lines.append(line)
            print(repr(line))
    return lines

    # =============================================================
    # 显示文件分隔符
    # =============================================================
def detect_separator(lines):

    sample_text = "".join(lines)

    if '\t' in sample_text:
        print("\n检测到分隔符：Tab (\\t)")
    elif ',' in sample_text:
        print("\n检测到分隔符：,")
    elif ';' in sample_text:
        print("\n检测到分号：;")
    elif ' ' in sample_text:
        print("\n检测到空格：空格")
    return

def inspect_data(file_path):

# ===========================================================
# 创建文件对象并判断文件是否存在（主函数）
# =========================================================== 

    path = Path(file_path)

    if not path.exists():
        print("文件不存在")
        return

    # 调用各函数工具
    get_file_info(path)
    lines = preview_file(path)
    detect_separator(lines)



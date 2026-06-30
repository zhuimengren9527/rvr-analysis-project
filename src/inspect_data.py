from datetime import datetime
from pathlib import Path
import chardet


# ===================================================
# 文件编码检测
# ===================================================

def detect_encoding(path):

    with open(path,'rb') as f:

        raw_data = f.read()
        result = chardet.detect(raw_data)

    print(f"文件编码推测:{result}")
    return result


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
            print(f"第{i+1}行:{repr(line)}")
    return lines


# =============================================================
# 显示文件分隔符
# =============================================================
def detect_separator(lines):

    sample_text = "".join(lines)

    if '\t' in sample_text:
        print("检测到Tab \\t")
        return '\t'

    elif ',' in sample_text:
        print("检测到逗号")
        return ','

    elif ';' in sample_text:
        print("检测到分号")
        return ';'

    elif ' ' in sample_text:
        print("检测到空格")
        return ' '

    print("未识别到常见分隔符")
    return None


# =============================================================
# 检测列名所在的行是第几行
# =============================================================
def detect_header_line(lines):
    print("列名所在行：")

    for index,line in enumerate(lines,start=1):
        if 'CREATEDATE' in line and 'SITE' in line:
            print(f"第{index}行")
            return index
    print('未识别到列名行')
    return None


# =============================================================
# 提取列名
# =============================================================
def extract_columns(lines, separator, header_index):
    if separator is None or header_index is None:
        print("无法提取列名")
        return None

    column_names = lines[header_index - 1].strip().split(separator)
    print(f"该文件的列名为: {column_names}")
    return column_names


# ===========================================================
# 创建文件对象并判断文件是否存在（主函数）
# =========================================================== 

def inspect_data(file_path):

    path = Path(file_path)

    if not path.exists():
        print("文件不存在")
        return
# ===========================================================
# # 调用各函数工具
# =========================================================== 
    
    get_file_info(path)
    lines = preview_file(path)
    detect_encoding(path)
    separator = detect_separator(lines)
    header_index = detect_header_line(lines)
    extract_columns(lines,separator,header_index)



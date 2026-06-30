from pathlib import Path
import pandas as pd

from inspect_data import (
    detect_encoding,
    detect_separator,
    detect_header_line,
    preview_file
)

def load_data(file_path):

    path = Path(file_path)

    encoding_result = detect_encoding(path)
    encoding = encoding_result['encoding']
    lines = preview_file(path)
    separator = detect_separator(lines)
    header_index = detect_header_line(lines)
    skip = header_index - 1
    
    df = pd.read_csv(file_path,encoding=encoding,sep=separator,skiprows=skip)
    
    print(f"数据读取成功: {df.shape[0]}行，{df.shape[1]}列")
    return df
    

   
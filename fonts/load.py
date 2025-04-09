#!/usr/bin/env python3
import os
import requests
from urllib.parse import urlparse

def download_font(url, save_dir='fonts'):
    """
    下载字体文件并保存到指定目录
    
    Args:
        url: 字体文件的URL
        save_dir: 保存目录，默认为'fonts'
    """
    # 创建保存目录
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # 从URL中获取文件名
    filename = os.path.basename(urlparse(url).path)
    save_path = os.path.join(save_dir, filename)
    
    # 下载文件
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        
        # 保存文件
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"成功下载: {filename}")
    except Exception as e:
        print(f"下载失败 {filename}: {str(e)}")

# Great Vibes 字体URL
great_vibes_urls = [
    "https://fonts.gstatic.com/s/greatvibes/v19/RWmMoKWR9v4ksMfaWd_JN9XIiaQ6DQ.woff2",
    "https://fonts.gstatic.com/s/greatvibes/v19/RWmMoKWR9v4ksMfaWd_JN9XBiaQ6DQ.woff2",
    "https://fonts.gstatic.com/s/greatvibes/v19/RWmMoKWR9v4ksMfaWd_JN9XJiaQ6DQ.woff2",
    "https://fonts.gstatic.com/s/greatvibes/v19/RWmMoKWR9v4ksMfaWd_JN9XKiaQ6DQ.woff2",
    "https://fonts.gstatic.com/s/greatvibes/v19/RWmMoKWR9v4ksMfaWd_JN9XLiaQ6DQ.woff2",
    "https://fonts.gstatic.com/s/greatvibes/v19/RWmMoKWR9v4ksMfaWd_JN9XFiaQ.woff2"
]

# Modern Antiqua 字体URL
modern_antiqua_urls = [
    "https://fonts.gstatic.com/s/modernantiqua/v24/NGStv5TIAUg6Iq_RLNo_2dp1sL1NYWqEcw.woff2",
    "https://fonts.gstatic.com/s/modernantiqua/v24/NGStv5TIAUg6Iq_RLNo_2dp1sL1DYWo.woff2"
]

# 下载所有字体文件
print("开始下载 Great Vibes 字体...")
for url in great_vibes_urls:
    download_font(url)

print("\n开始下载 Modern Antiqua 字体...")
for url in modern_antiqua_urls:
    download_font(url)

print("\n所有字体下载完成！")

#!/usr/bin/env python3
import os
import time
import requests
from urllib.parse import urlparse
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def download_font(url, save_dir='fonts', max_retries=3):
    """
    下载字体文件并保存到指定目录，包含重试机制
    
    Args:
        url: 字体文件的URL
        save_dir: 保存目录，默认为'fonts'
        max_retries: 最大重试次数，默认为3
    """
    # 创建保存目录
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # 从URL中获取文件名
    filename = os.path.basename(urlparse(url).path)
    save_path = os.path.join(save_dir, filename)
    
    # 如果文件已存在，跳过下载
    if os.path.exists(save_path):
        print(f"文件已存在，跳过下载: {filename}")
        return True
    
    # 配置重试策略
    retry_strategy = Retry(
        total=max_retries,
        backoff_factor=1,
        status_forcelist=[500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)
    http.mount("http://", adapter)
    
    # 下载文件
    for attempt in range(max_retries):
        try:
            print(f"尝试下载 {filename} (下载地址：{url}")
            response = http.get(url, timeout=30)
            response.raise_for_status()
            
            # 保存文件
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"成功下载: {filename}")
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"下载失败 {filename}: {str(e)}")
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 5  # 递增等待时间
                print(f"等待 {wait_time} 秒后重试...")
                time.sleep(wait_time)
            else:
                print(f"达到最大重试次数，放弃下载 {filename}")
                return False

# 从url.txt中读取字体URL
with open('url.txt', 'r') as f:
    urls = [url.strip() for url in f.readlines()]  # 使用strip()去除每行的换行符和空白字符

# 下载所有字体文件
print("开始下载 ZCOOL KuaiLe 字体...")
for url in urls:
    if url:  # 确保URL不为空
        download_font(url)

print("\n所有字体下载完成！")

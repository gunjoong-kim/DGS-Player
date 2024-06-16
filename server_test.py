import numpy as np
import requests
import os
import time

def download_and_load_npz(url_base, file_count, save_dir='downloads'):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # 각 파일에 대해 반복
    for i in range(file_count):
        file_name = f"frame_{i}.npz"
        url = f"{url_base}/{file_name}"
        
        # 파일 다운로드
        response_start = time.time()
        response = requests.get(url)
        response_end = time.time()
        print(f"Response time: {response_end - response_start}")
        
        if response.status_code == 200:
            file_path = os.path.join(save_dir, file_name)
            
            write_start = time.time()
            with open(file_path, 'wb') as f:
                f.write(response.content)
            write_end = time.time()
            print(f"Write time: {write_end - write_start}")
            print(f"{file_name} downloaded and saved to {file_path}")
            
            # 파일 로드
            load_start = time.time()
            data = dict(np.load(file_path))
            load_end = time.time()
            print(f"Load time: {load_end - load_start}")
            
            # npz 파일 내 데이터 출력 (예: 'data'라는 키를 가진 데이터에 접근)
            print(data['means3D'][0])
                
        else:
            print(f"Failed to download {file_name} from {url}")

# 사용 예시
url_base = "http://css5.yonsei.ac.kr:8502/gunjoong/volumetric_test/frames/"
download_and_load_npz(url_base, 150)
import os

def delete_files_ending_with_space2md():
    # 현재 디렉토리부터 시작하여 모든 하위 디렉토리를 순회합니다.
    for root, dirs, files in os.walk('.'):
        for file in files:
            # 파일 이름이 " 2.md"로 끝나는지 확인합니다.
            if file.endswith(" 2.md"):
                file_path = os.path.join(root, file)
                print(f"Deleting: {file_path}")
                os.remove(file_path)

if __name__ == "__main__":
    delete_files_ending_with_space2md()


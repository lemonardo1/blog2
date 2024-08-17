import cv2
import numpy as np
import os

# 이미지를 읽어옴 (컬러 이미지로 읽기)
image = cv2.imread('path_to_image.jpg', cv2.IMREAD_COLOR)

# 이미지를 불러오고 전처리하는 함수
def load_and_preprocess_image(image_path, img_size=(64, 64)):
    # 이미지 파일을 읽어옴
    image = cv2.imread(image_path)
    
    # 이미지를 지정된 크기로 리사이즈
    image = cv2.resize(image, img_size)
    
    # 이미지를 float32 타입으로 변환하고, 0과 1 사이의 값으로 정규화
    image = image.astype('float32') / 255.0
    
    return image

# 데이터셋을 생성하는 함수
def create_dataset(data_dir, img_size=(64, 64)):
    images = []  # 이미지 배열
    labels = []  # 레이블 배열
    
    # 각 카테고리('malignant', 'benign')에 대해 반복
    for category in ['malignant', 'benign']:
        category_path = os.path.join(data_dir, category)  # 카테고리 경로 설정
        for img_name in os.listdir(category_path):  # 해당 경로에 있는 모든 이미지에 대해 반복
            img_path = os.path.join(category_path, img_name)  # 이미지 경로 설정
            image = load_and_preprocess_image(img_path, img_size)  # 이미지 로드 및 전처리
            images.append(image)  # 이미지 배열에 추가
            # 'malignant'이면 레이블 0, 'benign'이면 레이블 1을 추가
            labels.append(0 if category == 'malignant' else 1)      
    images = np.array(images)  # 리스트를 numpy 배열로 변환
    labels = np.array(labels)  # 리스트를 numpy 배열로 변환
    
    return images, labels  # 전처리된 이미지와 레이블 반환

# 데이터셋 생성
images, labels = create_dataset('data/', img_size=(64, 64))

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 훈련 세트와 테스트 세트로 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(images.reshape(len(images), -1), labels, test_size=0.2, random_state=42)

# K-최근접 이웃(KNN) 모델 생성 및 훈련
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# 테스트 세트를 사용하여 예측 수행
y_pred = knn.predict(X_test)

# 예측 정확도 계산
accuracy = accuracy_score(y_test, y_pred)

# 정확도 출력
print(f'Accuracy: {accuracy * 100:.2f}%')

# 새로운 이미지를 분류하는 함수
def predict_image_class(image_path, model, img_size=(64, 64)):
    image = load_and_preprocess_image(image_path, img_size)  # 이미지 로드 및 전처리
    image = image.reshape(1, -1)  # 모델에 맞게 이미지 형태 변환
    prediction = model.predict(image)  # 이미지 클래스 예측
    
    # 예측 결과에 따라 클래스 출력
    if prediction[0] == 0:
        return 'Class malignant'
    else:
        return 'Class benign'

# 새로운 이미지 경로 지정
image_path = 'path_to_new_image.jpg'
# 새로운 이미지에 대한 예측 수행
prediction = predict_image_class(image_path, knn)
# 예측 결과 출력
print(f'The image belongs to: {prediction}')

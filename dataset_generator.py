import numpy as np
import matplotlib.pyplot as plt

class dataset_generator:
    def __init__(self, feature_dim =1, n_sample=100, noise=0): 
        # n_sample을 설정해주지않으면, 기본값 100(default)을 가진다.
        self._feature_dim = feature_dim
        self._n_sample = n_sample
        self._noise = noise

        self._coefficient = None
        self._init_set_coefficient() # 이것도 자동으로 초기화해주기위해 불러와주는게 좋겠다.

    # y= x1 + x2 + x3 + bias와 같은 형식으로 만들어준다.
    def _init_set_coefficient(self):
        self._coefficient = [1 for _ in range(self._feature_dim)] + [0]
        print(self._coefficient)
    # 값들을 설정해주기
    def set_coefficient(self, coefficient_list):
        self._coefficient = coefficient_list

    def set_n_sample(self, n_sample):
        self._n_sample = n_sample

    def set_n_noise(self, n_noise):
        self._n_noise = n_noise
    #데이터셋 구성하기
    def make_dataset(self):
        x_data = np.random.normal(0, 1, size = (self._n_sample, 
                                                self._feature_dim))
        
        y_data = np.zeros(shape = (self._n_sample,1))
        # 빈 y_data를 하나 만들어서 계산할 때마다 accumulation!
        for feature_idx in range(self._feature_dim):
            y_data += self._coefficient[feature_idx]*x_data[:,feature_idx].reshape(-1,1)
        y_data += self._coefficient[-1]
        y_data += self._noise*np.random.normal(0,1,size=(self._n_sample,1))
        
        return x_data, y_data
    # 데이터의 분포를 시각화를 통해서 확인
    def dataset_visualizer(self):
      if self._feature_dim ==1:
          fig, ax = plt.subplots(figsize=(10,10))
          
          ax.plot(x_data, y_data, 'bo', alpha=0.3, markersize=20)
          ax.tick_params(axis='both', labelsize=30)
          
          ax.set_title("Dataset", fontsize = 40, color='darkgreen')
          ax.set_xlabel("X data", fontsize = 30, alpha=0.6)
          ax.set_ylabel("Y data", fontsize = 30, alpha=0.6)
      else:
          class feature_dim_error(Exception):
            pass
          raise feature_dim_error("Visualization is valid for only feature_dim ==1")
data_gen = dataset_generator(feature_dim = 1) # feature_dim = ? 이 값을 바꾸게되면 2,3,4 -> dataset_visuallizer의 그래프가 예외처리가 된다.
# 처음 default argument에서 초기화된 100이 아닌 다른 수로 설정 : data_gen.set_n_sample(200)
x_data, y_data = data_gen.make_dataset()
data_gen.dataset_visualizer()

print(x_data.shape, y_data.shape)
# print("\n coefficient 변경된 내용 확인!")
#print(data_gen._coefficient)
#data_gen.set_coefficient([3,4,-2,1])
#print(data_gen._coefficient) 

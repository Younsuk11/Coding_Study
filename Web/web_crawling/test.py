import numpy as np
import matplotlib.pylab as plt
from sympy import diff

## gradient _ 편미분 벡터
def numerical_gradient(f,x) :
    h = 1e-4
    grad = np.zeros_like(x) # x 와 형상(shape)가 고, 모두 0인 배열 형성

    for idx in range(x.size):  #x.size :  원소 개수_ x0, x1모두 한번에 계산
        tmp_val  = x[idx]  #이 후 복원을 위해 따로 변수화
        # f(x+h) 계산
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)

        # f(x-h)계산
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h) #gradient 원소 모두 업데이트

        x[idx] = tmp_val # x 값 복원

    return grad



# 경사 하강법

def gradient_descent(f, init_x, lr = 0.01, step_num = 100): 
    # f: 함수, init_x : 입력값 배열, lr : learning rate, step_num : 시행 횟수
    v = None
    x= init_x
    x_history = [] # 지금까지의 이동경로 저장하기 위함
    gradients_history = []
    for i in range(step_num):
        x_history.append(x.copy()) 
        
        # 현재 값 복사해서 저장하기_ 얕은 복사
        # 굳이 복사할 이유가...??? _ .append(x)와 다른데.... 왜 다르지?
        # "현재 상태"를 저장하는 것 vs "변수"자체를 저장하는것
        # "현재 상태"를 저장하기 위해서... 변수로 선언된것을 복사한 다른 객체를 저장해야한다.(얇은 복제)
        # "변수 자체"저장한다면 "해당변수"가 바뀌게 되면 같이 바뀌게 됨.(단순객체 복제 )

        grad = numerical_gradient(f,x)  #시행마다 옮겨간 위치에서의 gradient 구하기
        gradients_history.append(grad.copy())
        x -= lr*grad  #장소 옮기기
        

    return x , np.array(x_history), np.array(gradients_history)# 최종 도착 장소 출력

    #list인 x_history 를 np.array로 바꿔야 이후 , 열, 행 slicing이 가능



# example

# f(x0, x1) = x0**2 + x1**2
def function2(x):
    return ((x[0]**2)/20) + (x[1]**2) 

init_x = np.array([-7.0, 2.0])
# print(gradient_descent(function2, init_x, lr = 0.1, step_num= 100))
#[-6.11110793e-10  8.14814391e-10] # 이동한 최종 목적 장소.

lr = 0.01
step_num = 1000
x, x_history, gradients_history = gradient_descent(function2, init_x, lr = lr, step_num= step_num)


# print(x_history)

# # 가로 세로 파란줄 그어놓기. plt.plot(x범위, y범위, 그리는 형태)
plt.plot([-10,10],[0,0], '--b')
plt.plot([0,0],[-5,5], '--b')

x = np.arange(-10, 10, 0.1)
y = np.arange(-5, 5, 0.1)


X, Y = np.meshgrid(x,y)
Z = ((X**2)/20) + Y**2
plt.contour(X, Y, Z, levels = np.arange(0,10, 0.5))


plt.plot(x_history[:,0], x_history[:,1], 'o--')
#x_history[:,0] = 이동하면서 찍힌 x0값들
#x_history[:,1] = 이동하면서 찍힌 x1값들
plt.xlim(-10., 10.)
plt.ylim(-5., 5.)
plt.xlabel("X0")
plt.ylabel("X1")
plt.show()







import numpy as np

#シグモイド関数
def sigmoid(x):
    return 1/(1 + np.exp(-x))

#恒等関数
def identify_function(x):
    return x

#network初期化関数
def init_network():
    #ディクショナリ宣言
    network = {}
    #ディクショナリに要素を追加
    #入力(0)層から1層への重み
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    #入力層のバイアス
    network['b1'] = np.array([0.1, 0.2, 0.3])
    #1層から2層への重み
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    #2層のバイアス
    network['b2'] = np.array([0.1, 0.2])
    #2層から出力層への重み
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    #出力層のバイアス
    network['b3'] = np.array([0.1, 0.2])

    return network

def forward(network, x):
    #ディクショナリから要素の取り出し
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    #入力層から1層への信号伝達
    a1 = np.dot(x, W1) + b1
    #1層での活性化
    z1 = sigmoid(a1)

    #1層から2層への信号伝達
    a2 = np.dot(z1, W2) +b2
    #2層での活性化
    z2 = sigmoid(a2)

    #2層から出力層への信号伝達
    a3 = np.dot(z2, W3) + b3
    #出力層での活性化
    y = identify_function(a3)

    return y

network = init_network()
x = np.array([1.0, 0.5])

y = forward(network, x)
print (y)
import sys, os
sys.path.append(os.pardir)
from deep-learning-from-scratch-master.dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(flatten = True, normalize = False)

print(x_train.shape)

#オライリージャパンのリポジトリからソースを取得する必要があるらしい
#各種必要な関数をそろえてくれているとのこと
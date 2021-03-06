import numpy as np

class DecisionTree(object):
    def __init__(self):
        #决策树模型
        self.tree = {}

    def calcInfoGain(self, feature, label, index):
        '''
        计算信息增益
        :param feature:测试用例中字典里的feature，类型为ndarray
        :param label:测试用例中字典里的label，类型为ndarray
        :param index:测试用例中字典里的index，即feature部分特征列的索引。该索引指的是feature中第几个特征，如index:0表示使用第一个特征来计算信息增益。
        :return:信息增益，类型float
        '''

        # 计算熵
        def calcInfoEntropy(label):
            '''
            计算信息熵
            :param label:数据集中的标签，类型为ndarray
            :return:信息熵，类型float
            '''

            label_set = set(label)
            result = 0
            for l in label_set:
                count = 0
                for j in range(len(label)):
                    if label[j] == l:
                        count += 1
                # 计算标签在数据集中出现的概率
                p = count / len(label)
                # 计算熵
                result -= p * np.log2(p)
            return result

        # 计算条件熵
        def calcHDA(feature, label, index, value):
            '''
            计算信息熵
            :param feature:数据集中的特征，类型为ndarray
            :param label:数据集中的标签，类型为ndarray
            :param index:需要使用的特征列索引，类型为int
            :param value:index所表示的特征列中需要考察的特征值，类型为int
            :return:信息熵，类型float
            '''
            count = 0
            # sub_label表示根据特征列和特征值分割出的子数据集中的标签
            sub_label = []
            for i in range(len(feature)):
                if feature[i][index] == value:
                    count += 1
                    sub_label.append(label[i])
            pHA = count / len(feature)
            e = calcInfoEntropy(sub_label)
            return pHA * e

        base_e = calcInfoEntropy(label)
        f = np.array(feature)
        # 得到指定特征列的值的集合
        f_set = set(f[:, index])
        sum_HDA = 0
        # 计算条件熵
        for value in f_set:
            sum_HDA += calcHDA(feature, label, index, value)
        # 计算信息增益
        return base_e - sum_HDA


    def fit(self, feature, label):
        '''
        :param feature: 训练集数据，类型为ndarray
        :param label:训练集标签，类型为ndarray
        :return: None
        '''

        #************* Begin ************#
        self.tree = self.fit_recursive(feature, label)
        #************* End **************#

    def fit_recursive(self, feature, label):
        # 如果 所有标签都相同
        if np.unique(label).shape[0] == 1:
            return np.unique(label)[0]

        # 如果 样本只有一个标签 或 所有的样本特征相同
        if feature.shape[1] == 1 or np.unique(feature, axis=0).shape[0] == 1:
            label_count = np.bincount(label)
            return np.argmax(label_count)

        # 选取信息增益最大的 feature
        dim = feature.shape[1]
        highest_gain = -1
        best_feature_index = 0
        for i in range(dim):
            gain = self.calcInfoGain(feature, label, i)
            if gain > highest_gain:
                highest_gain = gain
                best_feature_index = i
        best_feature = feature[:, best_feature_index]
        best_feature_values = np.unique(best_feature)
        tree = {best_feature_index: {}}
        for value in best_feature_values:
            sub_feature = feature[best_feature == value]
            sub_label = label[best_feature == value]
            tree[best_feature_index][value] = self.fit_recursive(sub_feature, sub_label)
        return tree

    def predict(self, feature):
        '''
        :param feature:测试集数据，类型为ndarray
        :return:预测结果，如np.array([0, 1, 2, 2, 1, 0])
        '''

        #************* Begin ************#
        N = feature.shape[0]
        result = np.zeros(N)
        for i in range(N):
            feature_i = feature[i]
            result[i] = self.predict_recursive(self.tree, feature_i)
        return result
        #************* End **************#

    def predict_recursive(self, tree, feature_i):
        if not isinstance(tree, dict):
            return tree
        cur_f = list(tree.keys())[0]
        cur_v = feature_i[cur_f]
        return self.predict_recursive(tree[cur_f][cur_v], feature_i)

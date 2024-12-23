这张图展示了一些特征工程的公式，主要用于金融市场中的订单簿数据分析。以下是对这些特征的逐步解释：

---

### **左侧部分：基础特征**
1. **买卖报价 (bid 和 ask)**  
   - $ bid_i = n.bid_i + 1 $：表示第 $i$ 档买价，通常从订单簿中提取。
   - $ ask_i = n.ask_i + 1 $：表示第 $i$ 档卖价。

2. **买卖量 (bsize 和 asize)**  
   - $ bsize_i = \log(n.bsize_i) $：第 $i$ 档买量的对数变换。
   - $ asize_i = \log(n.asize_i) $：第 $i$ 档卖量的对数变换。

3. **价差 (spread)**  
   - $ spread_i = ask_i - bid_i $：第 $i$ 档的买卖价差。

4. **中间价格 (mid\_price)**  
   - $ mid\_price_i = \frac{ask_i + bid_i}{2} $：第 $i$ 档的中间价格，反映买卖价格的平均值。

5. **加权平均价格 (weighted\_ab)**  
   - $ weighted\_ab_i = \frac{ask_i \cdot n.asize_i + bid_i \cdot n.bsize_i}{n.asize_i + n.bsize_i} $：根据买卖量对价格加权，得到的加权平均价格。

6. **相对价差 (relative\_spread)**  
   - $ relative\_spread_i = \frac{spread_i}{mid\_price_i} $：价差相对于中间价格的比例，衡量市场流动性。

7. **移动平均价格 (ask1\_ma 和 bid1\_ma)**  
   - $ ask1\_ma_n = mean(ask_1 \text{ over n periods}) $：第1档卖价的 $n$ 周期移动平均。
   - $ bid1\_ma_n = mean(bid_1 \text{ over n periods}) $：第1档买价的 $n$ 周期移动平均。

8. **中间价格变化范围 (mid\_price\_range)**  
   - $ mid\_price\_range_n = mid\_price_t - mid\_price_{t-shift(n)} $：中间价格在 $n$ 个时间单位内的变化范围。

---

### **右侧部分：高级特征**
1. **总买卖量 (all\_size)**  
   - $ all\_size = \sum_{i=1}^5 (n.bsize_i + n.asize_i) $：前5档买卖量的总和。

2. **买卖量比例 (bsize\_asize\_1 和 bsize\_asize\_3)**  
   - $ bsize\_asize\_1 = \frac{n.bsize_1}{n.bsize_1 + n.asize_1} $：第1档买量占买卖总量的比例。
   - $ bsize\_asize\_3 = \frac{all\_size - (n.bsize_2 + n.bsize_4 + n.asize_2 + n.asize_4)}{all\_size} $：去掉第2和第4档后的买量占比。

3. **买卖量比率 (bsize\_over\_asize)**  
   - $ bsize\_over\_asize = \frac{\sum_{i=1}^5 n.bsize_i}{\sum_{i=1}^5 n.asize_i} $：前5档买量与卖量的比率。

4. **单位交易量 (amount\_size)**  
   - $ amount\_size = amount \cdot bsize\_over\_asize $：交易量与买卖量比率的乘积。

5. **买卖量相对差异 (vol\_rel\_diff 和 vol\_all\_rel\_diff)**  
   - $ vol\_rel\_diff = \frac{n.bsize_1 - n.asize_1}{n.bsize_1 + n.asize_1} $：第1档买卖量的相对差异。
   - $ vol\_all\_rel\_diff = \frac{\sum_{i=1}^5 n.bsize_i - \sum_{i=1}^5 n.asize_i}{\sum_{i=1}^5 (n.bsize_i + n.asize_i)} $：前5档买卖量的相对差异。

---

### **总结**
这些特征主要用于描述订单簿的价格、交易量和流动性特征。  
- **基础特征**（左侧）直接反映了市场的价格和交易量信息。  
- **高级特征**（右侧）通过聚合和比率计算，进一步揭示了市场的深度、买卖力量对比以及流动性状况。  

这些特征通常用于构建机器学习模型，以预测价格走势、市场波动或交易行为。

```bash
# label 5
类别权重： {1.0: 1.4332101193218663, 0.0: 6.5921224804493885, 2.0: 6.641456085294888}

Classification Report:
              precision    recall  f1-score   support

         0.0       0.35      0.63      0.45      4563
         1.0       0.91      0.59      0.72     20828
         2.0       0.37      0.66      0.48      4583

    accuracy                           0.61     29974
   macro avg       0.54      0.63      0.55     29974
weighted avg       0.74      0.61      0.64     29974

# label 5
类别权重： {1.0: 1.4322527740692756, 0.0: 6.6019396776679455, 2.0: 6.652094717668488}

Classification Report:
              precision    recall  f1-score   support

         0.0       0.36      0.65      0.46      4535
         1.0       0.91      0.59      0.72     20691
         2.0       0.37      0.65      0.47      4544

    accuracy                           0.61     29770
   macro avg       0.54      0.63      0.55     29770
weighted avg       0.74      0.61      0.64     29770

# label 10
Classification Report:
              precision    recall  f1-score   support

         0.0       0.45      0.56      0.50      6421
         1.0       0.77      0.65      0.71     17063
         2.0       0.46      0.55      0.50      6286

    accuracy                           0.61     29770
   macro avg       0.56      0.59      0.57     29770
weighted avg       0.64      0.61      0.62     29770

# label 20
Classification Report:
              precision    recall  f1-score   support

         0.0       0.36      0.65      0.46      4535
         1.0       0.91      0.59      0.72     20691
         2.0       0.37      0.65      0.47      4544

    accuracy                           0.61     29770
   macro avg       0.54      0.63      0.55     29770
weighted avg       0.74      0.61      0.64     29770

# label 40
Classification Report:
              precision    recall  f1-score   support

         0.0       0.36      0.65      0.46      4535
         1.0       0.91      0.59      0.72     20691
         2.0       0.37      0.65      0.47      4544

    accuracy                           0.61     29770
   macro avg       0.54      0.63      0.55     29770
weighted avg       0.74      0.61      0.64     29770

# label 60
Classification Report:
              precision    recall  f1-score   support

         0.0       0.36      0.65      0.46      4535
         1.0       0.91      0.59      0.72     20691
         2.0       0.37      0.65      0.47      4544

    accuracy                           0.61     29770
   macro avg       0.54      0.63      0.55     29770
weighted avg       0.74      0.61      0.64     29770
```

```python
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
model = SVC()
model.fit(train_data, train_label)

print("预测正确的标签数：", sum(y_hat == y))  
print("总体正确率：", sum(y_hat == y) / len(y_hat))  

# 分标签查看  
print("真实标签为0样本的正确预测个数：", sum(y[y == 0] == y_hat[y == 0]))  
print("真实标签为1样本的正确预测个数：", sum(y[y == 1] == y_hat[y == 1]))  
print("真实标签为2样本的正确预测个数：", sum(y[y == 2] == y_hat[y == 2]))  

# 我们更关心上涨下跌情况的预测  
# 所有不为0的标签的召回率（即仅考虑真实标签为上涨或下跌样本是否被正确分类）  
index = y != 1  
print("上涨下跌召回率：", sum(y_hat[index] == y[index]) / sum(index))  

# 所有不为1的标签的准确率（即仅考虑预测为上涨或下跌样本是否正确）  
index = y_hat != 1  
print("上涨下跌准确率：", sum(y_hat[index] == y[index]) / sum(index))
```
```bash
预测正确的标签数： 17168
总体正确率： 0.8584
真实标签为0样本的正确预测个数： 0
真实标签为1样本的正确预测个数： 17168
真实标签为2样本的正确预测个数： 0
上涨下跌召回率： 0.0
上涨下跌准确率： nan
```
```bash
总体正确率： 0.66425
上涨下跌召回率： 0.3086158192090395
上涨下跌准确率： 0.14153846153846153
```


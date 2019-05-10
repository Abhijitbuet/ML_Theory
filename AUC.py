import numpy as np
from sklearn import metrics
y = np.array([0, 0, 1, 0, 1, 0,0, 1, 1, 0, 1, 1, 1, 1, 0,1,1,1])
pred = np.array([ .03, 0.08, .1, .11, .22, .32, .35, 0.42, 0.44, 0.48, 0.56, .65, .71, .72, .73, .8, .82, .99])
fpr, tpr, thresholds = metrics.roc_curve(y, pred, pos_label=1)
print(metrics.auc(fpr, tpr))
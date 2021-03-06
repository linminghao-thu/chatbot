
#导入库
from model.model import *
from model.pre_process import *
import torch
#读入数据
dataClass = Corpus('data/qingyun.tsv', maxSentenceWordsNum=25)
#指定模型和一些超参
model = Seq2Seq(dataClass, featureSize=256, hiddenSize=256,
                attnType='L', attnMethod='concat',
                encoderNumLayers=5, decoderNumLayers=3,
                encoderBidirectional=True,
                device=torch.device('cpu:0'))
#训练
model.train(batchSize=1024, epoch=1000)
#保存模型
model.save('modelC.pkl')
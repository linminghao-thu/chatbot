
#导入库
from model import *
from model.model import ChatBot
from model.pre_process import *
import torch, warnings
warnings.filterwarnings("ignore")

#载入模型
chatbot = ChatBot('mm/model.pkl')

#针对问题1
chatbot.predictByGreedySearch("你好啊")

#针对问题2
chatbot.predictByBeamSearch("什么是人工智能", isRandomChoose=True, beamWidth=10)

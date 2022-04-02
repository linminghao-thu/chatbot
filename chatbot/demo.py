'''
#导入库
from model.model import *
import torch,warnings,argparse
warnings.filterwarnings("ignore")

#选择哪个模型 ，是否使用gpu
parser = argparse.ArgumentParser()
parser.add_argument('--model', help='The path of your model file.', default='mm/modelA.pkl', type=str)
parser.add_argument('--device', help='Your program running environment, "cpu" or "cuda"', type=str, default='cpu')
args = parser.parse_args()
print(args)
#主程序，打印log，同时对话
if __name__ == "__main__":
    print('Loading the model...')
    chatBot = ChatBot(args.model, device=torch.device(args.device))
    print('Finished...')

    allRandomChoose,showInfo = False, False
    #在控制端显示的词语
    while True:
        inputSeq = input("提问者: ")
        if inputSeq=='_crazy_on_':
            allRandomChoose = True
            print('BOT1: ','成功开启疯狂模式...')
        elif inputSeq=='_crazy_off_':
            allRandomChoose = False
            print('BOT1: ','成功关闭疯狂模式...')
        elif inputSeq=='_showInfo_on_':
            showInfo = True
            print('BOT1: ','成功开启日志打印...')
        elif inputSeq=='_showInfo_off_':
            showInfo = False
            print('BOT1: ','成功关闭日志打印...')
        else:
            outputSeq = chatBot.predictByBeamSearch(inputSeq, isRandomChoose=True, allRandomChoose=allRandomChoose, showInfo=showInfo)
            print('BOT1: ',outputSeq)
        print()
'''

#导入库
from flask import Flask, request, jsonify
from model.model import *
import torch,warnings,argparse
warnings.filterwarnings("ignore")

#选择哪个模型 ，是否使用gpu
parser = argparse.ArgumentParser()
parser.add_argument('--model', help='The path of your model file.', default='mm/modelB.pkl', type=str)
parser.add_argument('--device', help='Your program running environment, "cpu" or "cuda"', type=str, default='cpu')
args = parser.parse_args()
print(args)

app = Flask(__name__)
chatBot = ChatBot(args.model, device=torch.device(args.device))

@app.route('/getText', methods=['GET'])
def getText():
    inputSeq = request.args.get('text')
    outputSeq = chatBot.predictByBeamSearch(inputSeq, isRandomChoose=True, allRandomChoose=False, showInfo=False)
    return outputSeq

#主程序，打印log，同时对话
if __name__ == "__main__":
	app.run(host='127.0.0.1', port=5000, debug=False)
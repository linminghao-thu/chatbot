from flask import Flask, request, jsonify
from model.model import *
import torch,warnings,argparse
warnings.filterwarnings("ignore")

#选择哪个模型 ，是否使用gpu
parser = argparse.ArgumentParser()
parser.add_argument('--model', help='The path of your model file.', default='mm/modelA.pkl', type=str)
parser.add_argument('--device', help='Your program running environment, "cpu" or "cuda"', type=str, default='cpu')
args = parser.parse_args()
print(args)



app = Flask(__name__)

@app.route('/getText', methods=['POST'])
def getText():
	return "123"

#主程序，打印log，同时对话
if __name__ == "__main__":
	print('Loading the model...')
	chatBot = ChatBot('mm/model.pkl')
	print('Finished...')
	app.run()

from flask import Flask,render_template,url_for,request
import torch
from torchvision import datasets , transforms
import pickle
from network import Network
app = Flask(__name__)
from PIL import Image

  
model = pickle.load(open('modelv2.pkl','rb'))

@app.route('/')
def home():
    css = url_for('static',filename = 'front.css')
    js = url_for('static',filename = 'draw.js')
    saver = url_for('static',filename = 'FileSaver.js')
    return render_template('front.html',css_path = css, drawpath = js , saver = saver)

@app.route('/predict',methods = ['post'])
def predict():
    image = request.files["image"]

    image.save("to_predict/image.png")

    input = Image.open("to_predict/image.png").convert("L")
    transform = transforms.ToTensor()
    input = transform(input)
    print(input.shape)
    input = input.reshape(-1,28*28)

    output = model(input)

    result = torch.argmax(output,dim = 1).item()
    print(output)
    print(result)
    return render_template('front.html',prediction = result)


if __name__ == '__main__':
    app.run()

    
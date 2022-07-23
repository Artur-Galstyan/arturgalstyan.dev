import matplotlib.pyplot as plt
import cv2
import numpy as np
import pickle
import json
import pathlib
from flask import Blueprint, request
import random
from .nn_module import NeuralNetwork
from sklearn.preprocessing import MinMaxScaler

api = Blueprint("api", __name__)
path = pathlib.Path(__file__).resolve().parent / "assets/nn_pickle"
nn_params = pickle.load(open(path, "rb"))
nn = NeuralNetwork(nn_params["architecture"])
nn.parameters = nn_params["parameters"]


wait_sentences = []
parent = pathlib.Path(__file__).resolve().parent / "assets/wait_sentences"
with open(parent) as file:
    while line := file.readline().rstrip():
        wait_sentences.append(line)


@api.route("/get_thinking_sentence", methods=["POST"])
def get_thinking_sentence():
    return {"wait_sentence": random.choice(wait_sentences)}


@api.route("/get_nn_prediction", methods=["POST"])
def get_neural_network_prediction():
    data = json.loads(request.get_data(as_text=True))["imgData"][0]
    img_data = [data[f"{i}"] for i in range(len(data))]

    n_pixels = int(len(img_data) / 4)
    n_pixels_per_side = int(np.sqrt(n_pixels))

    data = np.float32(
        np.array(img_data).reshape(n_pixels_per_side, n_pixels_per_side, 4)
    )
    min_max_scaler = MinMaxScaler()
    gray = np.array(cv2.cvtColor(data, cv2.COLOR_RGBA2GRAY))
    img = cv2.resize(gray, (28, 28), interpolation=cv2.INTER_AREA)
    img = min_max_scaler.fit_transform(img)

    img = img.reshape(1, 784)
    a, _ = nn.forward(img)

    return json.dumps({"pred": int(np.argmax(a))})

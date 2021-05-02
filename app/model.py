from keras.models import model_from_json
import numpy as np
import tensorflow as tf


EMOTIONS_LIST = ["Angry", "Disgust",
                     "Fear", "Happy",
                     "Sad", "Surprise",
                     "Neutral"]

with open('app/models/model_graphs/face_model.json', "r") as json_file:
    loaded_model_json = json_file.read()
    loaded_model = model_from_json(loaded_model_json)
    print('----------',loaded_model)

loaded_model.load_weights('app/models/face_model1.h5')
graph = tf.get_default_graph()
print("Model loaded from disk")
loaded_model.summary()


def predict_emotion(img):
    global graph
    with graph.as_default():
        preds = loaded_model.predict(img)
    res = np.argmax(preds)

    return EMOTIONS_LIST[res],res

#
# if __name__ == '__main__':
#     pass

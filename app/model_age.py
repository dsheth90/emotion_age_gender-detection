from keras.models import model_from_json
import numpy as np
import tensorflow as tf

AGE_LIST = ["adult", "child",
                     "old", "youth"]

with open('app/models/imdb_models/model_age_IMDB_gpu.json', "r") as json_file:
    loaded_model_json1 = json_file.read()
    loaded_model1 = model_from_json(loaded_model_json1)

# load weights into the new model
loaded_model1.load_weights('app/models/imdb_models/model_age_IMDB_gpu.h5')
graph = tf.get_default_graph()
print("Model loaded from disk")
loaded_model1.summary()


def predict_age(img):
    global graph
    with graph.as_default():
        preds = loaded_model1.predict(img)
    res = np.argmax(preds)

    return AGE_LIST[res],res


# if __name__ == '__main__':
#     pass

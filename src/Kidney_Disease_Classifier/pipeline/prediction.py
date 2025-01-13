import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.losses import CategoricalCrossentropy

# Custom class to handle the 'fn' issue
class CustomCategoricalCrossentropy(CategoricalCrossentropy):
    def __init__(self, *args, **kwargs):
        kwargs.pop("fn", None)  # Remove 'fn' if it exists
        super().__init__(*args, **kwargs)

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load model with a fix for the 'fn' issue
        model = load_model(
            os.path.join("model", "model.h5"),
            custom_objects={"CategoricalCrossentropy": CustomCategoricalCrossentropy},
        )

        # Preprocess the input image
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # Predict and process the result
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = "Tumor"
        else:
            prediction = "Normal"

        return [{"image": prediction}]

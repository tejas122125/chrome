# from transformers import AutoTokenizer, TFBertForSequenceClassification
# import tensorflow as tf

# tokenizer = AutoTokenizer.from_pretrained("ydshieh/bert-base-uncased-yelp-polarity")
# model = TFBertForSequenceClassification.from_pretrained("ydshieh/bert-base-uncased-yelp-polarity")

# inputs = tokenizer("i will kill you", return_tensors="tf")

# logits = model(**inputs).logits

# predicted_class_id = int(tf.math.argmax(logits, axis=-1)[0])
# print(predicted_class_id)
# model.config.id2label[predicted_class_id]
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="IMSyPP/hate_speech_en")
res = pipe("i will kill you")
print(res)
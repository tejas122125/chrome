from PIL import Image
import requests
from transformers import AutoProcessor, BlipForQuestionAnswering

# model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")
processor = AutoProcessor.from_pretrained("Salesforce/blip-vqa-base")

url = "https://imgs.search.brave.com/mhkPmLdV7xh36KCFk26kO7LUBYBYIQ4RU1RGHBUWdIk/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93d3cu/Ym9yZWRwYW5kYS5j/b20vYmxvZy93cC1j/b250ZW50L3VwbG9h/ZHMvMjAyMi8wNi9j/b25mdXNpbmctaW1h/Z2VzLXJlcXVpcmUt/bW9yZS1jb250ZXh0/LTItNjJiYTlkY2Jk/NDlhNF9fNzAwLmpw/Zw"
image = Image.open(requests.get(url, stream=True).raw)


# inference
text = "what is the swan doing in the picture"
inputs = processor(images=image, text=text, return_tensors="pt")
outputs = model.generate(**inputs)
res = processor.decode(outputs[0], skip_special_tokens=True)
print(res)

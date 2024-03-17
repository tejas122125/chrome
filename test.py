from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from flask import Flask, jsonify,request
import json
from dotenv import load_dotenv
import requests
import os

load_dotenv()



app = Flask("tejs")
data = ""        
parsed_text=""        

   
@app.route("/getdata",methods=['POST'])
def getdata():
    apikey = os.getenv('OPENAI_API_KEY')
    image_url = request.json['url']
    
    payload = {"url":image_url,'isOverlayRequired': False,'apikey':apikey,'language': 'eng'}

    r = requests.post('https://api.ocr.space/parse/image',
                          data=payload,
                          )
    data = r.content.decode()
    print(data)
    parsed_data = json.loads(data)
    parsed_text = parsed_data['ParsedResults'][0]['ParsedText']
    print(parsed_text)
    print(parsed_data)
    openai = ChatOpenAI(
    openai_api_key="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"
    )
    prompt_template = PromptTemplate.from_template(
    "you are skillfull bot which could convert plain text into code. Here is some text: {query}.convert this text into properly indentended code  and with same variable name as in text by automatically detecting the language . Also donot add any further text in it. Also if proper code cannot be produced return the raw data recieved  "  # Prompt structure
    )
    chain = prompt_template | openai
    text_to_save = chain.invoke({ "query":parsed_text}).content



    filename = "code.txt"  # Replace with your desired filename
    with open(filename, "w") as file:      
        file.write(text_to_save)
    return f"{text_to_save}" 



   
    
if __name__ == "__main__":
  app.run(port=8080,debug=True)
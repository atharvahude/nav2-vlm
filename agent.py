import json
import ast
import base64

from openai import OpenAI
from prompt import meta_prompt


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def ai_planner():

    client = OpenAI()
    # Path to your image
    image_path = "./input.png"
    # Getting the Base64 string
    base64_image = encode_image(image_path)
    
    # Asking for user input
    question = input("Where do you want to go ? : ")

    # Find a path to the Dining Room.
    
    # response = client.client.beta.assistants.create
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": meta_prompt+question,
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{base64_image}"},
                    }
                ],
            },
        ],
       temperature=0
    )

    # response_str = response.choices[0].message.content
    
    lst = response.choices[0].message.content.split("\n")[1:-1]
    mystr = ''
    for i in lst:
        mystr = mystr+i
    
    # print(mystr)
    
    # response_dict = ast.literal_eval(mystr)
    # response_content = response.choices[0].message.content
    
    # print(response_ceontent)
    response_dict=json.loads(mystr)

    return response_dict

if __name__ == "__main__":
    print(ai_planner())
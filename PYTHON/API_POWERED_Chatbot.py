import os
import gradio
from bardapi import Bard

os.environ['_BARD_API_KEY'] = 'YOUR-BARD-API-KEY'

messages = [{"role": "system", "content": "You are an expert and knows everything"}]
# content may vary, if you give you are an expert in medical feild it will perfectly give answer for medical related question you ask.

def CustomChatBard(user_input):
    messages.append({"role": "user", "content": user_input})
    response = Bard().get_answer(user_input)
    ChatBard_reply = response['content']
    messages.append({"role": "assistant", "content": ChatBard_reply})
    return ChatBard_reply

demo = gradio.Interface(fn=CustomChatBard, inputs="text", outputs="text", title="jenishgpt")

demo.launch(share=True)

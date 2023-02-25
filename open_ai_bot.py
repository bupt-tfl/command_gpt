# encoding:utf-8
import openai


# OpenAI对话模型API (可用)
class OpenAIBot:
    def __init__(self):
        openai.api_key = "your api_key"

    def reply(self, query):
        return self.reply_text(query)

    def reply_text(self, query):
        try:
            response = openai.Completion.create(
                model="text-davinci-003",  # 对话模型的名称
                prompt=query,
                temperature=0.2,  # 值在[0,1]之间，越大表示回复越具有不确定性
                max_tokens=1200,  # 回复最大的字符数
                top_p=1,
                frequency_penalty=2.0,  # [-2,2]之间，该值越大则更倾向于产生不同的内容
                presence_penalty=2,  # [-2,2]之间，该值越大则更倾向于产生不同的内容
                stop=["#"]
            )
            res_content = response.choices[0]["text"].strip()
        except Exception as e:
            return str(e)
        return res_content

    def create_img(self, query):
        try:
            response = openai.Image.create(
                prompt=query,  # 图片描述
                n=1,  # 每次生成图片的数量
                size="256x256"  # 图片大小,可选有 256x256, 512x512, 1024x1024
            )
            image_url = response['data'][0]['url']
        except Exception as e:
            return None
        return image_url

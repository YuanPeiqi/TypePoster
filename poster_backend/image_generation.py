import os
import openai
openai.api_key = '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'
openai.Model.list()

images = openai.Image.create(
    prompt='有科技感的数据库系统',
    n=2,
    size='1024x1024'
)

print(images)

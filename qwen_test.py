from llms import QwenWrapper

qwen = QwenWrapper()

prompt = "Give me a short introduction to large language model."
response = qwen.query(prompt)

print("prompt:", prompt)
print("response:", response)

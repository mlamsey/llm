from llms import QwenWrapper

# qwen = QwenWrapper(system_prompt="You are a helpful robotic exercise coach. You work with older adults, and you want people to be healthy.")
qwen = QwenWrapper()
while True:
    ui = input("Input (q to quit): ")
    if ui.lower() == 'q':
        break

    response = qwen.query(ui)
    print("\n", response, "\n")

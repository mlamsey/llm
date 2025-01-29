from llms import QwenWrapper, QwenVersion
from termcolor import colored

def main(args):
    if args.model == "chat":
        model = QwenVersion.Chat05B
    elif args.model == "main":
        model = QwenVersion.Main7B
    else:
        raise ValueError(f"Invalid model: {args.model}")

    # qwen = QwenWrapper(system_prompt="You are a helpful robotic exercise coach. You work with older adults, and you want people to be healthy.")
    qwen = QwenWrapper(model=model)
    while True:
        ui = input("Input (q to quit): ")
        if ui.lower() == 'q':
            break

        response = qwen.query(ui)
        print("\n", colored(response, "green"), "\n")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="chat", help="Model to run: chat or main")

    args = parser.parse_args()

    main(args)

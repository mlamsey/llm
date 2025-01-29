from transformers import AutoModelForCausalLM, AutoTokenizer

class QwenVersion:
    Chat05B = "Qwen/Qwen1.5-0.5B-Chat"
    Main7B = "Qwen/Qwen2.5-7B"

class QwenWrapper:
    def __init__(self,
                 model: QwenVersion = QwenVersion.Chat05B,
                 device: str = "cuda",
                 system_prompt: str = "You are a helpful assistant."):
        print(f"Initializing model {model}... ", end="")

        self.device = device
        self.system_prompt = system_prompt

        self.model = AutoModelForCausalLM.from_pretrained(
            model,
            torch_dtype="auto",
            device_map="auto"
        )
        self.tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen1.5-0.5B-Chat")

        print("Done!")

    def query(self, prompt: str):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.device)

        generated_ids = self.model.generate(
            model_inputs.input_ids,
            max_new_tokens=512
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return response
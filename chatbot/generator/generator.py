<<<<<<< HEAD
from typing import Iterator
from retrieval import Retrieval 

class Generator:
    def __init__(self , retrieval : Retrieval) -> None:
        
        self.retrieval = retrieval



    def generate(self, prompt: str) -> Iterator[str]:
    
        

        if "information:" in prompt.lower():

            info_line = prompt.split("\n\n")[0]
            text = info_line.replace("system Use this information","")

        else: 

            text = "again."



        from time import sleep
        for chunk in text.split():
            sleep(0.1)
            yield chunk
            yield ' '
=======
from llama_cpp import Llama
from typing import Iterator

class Generator:
    def __init__(self) -> None:
        # ###
        # 주석을 지우고 __init__ 을 자유롭게 활용하자.
        # ###
        self.llm = Llama.from_pretrained(
            repo_id="bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF",
            filename="DeepSeek-R1-Distill-Qwen-1.5B-IQ2_M.gguf",
        )
        print(self.llm.chat_format)


    def generate(self, prompt: str) -> Iterator[str]:
        # ###
        # 주석을 지우고 다음 기능을 완성하자.
        # generate 는 단순 prompt 뒤에 이어질 "자연스러운" 말을 리턴하면 된다.
        # 단, 토큰을 하나하나 출력하기 위해서는 Iterator 로 리턴해야한다. 
        # yield 개념을 모른다면 공부해보자!
        # 
        # 예시 1:
        # prompt: I want
        # @return: " to be a doctor"
        # 
        # 예시 2:
        # prompt: Pizza is 
        # @return: " so delicious"
        # ###
        stream = self.llm(prompt, max_tokens=None, stream=True)

        for chunk in stream:
            yield chunk['choices'][0]['text']
>>>>>>> c65e4b3681e38815e1f71075239ae96afb600bb1


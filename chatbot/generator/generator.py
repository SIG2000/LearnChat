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


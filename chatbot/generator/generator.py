import re
from typing import Iterator

class Generator:
    def __init__(self) -> None:
        pass

    def generate(self, prompt: str) -> Iterator[str]:
        match = re.search(r"<\｜User\｜>(.*?)<\｜Assistant\｜>", prompt)
        query = match.group(1).strip() if match else prompt.strip()

        system_info_match = re.search(r"<system> Use this information: (.*?)\n\n", prompt, re.DOTALL)
        info = system_info_match.group(1).strip() if system_info_match else "This is a sample answer. Replace this with your answer"
        
        text = info

        from time import sleep
        for chunk in text.split():
            sleep(0.1)
            yield chunk
            yield ' '
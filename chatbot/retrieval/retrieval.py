import json


class Retrieval:
    def __init__(self, data_path: str = "./data/Team5.json"):
        with open(data_path, "r") as file:
            data: dict[str, str] = json.load(file)
            self.data = data

    def retrieve(self, query: str) -> str | None:

        return None

        try:
            # print(self.data[query])
            return f"{query}: {self.data[query]}"
        except KeyError as err:
            pass

        for key, val in self.data.items():
            if key in query:
                query = key
                break

        try:
            print(self.data[query])
            return f"{query}: {self.data[query]}"
        except KeyError:
            return None

    def print_data(self) -> None:
        print(self.data)

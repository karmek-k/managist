WRAP_THRESHOLD = 59


class StringWrapper:
    def __init__(self, threshold: int=WRAP_THRESHOLD) -> None:
        if threshold <= 0:
            raise ValueError('Wrapper threshold must be a positive integer')

        self.threshold = threshold

    def wrap(self, string: str) -> str:
        result = []
        
        for i, char in enumerate(string):
            if i % self.threshold == 0 and i > 0:
                result.append('\n')

            result.append(char)
        
        return ''.join(result)

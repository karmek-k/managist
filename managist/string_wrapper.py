WRAP_THRESHOLD = 59


class StringWrapper:
    """
    A service class for wrapping lines when
    a certain number of characters (threshold) is met in a single line.
    """
    def __init__(self, threshold: int=WRAP_THRESHOLD) -> None:
        """
        Creates a `StringWrapper` with given `threshold`.
        `threshold` must be a positive integer.
        """
        if threshold <= 0:
            raise ValueError('Wrapper threshold must be a positive integer')

        self.threshold = threshold

    def wrap(self, string: str) -> str:
        """
        Inserts newlines in a way that
        each line of `string` is at most `self.threshold` characters long.
        """
        result = []
        
        for i, char in enumerate(string):
            if i % self.threshold == 0 and i > 0:
                result.append('\n')

            result.append(char)
        
        return ''.join(result)

from typing import Optional

from managist.string_wrapper import StringWrapper


class Gist:
    def __init__(self,
                 title: str,
                 content: Optional[str],
                 wrapper: Optional[StringWrapper]) -> None:
        self.title = title

        if wrapper:
            self.content = wrapper.wrap(content)
        else:
            self.content = content
    

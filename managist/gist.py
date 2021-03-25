from typing import Optional

from github.MainClass import Github

from managist.string_wrapper import StringWrapper


class Gist:
    def __init__(self,
                 github: Github,
                 title: str,
                 content: Optional[str]=None,
                 wrapper: Optional[StringWrapper]=None) -> None:
        self.github = github
        self.title = title

        if wrapper:
            self.content = wrapper.wrap(content)
        else:
            self.content = content
    

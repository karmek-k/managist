from typing import Optional

from github.MainClass import Github
from github.InputFileContent import InputFileContent

from managist.string_wrapper import StringWrapper


class Gist:
    def __init__(self,
                 github: Github,
                 title: str,
                 content: str,
                 wrapper: Optional[StringWrapper]=None) -> None:
        """
        Creates a new Gist. This constructor 
        is supposed to be used by the `Managist.create_gist` method.
        """
        self.github = github
        self.title = title
        self.github_gist = None

        if wrapper:
            self.content = wrapper.wrap(content)
        else:
            self.content = content

    def save(self, public: bool=False) -> None:
        """
        Saves gist's content. If the gist is not present on GH's servers,
        then creates one.
        """
        file_dict = {'gist': InputFileContent(self.content, self.title)}
        user = self.github.get_user()

        if not self.github_gist:
            self.github_gist = user.create_gist(public, files=file_dict)
        else:
            self.github_gist.edit(files=file_dict)


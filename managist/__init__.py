from github import Github

from managist.gist import Gist
from managist.string_wrapper import StringWrapper, WRAP_THRESHOLD


class Managist:
    def __init__(self, access_token: str) -> None:
        self.github = Github(access_token)

        # test if the token is correct
        self.github.get_user().get_repos().totalCount
    
    def create_gist(self,
                    title: str,
                    content: str,
                    wrap: bool=False,
                    wrap_threshold: int=WRAP_THRESHOLD) -> Gist:
        wrapper = StringWrapper(wrap_threshold) if wrap else None

        return Gist(self.github, title, content, wrapper)

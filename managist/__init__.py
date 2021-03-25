from github import Github
from github.Gist import Gist as GithubGist

from managist.gist import Gist


class Managist:
    def __init__(self, access_token: str) -> None:
        self.github = Github(access_token)
        self.user = self.github.get_user()

        # test if the token is correct
        self.user.get_repos().totalCount


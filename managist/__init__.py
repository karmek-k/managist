from github import Github

from managist.gist import Gist
from managist.string_wrapper import StringWrapper, WRAP_THRESHOLD


class Managist:
    """
    The main class of the `managist` library.
    
    You can get an access token at https://github.com/settings/tokens
    (make sure that you enable the `gist` scope for it!)
    """

    def __init__(self, access_token: str) -> None:
        """
        Creates and tests a GitHub API connection.
        You can get an access token at https://github.com/settings/tokens

        Make sure that `access_token` has `gist` scope!
        """
        self.github = Github(access_token)

        # test if the token is correct
        self.github.get_user().get_repos().totalCount
    
    def create_gist(self,
                    title: str,
                    content: str,
                    wrap: bool=False,
                    wrap_threshold: int=WRAP_THRESHOLD) -> Gist:
        """Factory method that creates a gist object with self.github instance."""

        wrapper = StringWrapper(wrap_threshold) if wrap else None

        return Gist(self.github, title, content, wrapper)

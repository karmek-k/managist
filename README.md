# managist

Python library for interacting with GitHub Gists

## Example

```python
from managist import Managist


mg = Managist('your_access_token')

new_gist = mg.create_gist('Test gist title', 'Managist works!')
new_gist.save()
```

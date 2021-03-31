# managist

[![Build Status](https://travis-ci.com/karmek-k/managist.svg?branch=master)](https://travis-ci.com/karmek-k/managist)

Python library for interacting with GitHub Gists

## Example

### Creating an example gist

```python
from managist import Managist


mg = Managist('your_access_token')

new_gist = mg.create_gist('Test gist title', 'Managist works!')
new_gist.save(public=True)
```

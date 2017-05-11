# PY-GG
A Python module wrapper for the Champion.GG API

# Installation
  ```
  pip install py_gg
  ```

# Usage
First, instantiate the wrapper with your api key
  ```
  import py_gg
  py_gg.init(YOUR_API_KEY)
  ```

Then you gain access to all current endpoints of the API! Some endpoints require either `role` or `champion_id`, along with an optional object with ...options. These params are passed as query string params and are `page`, `limit`, `elo`, `sort`, and `champData`. For more details on these parameters, please refer to the Champion.GG API documentation.

The methods are:

Method | Parameters |
------ | ---------- |
`.init`| `api_key`  |
`.statistics.overall` | `options` |
`.statistics.general` | `options` |
`.champions.all` | `options` |
`.champions.specific`| `champId`, `options` |
`.champions.specific_role`| `champId`, `role`, `options` |
`.champions.specific_matchup`| `champ1Id`, `champ2Id`, `role`, `options` |


## contributing
Feel free to contribute, let's just try to keep it readable :)

## Release History
  * 1.0.0 Initial release
  * 1.0.1 Fixes to calls to Champions and Stats
  * 2.0.0 Release for v2 of the API
  * 2.0.1 Fixes to pypi
  * 2.0.2 QOL Changes, privitizing methods

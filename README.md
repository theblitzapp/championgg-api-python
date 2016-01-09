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

Then you gain access to all current endpoints of the API! All but initialization require a callback function and some also require either `role` or `champion_name`, along with an optional object with ...params. These params are passed as query string params and are `page` and `limit`. The param `order` refers to either best or worst.

The methods are:

Method | Parameters |
------ | ---------- |
`.init`| `api_key`  |
`.stats.all` | `none` |
`.stats.role` | `role`, `type (improvement, winning, performance)`, `order` `params` |
`.stats.champion` | `name` |
`.stats.champs` | `type (played, winning, rated)`, `order`, `params` |
`.champion.all` | `none` |
`.champion.specific`| `name` |
`.champion.general`| `name` |
`.champion.skills`| `name`, `order` |
`.champion.items`| `name`, `starting (True, False)`, `order` |
`.champion.runes`| `name`, `order` |
`.champion.matchup`| `name`, `enemy` |


## contributing
Feel free to contribute, let's just try to keep it readable :)

## Release History
  * 1.0.0 Initial release
  * 1.0.1 Fixes to calls to Champions and Stats

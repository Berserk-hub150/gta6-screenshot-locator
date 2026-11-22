# Screenshot Locator

Locate the minimap crop of a screenshot on a user-supplied GTA VI atlas. Returns three spatially distinct candidates, correlation scores and pixel coordinates.

## Quick start

```sh
python -m pip install -r requirements.txt
python locate.py demo/atlas.png demo/query.png
```

## Using your own material

The illustrated sample returns (126, 117). Crop the minimap and use a reference at the same scale and orientation. The algorithm works on matching map textures. Street-level photos require a different reference database. Repeated textures can produce ambiguous matches.

Independent fan project. Grand Theft Auto is a trademark of its respective owners.

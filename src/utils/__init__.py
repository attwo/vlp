import json
import hashlib


def get_dict_hash(source: dict):
    hash_material = json.dumps(source).encode()
    return hashlib.md5(hash_material).hexdigest()

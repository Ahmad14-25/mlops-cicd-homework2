import hashlib

def hash_feature(value: str, num_buckets: int = 100) -> int:
    return int(hashlib.md5(value.encode()).hexdigest(), 16) % num_buckets

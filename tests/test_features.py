from app.features import hash_feature

def test_hash_feature_consistency():
    assert hash_feature("mlops", 10) == hash_feature("mlops", 10)

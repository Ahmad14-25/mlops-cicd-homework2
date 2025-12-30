from app.features import hash_feature
from app.model import predict

def test_model_pipeline():
    result = predict(hash_feature("test"))
    assert result in [0, 1]

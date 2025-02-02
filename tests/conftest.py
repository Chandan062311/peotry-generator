import pytest
from unittest.mock import Mock, patch

@pytest.fixture(autouse=True)
def mock_transformers():
    with patch('transformers.AutoTokenizer') as mock_tokenizer, \
         patch('transformers.AutoModelForCausalLM') as mock_model:
        
        tokenizer = Mock()
        tokenizer.decode.return_value = "Mocked poem text"
        mock_tokenizer.from_pretrained.return_value = tokenizer
        
        model = Mock()
        model.generate.return_value = [[1, 2, 3]]
        mock_model.from_pretrained.return_value = model
        
        yield
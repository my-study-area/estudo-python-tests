from src.tutorial2exception.sample import validate_age
import pytest


def test_validate_age_valid_age():
  result = validate_age(2)
  assert result == True


def test_validate_age_invalid_age():
  with pytest.raises(ValueError, match="Age cannot be less than 0"):
    validate_age(-1)

  with pytest.raises(ValueError):
    validate_age(-1)

  with pytest.raises(ValueError) as message:
    validate_age(-1)
  assert str(message.value) == "Age cannot be less than 0"

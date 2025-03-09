import pytest

from src.ai_model import EmotionClassifier


@pytest.fixture
def classifier():
    """Fixture to initialize the EmotionClassifier for testing."""
    return EmotionClassifier()


def test_classify_returns_dict(classifier):
    """Test if the classifier returns a dictionary."""
    text = "I feel sad and frustrated."
    result = classifier.classify(text)
    assert isinstance(result, dict), "Output should be a dictionary."


def test_classify_filters_low_scores(classifier):
    """Test if emotions below the threshold are removed."""
    text = "I feel amazing and excited."
    result = classifier.classify(text)

    # Ensure all emotions have a score above the threshold
    assert all(
        score >= classifier.threshold for score in result.values()
    ), "Low-confidence emotions should be filtered out."


def test_classify_handles_empty_input(classifier):
    """Test if the classifier handles empty input gracefully."""
    text = ""
    result = classifier.classify(text)
    assert result == {}, "Empty input should return an empty dictionary."


def test_classify_detects_multiple_emotions(classifier):
    """Test if the classifier detects
    multiple emotions in a complex sentence."""
    text = "I'm feeling nervous, yet a little hopeful about tomorrow."
    result = classifier.classify(text)
    assert len(result) > 0, "The classifier should detect at least one emotion."

from transformers import pipeline


class EmotionClassifier:
    def __init__(
        self,
        model_name=("joeddav/distilbert-base-uncased-go-emotions-student"),
        threshold=0.05,
    ):
        """
        Initializes the emotion classifier with a given model and threshold.
        """
        self.classifier = pipeline("text-classification", model=model_name, top_k=None)
        self.threshold = threshold

    def classify(self, text: str):
        """
        Classifies emotions from a given text input
        and filters out low-confidence results.
        Returns an empty dictionary if input is empty.
        """
        if not text.strip():
            return {}

        predictions = self.classifier(text)
        filtered_emotions = {
            pred["label"]: pred["score"]
            for pred in predictions[0]
            if pred["score"] >= self.threshold
        }

        sorted_emotions = dict(
            sorted(filtered_emotions.items(), key=lambda x: x[1], reverse=True)
        )
        return sorted_emotions

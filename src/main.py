import argparse

from src.ai_model import EmotionClassifier


def main():
    """CLI entry point for emotion classification."""
    parser = argparse.ArgumentParser(description="Analyze emotions in a text.")
    parser.add_argument(
        "text", type=str, help="Journal entry or text input for emotion analysis"
    )
    args = parser.parse_args()

    classifier = EmotionClassifier()
    emotions = classifier.classify(args.text)

    if emotions:
        print("\nDetected emotions:")
        for emotion, score in emotions.items():
            print(f"{emotion}: {score:.4f}")
    else:
        print("\nNo strong emotions detected.")


if __name__ == "__main__":
    main()

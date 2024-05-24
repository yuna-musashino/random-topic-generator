import argparse
from .topics import get_random_topic, get_topics_by_category

def main():
    parser = argparse.ArgumentParser(description="Generate a random topic.")
    parser.add_argument(
        "-c", "--category", type=str, help="Specify a category for the topic."
    )
    args = parser.parse_args()

    if args.category:
        topic = get_topics_by_category(args.category)
    else:
        topic = get_random_topic()

    if topic:
        print(f"Your random topic is: {topic}")
    else:
        print("No topics found for the specified category.")

if __name__ == "__main__":
    main()

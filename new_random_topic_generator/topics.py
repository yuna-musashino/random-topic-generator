import random

topics = {
    "general": [
        "What is your favorite book and why?",
        "Describe a memorable vacation.",
        "If you could have any superpower, what would it be?",
    ],
    "technology": [
        "What are the latest trends in AI?",
        "How is blockchain technology evolving?",
        "Discuss the impact of 5G technology."
    ],
    "science": [
        "Explain the theory of relativity.",
        "What are the current challenges in quantum computing?",
        "How do vaccines work?"
    ]
}

def get_random_topic():
    all_topics = [item for sublist in topics.values() for item in sublist]
    return random.choice(all_topics) if all_topics else None

def get_topics_by_category(category):
    return random.choice(topics[category]) if category in topics else None

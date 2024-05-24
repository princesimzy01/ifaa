import spacy
from my_ifa_system import OduIfa
import sqlite3
from odu_imp import get_odu_ifa_by_name

nlp = spacy.load("en_core_web_sm")

knowledge_base = {
    "Eji Ogbe": ["new beginnings", "prosperity", "success", "growth", "opportunity"],
    "Oyeku Meji": ["endings", "transitions", "death", "closure", "finality"],
    "Iwori Meji": ["conflict", "deception", "struggle", "dishonesty", "challenge"],
    "Odi Meji": ["stability", "foundation", "strength", "security", "support"],
    # Add more Odu Ifa and their associated keywords
}


def preprocess_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return tokens


def match_question_to_odu(question, knowledge_base):
    tokens = preprocess_text(question)
    matched_odu = {}

    for odu, keywords in knowledge_base.items():
        match_count = sum(1 for token in tokens if token in keywords)
        if match_count > 0:
            matched_odu[odu] = match_count

    if matched_odu:
        best_match = max(matched_odu, key=matched_odu.get)
        return best_match
    else:
        return "No matching Odu Ifa found for your question."


def main():
    print("Welcome to the Ifa Divination Inference Engine")
    while True:
        question = input("Ask a question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        odu = match_question_to_odu(question, knowledge_base)

        the_odu = get_odu_ifa_by_name(odu.lower())

        if the_odu:
            print(f"Odu Ifa: {the_odu.odu_name.capitalize()}")
            print("Verses:")
            for verse in the_odu.verses:
                print(f" {verse}")
            print("Meanings:")
            for meaning in the_odu.meanings:
                print(f" {meaning}")
            print("Advice:")
            for advice in the_odu.advice:
                print(f" {advice}")
        else:
            print("Odu Ifa not found")


if __name__ == "__main__":
    main()

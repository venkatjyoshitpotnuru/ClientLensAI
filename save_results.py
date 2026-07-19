import json
import os
from datetime import datetime


OUTPUT_FOLDER = "outputs"


def save_analysis(data):

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    filename = datetime.now().strftime(
        "analysis_%Y%m%d_%H%M%S.json"
    )

    path = os.path.join(OUTPUT_FOLDER, filename)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return path


def save_review(status, notes):

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    filename = datetime.now().strftime(
        "review_%Y%m%d_%H%M%S.json"
    )

    path = os.path.join(OUTPUT_FOLDER, filename)

    review = {
        "review_status": status,
        "review_notes": notes,
        "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open(path, "w", encoding="utf-8") as file:
        json.dump(review, file, indent=4)

    return path
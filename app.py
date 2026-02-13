from flask import Flask, request, jsonify
import os, unicodedata, difflib

app = Flask(__name__)

POEMS_FOLDER = "vers_tar"  # ide kell a .txt fájlokat rakni

def normalize(text):
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    return "".join(c for c in text if unicodedata.category(c) != "Mn")

def load_offline_poems():
    poems = []
    for filename in os.listdir(POEMS_FOLDER):
        if filename.endswith(".txt"):
            path = os.path.join(POEMS_FOLDER, filename)
            author = filename.replace(".txt", "").replace("_", " ").title()
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            current_title = None
            current_text = []
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if line.isupper() and len(line) < 100:
                    if current_title and current_text:
                        poems.append({
                            "author": author,
                            "title": current_title,
                            "text": "\n".join(current_text)
                        })
                    current_title = line
                    current_text = []
                else:
                    current_text.append(line)
            if current_title and current_text:
                poems.append({
                    "author": author,
                    "title": current_title,
                    "text": "\n".join(current_text)
                })
    return poems

poems = load_offline_poems()

def search_offline(snippet):
    results = []
    norm_snippet = normalize(snippet)
    for poem in poems:
        lines = poem["text"].split("\n")
        best_ratio = 0
        best_line = ""
        for line in lines:
            norm_line = normalize(line)
            ratio = difflib.SequenceMatcher(None, norm_snippet, norm_line).ratio()
            if ratio > best_ratio:
                best_ratio = ratio
                best_line = line
        if best_ratio >= 0.699:
            results.append({
                "author": poem["author"],
                "title": poem["title"],
                "context": best_line
            })
    return results

@app.route("/search")
def search():
    snippet = request.args.get("snippet", "")
    return jsonify(search_offline(snippet))

if __name__ == "__main__":
    app.run(debug=True)

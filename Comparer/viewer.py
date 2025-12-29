from flask import Flask, render_template
import importlib.util
import sys

# Import data.py normally
from data import test_comparisons

# Import data-answers.py using importlib (handles hyphen in filename)
spec = importlib.util.spec_from_file_location("data_answers", "data-answers.py")
data_answers = importlib.util.module_from_spec(spec)
sys.modules["data_answers"] = data_answers
spec.loader.exec_module(data_answers)
test_comparison_expected_answers = data_answers.test_comparison_expected_answers

app = Flask(__name__)

@app.route('/')
def index():
    # Combine comparisons with their answers
    combined = []
    for i, comparison in enumerate(test_comparisons):
        answer = test_comparison_expected_answers[i] if i < len(test_comparison_expected_answers) else None
        combined.append({
            'comparison': comparison,
            'answer': answer
        })

    # Calculate stats
    total = len(combined)
    arbitrageable = sum(1 for item in combined if item['answer'] == True)
    not_arbitrageable = sum(1 for item in combined if item['answer'] == False)

    return render_template(
        'index.html',
        comparisons=combined,
        total=total,
        arbitrageable=arbitrageable,
        not_arbitrageable=not_arbitrageable
    )

if __name__ == '__main__':
    print("🚀 Starting Market Comparison Viewer on http://127.0.0.1:7039")
    print("⚠️  Make sure to use HTTP (not HTTPS) in your browser!")
    app.run(host='127.0.0.1', port=7039, debug=True)

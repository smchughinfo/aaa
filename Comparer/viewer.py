from flask import Flask, render_template, request
import json
import logging
from pathlib import Path

# Import experimental test data and prompts
from EXPERIMENTAL_TEST_DATA import data
from EXPERIMENTAL_SYSTEM_PROMPTS import prompts

app = Flask(__name__)

def get_all_results():
    """Get all result files with their metadata"""
    results_dir = Path("EXPERIMENTAL_RESULTS")
    result_files = []

    for file in results_dir.glob("*.json"):
        # Parse filename: {prompt_num}_{data_num}_{data_limit}_{batch_size}.json
        parts = file.stem.split('_')
        if len(parts) == 4:
            result_files.append({
                'filename': file.name,
                'prompt_num': parts[0],
                'data_num': parts[1],
                'data_limit': parts[2],
                'batch_size': parts[3],
                'modified': file.stat().st_mtime
            })

    # Sort by modification time, newest first
    result_files.sort(key=lambda x: x['modified'], reverse=True)
    return result_files

def load_results(prompt_num, data_num, data_limit, batch_size):
    """Load specific results file"""
    results_dir = Path("EXPERIMENTAL_RESULTS")
    filename = f"{prompt_num}_{data_num}_{data_limit}_{batch_size}.json"
    filepath = results_dir / filename

    if not filepath.exists():
        return None

    with open(filepath, 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    # Get all available results
    all_results = get_all_results()

    if not all_results:
        return "No results found! Run an experiment first.", 404

    # Get selected result from URL params or use most recent
    prompt_num = request.args.get('prompt', all_results[0]['prompt_num'])
    data_num = request.args.get('data', all_results[0]['data_num'])
    data_limit = request.args.get('limit', all_results[0]['data_limit'])
    batch_size = request.args.get('batch', all_results[0]['batch_size'])

    # Load selected results
    results = load_results(prompt_num, data_num, data_limit, batch_size)

    if not results:
        return f"Results not found for {prompt_num}_{data_num}_{data_limit}_{batch_size}", 404

    # Load test data and prompt
    test_data = data[data_num][:int(data_limit)]
    prompt_text = prompts.get(prompt_num, "Prompt not found")

    # Combine test data with results
    combined = []
    for i, comparison_data in enumerate(test_data):
        result = results[i] if i < len(results) else None

        combined.append({
            'comparison': comparison_data,
            'result': result
        })

    # Calculate stats
    total = len(combined)
    correct = sum(1 for item in combined if item['result'] and item['result'].get('categorized_correctly') == True)
    incorrect = sum(1 for item in combined if item['result'] and item['result'].get('categorized_correctly') == False)
    accuracy = (correct / total * 100) if total > 0 else 0

    # Current selection metadata
    current_selection = {
        'prompt_num': prompt_num,
        'data_num': data_num,
        'data_limit': data_limit,
        'batch_size': batch_size,
        'prompt_text': prompt_text
    }

    return render_template(
        'index.html',
        comparisons=combined,
        total=total,
        correct=correct,
        incorrect=incorrect,
        accuracy=accuracy,
        all_results=all_results,
        current_selection=current_selection
    )

if __name__ == '__main__':
    logging.info("🚀 Starting Market Comparison Viewer on http://127.0.0.1:7039")
    logging.info("⚠️  Make sure to use HTTP (not HTTPS) in your browser!")
    app.run(host='127.0.0.1', port=7039, debug=True)

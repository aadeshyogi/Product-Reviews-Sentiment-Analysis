# Product Reviews Sentiment Analysis

An NLP and deep-learning project that predicts the sentiment of a product review as **Positive**, **Neutral**, or **Negative**. The project includes a Streamlit interface where users can enter a review and view the predicted sentiment along with a confidence score.

## Features

- Predicts sentiment for user-provided product reviews.
- Supports three sentiment classes: Positive, Neutral, and Negative.
- Preprocesses review text before inference.
- Displays the predicted class and confidence score in a Streamlit web app.
- Loads a trained Keras model and saved preprocessing assets.

## Tech Stack

- **Language:** Python
- **Deep Learning:** TensorFlow, Keras
- **NLP:** Text preprocessing, tokenization, stop-word filtering, sequence padding
- **Web App:** Streamlit
- **Numerical Processing:** NumPy

## Project Structure

```text
Product-Reviews-Sentiment-Analysis/
├── app.py
├── banner.png
├── requirements.txt
├── sentiment_classifier.keras
├── tokenizer.pkl
├── stopwords.pkl
├── Product Reviews Sentiment Analysis.ipynb
├── training_curves2.png
└── README.md
```

If you organize the model assets into a `models/` folder or the notebook and plots into separate folders, update the file paths in `app.py` accordingly.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aadeshyogi/Product-Reviews-Sentiment-Analysis.git
cd Product-Reviews-Sentiment-Analysis
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your repository's URL.

### 2. Create and activate a virtual environment

**Windows**
```bash
python -m venv myenv
myenv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to use the application.

## How to Use

1. Launch the Streamlit app.
2. Enter or paste a product review into the text box.
3. Click **Predict**.
4. Review the predicted sentiment and confidence score.

## Model and Inference

The application loads the saved model from `sentiment_classifier.keras`, along with `tokenizer.pkl` and `stopwords.pkl` for text preparation. The label mapping in the application is:

| Class ID | Sentiment |
|---:|---|
| 0 | Negative |
| 1 | Neutral |
| 2 | Positive |

Keep these assets consistent with the preprocessing and label mapping used during model training.

## Dataset

The project notebook and dataset file can document the source, preparation, and analysis of the product reviews used in the project. Before publishing a dataset, confirm that its license and source terms permit redistribution. If redistribution is not allowed, do not commit the dataset; instead, provide the original source and instructions for obtaining it.

## Repository Notes

- Do **not** upload your virtual environment (`myenv/`, `venv/`, or `.venv/`).
- Do **not** upload `.ipynb_checkpoints/` or `__pycache__/`.
- Check `config.json` and `config2.json` before committing them. Never publish API keys, passwords, tokens, or other secrets.
- Check the size of `sentiment_classifier.keras`. GitHub blocks regular Git files larger than 100 MB; use Git LFS or an appropriate release/download method if needed.
- Keep `requirements.txt` aligned with the packages the app actually imports.

## Results

Add verified evaluation metrics here after checking the notebook's evaluation output. Do not report an accuracy value unless it is confirmed by the model's test-set results.

## Future Improvements

- Add more evaluation metrics, such as precision, recall, and F1-score.
- Improve handling of misspellings, emojis, and mixed-language reviews.
- Deploy the Streamlit application online.
- Add a confusion matrix and class-wise performance visualizations.

## Author

**Aadesh Yogi**

- GitHub: [aadeshyogi12](https://github.com/aadeshyogi12)
- LinkedIn: [aadeshyogi](https://linkedin.com/in/aadeshyogi)

---

If you find this project useful, feel free to star the repository.

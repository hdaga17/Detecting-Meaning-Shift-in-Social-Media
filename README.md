
# Detecting Meaning Shift in Social Media

![License](https://img.shields.io/github/license/hdaga17/Detecting-Meaning-Shift-in-Social-Media)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![NLP](https://img.shields.io/badge/NLP-Embeddings-orange)
![Status](https://img.shields.io/badge/status-Completed-brightgreen)

## Overview
This project is focused on detecting shifts in word meanings within social media content over time using advanced Natural Language Processing (NLP) techniques and Machine Learning (ML) algorithms. By analyzing evolving language trends, this system captures subtle semantic changes, providing insights into how meanings of words shift with cultural and contextual variations.

## Table of Contents
1. [Project Motivation](#project-motivation)
2. [Methodology](#methodology)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Results](#results)
6. [Future Improvements](#future-improvements)
7. [Contributing](#contributing)
8. [License](#license)

## Project Motivation
As language constantly evolves, social media is a primary space where meanings of words can change rapidly. This project aims to:
- Track and quantify these shifts.
- Identify culturally and temporally influenced changes in semantics.
- Visualize these shifts to understand underlying linguistic trends.

## Methodology
The project pipeline includes the following stages:

1. **Data Collection**: Gathered social media text data relevant to specific words of interest.
2. **Preprocessing**: Applied tokenization, lemmatization, POS tagging, and removal of stop words using libraries like `spaCy` and `NLTK`.
3. **Embedding Generation**: 
   - Utilized static (Word2Vec) and contextual embeddings (BERT) to capture semantic representations of words.
   - Implemented temporal embeddings to compare changes in word usage over different time frames.
4. **Meaning Shift Detection**:
   - Calculated cosine similarity across embeddings from various time intervals to quantify semantic drift.
   - Used clustering (e.g., K-Means) and dimensionality reduction techniques (t-SNE, PCA) to visualize these shifts effectively.
5. **Visualization and Analysis**: Developed graphs and clustering plots to visualize the semantic trajectories of words across time.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/hdaga17/Detecting-Meaning-Shift-in-Social-Media.git
   cd Detecting-Meaning-Shift-in-Social-Media
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

3. Install any additional NLP resources (e.g., spaCy models):
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Usage
To detect meaning shifts on a specific dataset:

1. **Data Preprocessing**: Run the `preprocess_data.py` script to clean and tokenize data.
   ```bash
   python preprocess_data.py --input data/social_media_data.csv --output data/processed_data.csv
   ```

2. **Generate Embeddings**: Use the `generate_embeddings.py` script to create temporal word embeddings.
   ```bash
   python generate_embeddings.py --input data/processed_data.csv --model Word2Vec
   ```

3. **Meaning Shift Detection**: Execute the `detect_shift.py` script to calculate and visualize shifts.
   ```bash
   python detect_shift.py --input embeddings/ --output results/
   ```

4. **Visualization**: View the results using the plots generated in the `results/` directory.

## Results
The project effectively detected meaning shifts in social media text. Results indicated significant semantic drift for certain terms, influenced by cultural events, popular media, and emerging trends. These shifts were visualized in the form of t-SNE plots and PCA-reduced embeddings.

## Future Improvements
- **Enhanced Data Collection**: Integrate APIs (e.g., Twitter API) for real-time data gathering.
- **Multi-lingual Support**: Extend the model to detect meaning shifts across multiple languages.
- **Advanced Models**: Experiment with more recent embedding techniques (e.g., RoBERTa, T5) for enhanced semantic analysis.

## Contributing
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request. For major changes, please open an issue first to discuss your ideas.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For further questions or suggestions, feel free to reach out to the project maintainer at hdaga17.

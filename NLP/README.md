# Social Media Trend Analysis

## Project Overview

Social media is a dynamic platform where trends emerge and fade rapidly. This project explores the mechanics behind social media trends using machine learning, sentiment analysis, and natural language processing (NLP). Our analysis is aimed at identifying popular topics, gauging public opinion, and understanding the lifespan of trends.

### Key Objectives
1. Analyze social media content to identify trending topics.
2. Perform sentiment and emotion analysis on social media posts.
3. Implement transformer-based models and topic modeling tools for deeper insights.

## System Architecture

The project pipeline includes the following stages:
1. **Data Ingestion**: Collecting social media data using APIs.
2. **Metadata Parsing**: Extracting and storing tweet metadata for analysis.
3. **Preprocessing**: Tokenization, stopword removal, and lemmatization.
4. **Sentiment and Emotion Analysis**: Using VADER, NRC Lexicon, and fine-tuned BERT models.
5. **Topic Modeling**: Implementing BERTopic and LDA for thematic clustering.
6. **Visualization**: Creating interactive dashboards and visualizations.
7. **Storage**: Saving processed outputs for downstream tasks.



## Technologies and Tools

- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn, NLTK, Matplotlib, Seaborn, Plotly, Transformers, BERTopic
- **Platform**: Jupyter Notebook
- **Hardware**: Local machine with 16GB RAM

## Dataset

The project uses a CSV dataset containing social media posts with metadata. The dataset includes the following features:
- Post content
- User metadata
- Sentiment labels

## Results

1. **Sentiment Analysis**: Achieved high accuracy with BERT compared to VADER for sentiment classification.
2. **Emotion Analysis**: Implemented NRC Lexicon for detecting emotional granularity.
3. **Topic Modeling**: Generated coherent topic clusters using BERTopic.

### Key Visualizations
- Word count distribution
- Sentiment distribution (BERT-based)
- Emotion frequency and correlation heatmaps
- Topic progression timelines



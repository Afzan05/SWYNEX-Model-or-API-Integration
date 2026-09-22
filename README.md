# SWYNEX-Model-or-API-Integration
# SWYNEX Model Integration Prototype

This repository contains a prototype built for Task 2 of the SWYNEX internship. It demonstrates how to integrate a public AI model to solve a natural language processing problem (Sentiment Analysis).

## Defined Problem
Businesses need to automatically categorize user feedback as positive or negative to improve customer service. This prototype uses a pre-trained Hugging Face transformer model to evaluate the sentiment of text inputs.

## Setup Instructions
1. Clone this repository.
2. Install the required library: `pip install transformers`
3. Run the script: `python main.py`

## Example Inputs and Outputs
**Input 1:** 'I absolutely loved working on this AI integration task!'
**Output 1:** Label: POSITIVE, Confidence: 0.9998

**Input 2:** 'The documentation was a bit confusing and hard to follow.'
**Output 2:** Label: NEGATIVE, Confidence: 0.9982

*Note: This prototype runs locally using an open-source model and does not require any secret API keys.*

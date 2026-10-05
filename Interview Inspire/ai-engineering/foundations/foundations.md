# AI Foundations Interview Questions

---

## Python for AI & Data Science
1. What is the difference between shallow copy and deep copy in Python?
2. How do Python Generators and the `yield` keyword manage memory when streaming large datasets?
3. How do Python Decorators work? How do you write a decorator with arguments?
4. What is the Global Interpreter Lock (GIL) in CPython, and how does it impact multi-threading vs multi-processing?
5. How does vectorization in NumPy achieve 10x-100x speedup over standard Python loops?
6. In PyTorch, what is `torch.Tensor` vs `nn.Parameter`? How does `autograd` build the dynamic computation graph?
7. What is the difference between `model.eval()` and `torch.no_grad()` during inference?

---

## Mathematics for Machine Learning
1. What is Matrix Multiplication, and why are GPUs exceptionally well-suited for neural network calculations?
2. What are Eigenvalues and Eigenvectors, and how are they used in Principal Component Analysis (PCA)?
3. What is Gradient Descent (Batch, Mini-batch, Stochastic)? What is the mathematical significance of the learning rate?
4. How does Backpropagation use the Chain Rule of calculus to compute partial derivatives of the loss function?
5. What is the difference between Mean Squared Error (MSE), Cross-Entropy Loss, and Contrastive Loss?
6. What is Bayes' Theorem, and how is it used in probabilistic reasoning?
7. What is the difference between L1 Regularization (Lasso) and L2 Regularization (Ridge)? Why does L1 lead to sparsity?

---

## Core Machine Learning Fundamentals
1. What is the Bias-Variance Tradeoff? How do you diagnose high bias (underfitting) vs high variance (overfitting)?
2. What are the key evaluation metrics for classification (Accuracy, Precision, Recall, F1-Score, ROC-AUC)? When is Accuracy misleading?
3. How do decision tree ensembles (Random Forest vs Gradient Boosted Trees like XGBoost/LightGBM) differ in training and aggregation?
4. What is K-Fold Cross Validation, and how does it prevent data leakage?
5. How do you handle imbalanced datasets (SMOTE, class weighting, focal loss)?

---

## Deep Learning & Neural Network Architectures
1. Why are Activation Functions non-linear (ReLU, GeLU, Sigmoid, Softmax)? What happens if you stack linear layers without non-linearities?
2. What are the Exploding and Vanishing Gradient problems? How do Residual Connections (ResNets) and Layer Normalization solve them?
3. What is the difference between Batch Normalization and Layer Normalization? Why do Transformers prefer LayerNorm?
4. How does Dropout work during training vs inference?
5. What are common optimizers (SGD with Momentum, RMSprop, Adam, AdamW)? Why is AdamW preferred for Transformers?

---

## Transformers & NLP Concepts
1. Explain the Self-Attention mechanism mathematically: why do we compute `Softmax((Q * K^T) / sqrt(d_k)) * V`?
2. Why do we divide by `sqrt(d_k)` (scaling factor) in Scaled Dot-Product Attention?
3. What is Multi-Head Attention, and what intuition does it provide over single-head attention?
4. What are Positional Encodings (Sinusoidal vs Learnable vs RoPE - Rotary Position Embedding)? Why is RoPE widely used in modern LLMs (Llama, Mistral)?
5. What are the structural differences between Encoder-Only (BERT), Decoder-Only (GPT, Llama), and Encoder-Decoder (T5) architectures?
6. How do subword tokenization algorithms work (Byte-Pair Encoding - BPE, WordPiece, SentencePiece)? What is byte-fallback BPE?

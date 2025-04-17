---
id: j8n7h2if1c9beltgij24osq
title: Aiengineering
desc: ''
updated: 1744554285957
created: 1744545671363
---


# What's AI Engineering? 

AI Engineering is the discipline of levering foundational models to build applications. It's a discipline that emerged due to the hard work of machine learning engineers and allowing their models to be open sourced.

Previosuly, if someone want to do an app that's dependent on machine learning algorithms, they will have to first do the data science pipelines and then train a model and then build the app. Currently, due to the emergin numbers of open sourced moels, the team can instead use those open sourced models and build the app then fine tune them or decide to build their own models once the idea of the app proved success.

## Whats foundational models, LLMs and LMMs?

Foundational models are models that are already been trained on large dataset for multiple tasks where then they can be used and fine tuned to specific tasks.

LLMs stands for large language models. They are models which uses most likely the **transformers architecture!**. Their purpose is to convey more context from the data so that it can predict the next word correctly.

### How does the transformer architecture works?

The backbone of the transoformers architecture is **the attention mechanism.** Basically, the transformers consists of Input, **embedding** the input, N x attention layers + **MLPs**, + Output layer, and then the output.


#### What are embeddings?

Embeddings are matrices to translate the semantic meanings of words. E.g King is close to queen. But embeddings do not convey context in sentences. To do that, we need **attention mechanism** 


#### Whats the difference between embeddings and queries (in the attention mechanism)?
Basically, the embedding after the input provide the global semantic meaning of the word to other words. For example, bank is related to finance. This is in a very generic way where you can think of it as there's a global dictionary where we can compare the word to all other words.

The query instead focus on the semantic meaning in the sentence itself. It kinda applies the same thing as the embedding but locally.

#### Whats the attention mechanism?

The attention mechanism consist of three elements:
1- The Query (Q)
2- The Key (K)
3- The Value (V)

Imagine one of the input embedded was: Marwan is learning AI Engineering.

First, there's a query matrix. Each word in the input example, would have a column. This column is 



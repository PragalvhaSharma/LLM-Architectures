# LLM Architectures: A Collection of Explorations

Welcome to the **LLM Architectures** repository! This collection showcases various concepts, techniques, and architectures related to Large Language Models (LLMs). These files document my learning journey as I explored the cutting-edge methods that enhance LLM capabilities and applications.

## Repository Overview

This repository contains Jupyter notebooks and scripts that demonstrate practical implementations of LLM-related techniques. Below is an overview of the contents:

### Notebooks

1. **BasicReflection.ipynb**  
   Demonstrates how reflection mechanisms can enable LLMs to refine their responses iteratively for improved accuracy and coherence.

2. **ChainOfThought.ipynb**  
   Implements chain-of-thought prompting, a technique enabling LLMs to solve complex tasks step by step by reasoning through intermediate stages.  
   - **Key Resource**: [Chain-of-Thought Prompting: Helping LLMs Learn by Example](https://deepgram.com/learn/chain-of-thought-prompting-guide)

3. **LATS.ipynb**  
   Explores **Latent Alignment and Task-Specific Fine-Tuning**, a method for improving LLM task performance.

4. **LLMcompiler.ipynb**  
   Illustrates the use of LLMs for compiling or generating executable code based on high-level input specifications.

5. **ReAct.ipynb**  
   Combines reasoning and action frameworks to improve LLM decision-making for interactive tasks.  
   - **Key Resource**: [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)

6. **ReasoningWithoutObservation.ipynb**  
   Investigates techniques enabling LLMs to reason without explicit context or external observation.

7. **ReflectionActor.ipynb**  
   Introduces the **Reflection Actor** framework, a method for fine-tuning LLMs with iterative feedback loops.

8. **TreeOfThought.ipynb**  
   Implements the **Tree of Thought** approach, where models explore multiple reasoning paths before converging on a solution.

9. **Few-shot.ipynb**  
   Demonstrates few-shot learning techniques to adapt LLMs to novel tasks using minimal examples.

10. **Langgraph.ipynb**  
    Explores graph-based approaches to language understanding and how they can complement LLM performance.

11. **PromptChaining.ipynb**  
    Examines chaining prompts together to handle multi-step workflows efficiently.

12. **SelfConsistency.ipynb**  
    Implements self-consistency strategies, where LLMs validate responses by comparing results across multiple iterations.

13. **Zero-shot.ipynb**  
    Explores zero-shot capabilities of LLMs, showcasing their ability to generalize to unseen tasks without explicit training.  
    - **Key Resource**: [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)

### Additional Files

- **main.py**: Serves as an entry point for experimenting with various architectures.
- **requirements.txt**: Lists dependencies needed to run the notebooks and scripts.
- **LangGraph/**: A directory containing resources and implementations related to language graph modeling.

## Learning Highlights

Below are additional techniques and concepts included in this repository:

1. **Automatic Chain of Thought (Auto-CoT) Prompting**  
   Leverages LLMs to generate reasoning chains automatically, enhancing scalability.  
   - **Key Resource**: [Automatic Chain of Thought Prompting](https://openreview.net/forum?id=5NTt8GFjUHkr)

2. **Plan-and-Solve Prompting**  
   Breaks down complex tasks into subtasks, addressing limitations of zero-shot CoT prompting.  
   - **Key Resource**: [Plan-and-Solve Prompting](https://arxiv.org/abs/2305.04091)

3. **Hint of Thought (HoT) Prompting**  
   Decomposes reasoning into explainable sub-questions for interpretable outputs.  
   - **Key Resource**: [Hint of Thought Prompting](https://arxiv.org/abs/2305.11461)

4. **Cross-Lingual Chain of Thought Prompting**  
   Extends CoT prompting to multiple languages for cross-linguistic reasoning.  
   - **Key Resource**: [Cross-Lingual Prompting](https://aclanthology.org/2023.emnlp-main.163)

## Getting Started

### Prerequisites

- Python 3.8+
- Recommended: Jupyter Notebook or Jupyter Lab for interactive exploration
- Install dependencies using `pip install -r requirements.txt`

### Usage

1. Clone the repository:  
   ```bash
   git clone https://github.com/PragalvhaSharma/LLM-Architectures.git
   cd LLM-Architectures
   ```

2. Install the required Python packages:  
   ```bash
   pip install -r requirements.txt
   ```

3. Open the notebooks in Jupyter:  
   ```bash
   jupyter notebook
   ```

4. Explore each notebook to dive into a specific architecture or technique.

## Why This Repository?

This collection is meant to document my learning journey and provide a resource for anyone curious about LLM techniques. Whether you are new to LLMs or exploring advanced topics, these implementations aim to serve as a starting point.

## Contributions

Feel free to contribute! If you have suggestions, improvements, or new techniques to add, submit a pull request or open an issue.

## License

This project is open-source and available under the [MIT License](LICENSE).


import os
from pathlib import Path



List_of_Files =[
    "docs/python_basics.txt",
    "docs/machine_learning.txt",
    "ingest.py",
]

for filepath in List_of_Files:
    filepath=Path(filepath)
    filedir = filepath.parent
    filename = filepath.name

    if filedir != Path("."):
        os.makedirs(filedir,exist_ok=True)
    if not filepath.exists():
        with open(filepath ,"w") as f:
            if filename == "python_basics.txt":
                f.write("""Python is a high-level, interpreted programming language created by Guido van Rossum in 1 991.
Python uses indentation to define code blocks instead of curly braces.
Python supports multiple programming paradigms including procedural, object-oriented, and functional programming.
The Python Package Index (PyPI) hosts over 400,000 packages that extend Python's capabili ties.
Python is widely used in data science, web development, automation, and artificial intell igence.
Python's philosophy emphasizes code readability and simplicity, summarized in the Zen of Python""")
            elif filename == "machine_learning.txt":
                f.write("""Machine le
                arning is a subset of artificial intelligence that enables systems to learn fro m data.
Supervised learning uses labeled training data to teach models to make predictions on new examples.
Unsupervised learning finds hidden patterns in data without any labeled examples.
Neural networks are computational models inspired by the structure of the human brain.
Overfitting occurs when a model learns training data too well and performs poorly on new unseen data.
Regularization techniques like dropout and L2 penalty help prevent overfitting in neural networks.
The training process involves adjusting model weights to minimize a loss function over ma
ny Lteratlons.""")
        print(f"Created:{filepath}")
    else:
        print(f"Already exists:{filepath}")

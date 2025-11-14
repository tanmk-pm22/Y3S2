# Y3S2 Course Materials

Jupyter notebook-based learning materials for Year 3 Semester 2 courses.

## Courses

### 📊 Distributed Parallel Processing
Learn parallel and distributed computing concepts through interactive notebooks.

**Location:** `distributed-parallel-processing/`

**Topics:**
- Introduction to parallel processing
- Parallel architectures
- Threading and multiprocessing
- Distributed computing fundamentals
- Message passing (MPI)
- MapReduce and Apache Spark

### 💼 English for Career Preparation
Develop professional English communication skills for career success.

**Location:** `english-career-preparation/`

**Topics:**
- Resume writing
- Cover letters
- Interview preparation
- Business communication
- Presentations
- Professional networking

## Repository Structure

```
Y3S2/
├── distributed-parallel-processing/
│   ├── 01-introduction/
│   ├── 02-parallel-architectures/
│   ├── 03-threading-multiprocessing/
│   ├── 04-distributed-computing/
│   ├── 05-message-passing/
│   ├── 06-mapreduce-spark/
│   ├── exercises/
│   ├── projects/
│   └── resources/
├── english-career-preparation/
│   ├── 01-resume-writing/
│   ├── 02-cover-letters/
│   ├── 03-interview-preparation/
│   ├── 04-business-communication/
│   ├── 05-presentations/
│   ├── 06-networking/
│   ├── exercises/
│   └── resources/
└── shared/
    ├── templates/      # Notebook templates
    ├── utilities/      # Helper functions
    └── data/          # Shared datasets
```

## Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch Jupyter:**
   ```bash
   jupyter lab
   # or
   jupyter notebook
   ```

3. **Start learning:**
   - Navigate to your course of interest
   - Follow the numbered modules sequentially
   - Complete exercises in each section

## Using the Notebook Template

A starter template is available at `shared/templates/notebook_template.ipynb`. Copy this template when creating new notebooks:

```bash
cp shared/templates/notebook_template.ipynb distributed-parallel-processing/01-introduction/topic.ipynb
```

## Contributing

Feel free to add your own notes, exercises, and examples as you progress through the courses.

# Sparse Matrix Operations

## 🔁 Clone the Repository

To get started, clone this repository using:

```bash
git clone https://github.com/Betelhemf567/data-structures-sparse-matrix.git
cd data-structures-sparse-matrix
```

# 🧮 Sparse Matrix Operations

This Python project allows you to **add**, **subtract**, and **multiply** sparse matrices efficiently using dictionary-based storage. It provides a command-line interface to select input files, choose operations, and save the results in a clean format.

---

## 📁 Project Structure

```
project-root/
│
├── sample_inputs/           # Directory containing input matrix files
│   ├── matrix1.txt
│   └── matrix2.txt
|   |¬¬¬matrix3.txt
│
├── results/                 # Output directory for result files (auto-generated if missing)
│
├── src/
│   └── sparse_matrix.py     # Main Python script with SparseMatrix class and CLI interface
│
└── README.md                # You are here
```

---

## 📦 Requirements

This project uses **only built-in Python libraries**, so no installation of external packages is needed.

- Python 3.7 or higher

---

## 📥 Input File Format

Each input matrix file must follow this format:

```
rows=<number_of_rows>
cols=<number_of_columns>
(row_index, column_index, value)
(row_index, column_index, value)
...
```

**Example:**
```
rows=3
cols=3
(0, 0, 5)
(1, 2, 8)
(2, 1, -3)
```

---

## 🚀 How to Run the Program

1. **Navigate to the `src/` directory** (where `sparse_matrix.py` is located):

```bash
cd src
```

2. **Run the script**:

```bash
python3 sparse_matrix.py
```

3. **Follow the on-screen prompts**:
   - Choose two matrix files from `sample_inputs/`
   - Select the operation: Add, Subtract, or Multiply
   - The program will save the result in the `results/` directory with a timestamped filename.

---

## 📤 Output

Each result file will be named like:

```
result_add_YYYYMMDD_HHMMSS.txt
```

Inside the file:

```
Result of Matrix A + Matrix B (3x3):
(0, 0, 5)
(1, 2, 14)
(2, 1, -3)
```

---

## ✅ Features

- Sparse representation using dictionaries for memory efficiency
- Simple command-line interface
- Validates input file format
- Handles addition, subtraction, and matrix multiplication
- Automatically creates output directory if missing
- Clear and user-friendly output

---

## 🧪 Example Use Case

```bash
📁 Available input files:
1. matrix_a.txt
2. matrix_b.txt
3. matrix_c.txt

🔢 Select the first matrix file by number:
> 1

🔢 Select the second matrix file by number:
> 2

🔧 Select operation to perform:
1. ➕ Add
2. ➖ Subtract
3. ✖️ Multiply
> 3

🧮 Performing calculation...
✅ Multiplication complete. 2 non-zero entries. Performed 6 multiplications.

💾 Result saved to: results/result_multiply_YYYYMMDD_HHMMSS.txt
```

---

## 🛠 Troubleshooting

- **Invalid matrix file format?** Ensure each file:
  - Starts with `rows=` and `cols=`
  - Contains matrix elements in `(row, col, value)` format

- **Wrong input file?** Just re-run the script and choose different files.

---

## 👩‍💻 Author

Developed by **Betelhem chelebo**  

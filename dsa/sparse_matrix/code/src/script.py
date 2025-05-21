import os
from datetime import datetime

# Custom exception for invalid matrix file format
class InvalidMatrixFormat(Exception):
    pass

# SparseMatrix class to handle operations on sparse matrices
class SparseMatrix:
    def __init__(self, filepath=None):
        self.rows = 0
        self.cols = 0
        self.elements = {}  # Dictionary to store non-zero elements with keys as (row, col)
        if filepath:
            self.load_from_file(filepath)

    # Load sparse matrix data from a file
    def load_from_file(self, filepath):
        print(f"\n📂 Loading matrix from '{filepath}'...")
        with open(filepath, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
            if len(lines) < 2:
                raise InvalidMatrixFormat("❌ Input file has insufficient data.")
            try:
                self.rows = int(lines[0].split('=')[1])
                self.cols = int(lines[1].split('=')[1])
            except:
                raise InvalidMatrixFormat("❌ Invalid row/col line format.")

            for line in lines[2:]:
                if not line.startswith("(") or not line.endswith(")"):
                    raise InvalidMatrixFormat("❌ Input file has wrong format")
                line = line.strip('()')
                parts = line.split(',')
                if len(parts) != 3:
                    raise InvalidMatrixFormat("❌ Incorrect number of values in matrix element")
                try:
                    row, col, val = map(int, parts)
                except:
                    raise InvalidMatrixFormat("❌ Matrix element values must be integers")
                self.elements[(row, col)] = val
        print("✅ Matrix loading complete.\n")

    # Add two sparse matrices
    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("❌ Matrix dimensions must match for addition.")
        result = SparseMatrix()
        result.rows = self.rows
        result.cols = self.cols
        result.elements = self.elements.copy()
        for key, value in other.elements.items():
            result.elements[key] = result.elements.get(key, 0) + value
        return result

    # Subtract one sparse matrix from another
    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("❌ Matrix dimensions must match for subtraction.")
        result = SparseMatrix()
        result.rows = self.rows
        result.cols = self.cols
        result.elements = self.elements.copy()
        for key, value in other.elements.items():
            result.elements[key] = result.elements.get(key, 0) - value
        return result

    # Multiply two sparse matrices
    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError(f"❌ Matrix sizes do not allow multiplication ({self.rows}x{self.cols} * {other.rows}x{other.cols}).")
        
        result = SparseMatrix()
        result.rows = self.rows
        result.cols = other.cols
        count = 0

        # Prepare dictionaries to speed up multiplication
        a_col_map = {}  # Maps column index to list of (row, value) for matrix A
        for (r, c), val in self.elements.items():
            a_col_map.setdefault(c, []).append((r, val))

        b_row_map = {}  # Maps row index to list of (col, value) for matrix B
        for (r, c), val in other.elements.items():
            b_row_map.setdefault(r, []).append((c, val))

        # Get common indices where multiplication is valid
        common_indices = set(a_col_map.keys()) & set(b_row_map.keys())

        temp_result = {}

        # Perform multiplication only on non-zero intersections
        for k in common_indices:
            for a_row, a_val in a_col_map[k]:
                for b_col, b_val in b_row_map[k]:
                    key = (a_row, b_col)
                    temp_result[key] = temp_result.get(key, 0) + a_val * b_val
                    count += 1

        result.elements = {k: v for k, v in temp_result.items() if v != 0}
        print(f"\n✅ Multiplication complete. {len(result.elements)} non-zero entries. Performed {count} multiplications.\n")
        return result

    # Retrieve the value of a specific matrix element
    def get_element(self, currRow, currCol):
        return self.elements.get((currRow, currCol), 0)

    # Set a matrix element value, removing it if the value is zero
    def set_element(self, currRow, currCol, value):
        if value != 0:
            self.elements[(currRow, currCol)] = value
        elif (currRow, currCol) in self.elements:
            del self.elements[(currRow, currCol)]

# Determine input and output directories relative to the script location
def get_base_dirs():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..'))
    input_dir = os.path.join(base_dir, 'sample_inputs')
    output_dir = os.path.join(base_dir, 'results')
    return input_dir, output_dir

# List all available .txt input files
def list_files(input_dir):
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"❌ The directory {input_dir} does not exist.")

    print("\n📄 Available files in:", input_dir)
    files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]
    for i, file in enumerate(files, start=1):
        print(f"  {i}. {file}")
    return files

# Generate a timestamped result filename
def generate_output_filename(output_dir, operation):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(output_dir, f"result_{operation}_{timestamp}.txt")

# Write the resulting sparse matrix to a file
def write_matrix_to_file(matrix, filename, label):
    with open(filename, 'w') as f:
        f.write(f"Result of {label} ({matrix.rows}x{matrix.cols}):\n")
        for key in sorted(matrix.elements):
            val = matrix.elements[key]
            if val != 0:
                f.write(f"({key[0]}, {key[1]}, {val})\n")

# Main interactive program logic
def main():
    input_dir, output_dir = get_base_dirs()
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = list_files(input_dir)

    print("\n👉 Select the first matrix file by number:")
    choice_a = int(input("Enter number: ")) - 1
    A = SparseMatrix(filepath=os.path.join(input_dir, files[choice_a]))

    print("\n👉 Select the second matrix file by number:")
    choice_b = int(input("Enter number: ")) - 1
    B = SparseMatrix(filepath=os.path.join(input_dir, files[choice_b]))

    print("\n📌 Select operation:")
    print("  1. Add")
    print("  2. Subtract")
    print("  3. Multiply")

    operation = ""
    while operation not in ['1', '2', '3']:
        operation = input("Enter your choice (1, 2, or 3): ").strip()
        if operation not in ['1', '2', '3']:
            print("❌ Invalid operation selected. Please choose 1, 2, or 3.")

    try:
        print("\n🧮 Calculating...")
        if operation == '1':
            result = A.add(B)
            label = "Matrix A + Matrix B"
            output_filename = generate_output_filename(output_dir, 'add')
        elif operation == '2':
            result = A.subtract(B)
            label = "Matrix A - Matrix B"
            output_filename = generate_output_filename(output_dir, 'subtract')
        else:
            result = A.multiply(B)
            label = "Matrix A * Matrix B"
            output_filename = generate_output_filename(output_dir, 'multiply')

        write_matrix_to_file(result, output_filename, label)
        print(f"\n💾 Result written to: {output_filename} with {len(result.elements)} non-zero values.")
        print(f"✅ Operation complete. You can check the results in the 'results' folder.\n")
    except Exception as e:
        print(f"❌ Error: {e}")

# Run the program
if __name__ == "__main__":
    main()

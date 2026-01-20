import pandas as pd
import multiprocessing
import os

def validate_and_parse_excel(file_path):
    """
    Validates and parses the Excel file to ensure mandatory columns are present.
    Optimized to handle large Excel files using multiprocessing.

    Args:
        file_path (str): Path to the Excel file.

    Returns:
        pd.DataFrame: Parsed DataFrame if validation is successful.

    Raises:
        ValueError: If mandatory columns are missing.
    """
    mandatory_columns = [
        'Input_column_name',
        'Input_table',
        'transformation',
        'output_column_name',
        'description'
    ]

    # Read the Excel file
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        raise ValueError(f"Error reading Excel file: {e}")

    # Validate mandatory columns
    missing_columns = [col for col in mandatory_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing mandatory columns: {', '.join(missing_columns)}")

    # Example optimization: Parallel processing for large datasets
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Split DataFrame into chunks for parallel processing
        chunks = [df[i:i + 1000] for i in range(0, len(df), 1000)]
        results = pool.map(process_chunk, chunks)

    # Combine results
    df = pd.concat(results, ignore_index=True)
    return df

def process_chunk(chunk):
    """
    Process a chunk of the DataFrame.

    Args:
        chunk (pd.DataFrame): A chunk of the DataFrame to process.

    Returns:
        pd.DataFrame: Processed chunk of the DataFrame.
    """
    # Example processing logic
    return chunk

def sanitize_file_path(file_path):
    """
    Ensures the file path is safe and prevents directory traversal attacks.

    Args:
        file_path (str): The input file path.

    Returns:
        str: Sanitized file path.

    Raises:
        ValueError: If the file path is unsafe.
    """
    base_dir = os.path.abspath("./uploads")  # Define a safe base directory
    abs_path = os.path.abspath(file_path)

    if not abs_path.startswith(base_dir):
        raise ValueError("Unsafe file path detected.")

    return abs_path

# Example usage
if __name__ == "__main__":
    try:
        file_path = "example_mapping_sheet.xlsx"  # Replace with actual file path
        safe_path = sanitize_file_path(file_path)
        print(f"Sanitized file path: {safe_path}")
        df = validate_and_parse_excel(safe_path)
        print("Excel file parsed successfully:")
        print(df.head())
    except ValueError as e:
        print(f"Validation error: {e}")
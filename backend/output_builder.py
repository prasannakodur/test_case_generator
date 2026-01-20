import pandas as pd

def build_output(test_cases):
    """
    Builds the output DataFrame from generated test cases and assigns unique IDs.

    Args:
        test_cases (list of dict): List of test case dictionaries.

    Returns:
        pd.DataFrame: DataFrame containing structured test case output.
    """
    # Assign unique IDs
    for idx, test_case in enumerate(test_cases, start=1):
        test_case['testcase_id'] = f"TC_{idx:03}"

    # Convert to DataFrame
    df = pd.DataFrame(test_cases)

    return df

def save_output(df, file_format='csv', file_name='generated_testcases'):
    """
    Saves the output DataFrame to the specified file format.

    Args:
        df (pd.DataFrame): DataFrame to save.
        file_format (str): File format ('csv', 'xlsx', 'json').
        file_name (str): Base file name without extension.

    Returns:
        str: Path to the saved file.
    """
    if file_format == 'csv':
        output_path = f"{file_name}.csv"
        df.to_csv(output_path, index=False)
    elif file_format == 'xlsx':
        output_path = f"{file_name}.xlsx"
        df.to_excel(output_path, index=False)
    elif file_format == 'json':
        output_path = f"{file_name}.json"
        df.to_json(output_path, orient='records', lines=True)
    else:
        raise ValueError("Unsupported file format. Choose 'csv', 'xlsx', or 'json'.")

    return output_path

# Example usage
if __name__ == "__main__":
    test_cases = [
        {
            "test_case_name": "Validate Employee ID Mapping",
            "test_case_description": "Ensure employee_id maps directly from eid in staging to warehouse.",
            "testcase_script": "SELECT eid, employee_id FROM staging.employee_in_table JOIN warehouse.employee ON eid = employee_id",
            "expected_result": "Values must match 1:1"
        }
    ]

    df = build_output(test_cases)
    print("Generated Output:")
    print(df)

    output_file = save_output(df, file_format='csv')
    print(f"Output saved to: {output_file}")
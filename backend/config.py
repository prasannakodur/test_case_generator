class Config:
    """
    Configuration class for setting up parameters for test case generation.
    """
    TEST_CASE_ID_PREFIX = "TC_"
    SOURCE_SCHEMA_NAME = "staging"
    TARGET_SCHEMA_NAME = "warehouse"

    @staticmethod
    def update_config(test_case_id_prefix=None, source_schema_name=None, target_schema_name=None):
        """
        Updates the configuration parameters.

        Args:
            test_case_id_prefix (str): Prefix for test case IDs.
            source_schema_name (str): Name of the source schema.
            target_schema_name (str): Name of the target schema.
        """
        if test_case_id_prefix:
            Config.TEST_CASE_ID_PREFIX = test_case_id_prefix
        if source_schema_name:
            Config.SOURCE_SCHEMA_NAME = source_schema_name
        if target_schema_name:
            Config.TARGET_SCHEMA_NAME = target_schema_name

# Example usage
if __name__ == "__main__":
    print("Default Config:")
    print(f"Test Case ID Prefix: {Config.TEST_CASE_ID_PREFIX}")
    print(f"Source Schema Name: {Config.SOURCE_SCHEMA_NAME}")
    print(f"Target Schema Name: {Config.TARGET_SCHEMA_NAME}")

    Config.update_config(test_case_id_prefix="TEST_", source_schema_name="src", target_schema_name="tgt")

    print("Updated Config:")
    print(f"Test Case ID Prefix: {Config.TEST_CASE_ID_PREFIX}")
    print(f"Source Schema Name: {Config.SOURCE_SCHEMA_NAME}")
    print(f"Target Schema Name: {Config.TARGET_SCHEMA_NAME}")
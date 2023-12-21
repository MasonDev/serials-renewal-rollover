import pandas as pd

def map_columns(df):
    # Mapping of old column names to new column names (adjusted for right to left mapping)
    column_mapping = {
        'Reporting Code Description - 2nd': 'RLOC',
        'PO Line Reference': 'RECORD #(ORDER)',
        'Title': '245',
        'Fund Ledger Code': 'FUND',
        'Reporting Code Description - 1st': 'FAC/SCHOOL',
        'Source Currency': 'FOR. CURR.',
        'Transaction Expenditure Amount': 'E PRICE',
        'Vendor Code': 'VENDOR',
        'PO Line Type Name': 'ORD TYPE',
    }

    # Verify that all columns in the mapping are present in the DataFrame
    missing_columns = [col for col in column_mapping.keys() if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Columns {missing_columns} are missing in the input DataFrame.")

    # Rename columns from right to left
    df.columns = [column_mapping.get(col, col) for col in df.columns]

    return df

def map_rloc_values(df):
    # Mapping for values in the "RLOC" column
    rloc_mapping = {
        'CF CML Bus & Phil (aan)': 'g',
        'CF CML History (bp)': 'g',
        'CF CML Literature (jm)': 'g',
        'HA CML (crb)': 'h',
        'LAW CML (ahn)': 'l',
        'LAW CML 2 (aan)': 'l',
        'MZ CML CJK (fs)': 'm',
        'MZ CML Pacific (jc)': 'm',
        'MZ CML S/SE Asia ME (ncw)': 'v',
    }

    # Map values in the "RLOC" column
    df['RLOC'] = df['RLOC'].map(rloc_mapping)

    return df

def transform_data(input_file, output_file):
    # Read Excel into DataFrame
    df = pd.read_excel(input_file)

    # Map columns
    df = map_columns(df)

    # Map values in the "RLOC" column
    df = map_rloc_values(df)

    # Filter columns to keep only those in the mapping
    column_mapping_values = ['RLOC', 'RECORD #(ORDER)', '245', 'FUND', 'FAC/SCHOOL', 'FOR. CURR.', 'E PRICE', 'VENDOR', 'ORD TYPE']
    df = df[column_mapping_values]

    # Save the processed DataFrame to a new Excel file
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    input_excel_file = './data/SRD Rollover/SRD rollover - standing orders.xlsx'
    output_excel_file = 'output_processed_file.xlsx'

    try:
        transform_data(input_excel_file, output_excel_file)
        print(f"Processing completed. Result saved to {output_excel_file}")
    except Exception as e:
        print(f"Error: {e}")

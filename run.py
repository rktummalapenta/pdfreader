import os
import pdfextract
import pandas as pd


def main():
    ROOT_DIR = os.path.abspath(os.curdir)
    file = os.path.join(ROOT_DIR,r'inputs.yml')
    data = pdfextract.load_yaml(file)
    ds = pd.DataFrame()

    for file in os.listdir(os.path.join(ROOT_DIR, data['input']['dir'])):

        print(os.path.join(ROOT_DIR, data['input']['dir'], file))
        input_data = os.path.join(ROOT_DIR, data['input']['dir'], file)
        pdf = pdfextract.extract_bill_amounts(input_data, data['pg_number'], data)
        df = pd.DataFrame(pdf)
        df['amount'] = df['amount'].str.replace('$','')
        df['amount'] = pd.to_numeric(df['amount'])
        period = pdfextract.extract_bill_period(input_data, data['pg_number'], data)
        df['period'] = period
        ds = pd.concat([ds, df])

    final = ds.groupby(['mobile']).sum()
    print(final)


if __name__ == "__main__":
    main()

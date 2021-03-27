import yaml
import pdfplumber


def load_yaml(file):

    with open(file) as f:
        inputs = yaml.safe_load(f)
    return inputs


def extract_bill_amounts(page, pg_number, data):

    with pdfplumber.open(page) as pdf:
        pdf = pdf.pages[pg_number]
        x0 = int(data['bill_crop']['x0'])
        top = float(data['bill_crop']['top']) * float(pdf.height)
        x1 = float(data['bill_crop']['x1']) * float(pdf.width)
        bottom = float(data['bill_crop']['bottom']) * float(pdf.height)
        pg = pdf.crop((x0,top,x1,bottom))
        text = pg.extract_text()
        words = text.split(' ')
        remove_words = data['remove_words']
        cleaned_list = [x for x in words if x not in remove_words]
        table = { 'mobile' : [], 'amount' : [] }

        for i in range(len(cleaned_list)):
            x = cleaned_list[i].split("\n")
            for i in range(len(x)):
                if i == 0:
                    table ['amount'].append(x[i])
                if i == 1:
                    table['mobile'].append(x[i])
        return table


def extract_bill_period(page, pg_number, data):

    with pdfplumber.open(page) as pdf:
        pdf = pdf.pages[pg_number]
        x0 = int(data['bill_period']['x0'])
        top = float(data['bill_period']['top']) * float(pdf.height)
        x1 = float(data['bill_period']['x1']) * float(pdf.width)
        bottom = float(data['bill_period']['bottom']) * float(pdf.height)
        pg = pdf.crop((x0,top,x1,bottom))
        return(pg.extract_text())




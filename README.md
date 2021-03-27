# pdfreader

A python utility which reads mobile bill pdfs and calculates aggregations of bill paid by each mobile from provided monthly statements.
Considered my verizon monthly bill statements to calculate total amounts paid by each mobile.

 - Leveraged pdfplumber python library to extract pdf for this use case.

 - PDF was cropped to read required information from each pdf statement.
 
 - Place all pdfs in data folder to process using this utlity or pass in put directory in inputs.yml
 
 - Bbox values will vary based on required information and these values should be passed to inputs.yml
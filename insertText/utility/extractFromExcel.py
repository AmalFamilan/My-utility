import pandas as pd 


def parsing_student_data_from_excel(path):
    df = pd.read_excel(path)
    student_records = df.to_dict(orient="records")
    return student_records
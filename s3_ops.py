import subprocess
import pandas as pd

df = pd.read_csv(r"D:\object_detection_collection\Worksheet_collection - Science.csv")

links = df['pdf link'].to_numpy()
wrk_sheet_names = df['Worksheet name'].to_numpy()
stds = df['standard'].to_numpy()

def correct_the_link(link):
    s3_full_link = link.split('?')
    s3 = s3_full_link[0].split('//')
    s3_link_to_replace = s3[1].split('/')
    replaced_s3_link = s3_link_to_replace[0].split('.')
    # replaced_s3_link = replaced_s3_link[0]
    s3_link = f"s3://{replaced_s3_link[0]}/{s3_link_to_replace[1]}/{s3_link_to_replace[2]}/{s3_link_to_replace[3]}/{s3_link_to_replace[4]}/{s3_link_to_replace[5]}/{s3_link_to_replace[6]}"
    return s3_link


count = 0
for link,std,name in zip(links,stds,wrk_sheet_names):
    count += 1
    s3_link = correct_the_link(link)
    pdfSaveFolder = f"D:/object_detection_collection/maths/TEY251 - {std} - {name} - {count}.pdf"
    result = subprocess.run(["aws", "s3", "cp", s3_link, pdfSaveFolder])
    if result.returncode == 1:
        s3_link = s3_link.replace("%28", "(")
        s3_link = s3_link.replace("%29", ")")
        pdfSaveFolder = f"D:/object_detection_collection/maths  /TEY251 - {std} - {name} - {count}.pdf"
        result = subprocess.run(["aws", "s3", "cp", s3_link, pdfSaveFolder])
    print(f"--{count}--")

# s3_link = "s3://prod-deepstream/smartail/worksheet/VII/Science/65042f8b8a12975049d278a0/dddc7adf-342c-4c5f-afd3-12fb7cb0b0f9_Copy_of_G7A_Science_Quarterly_15,06.2023.pdf"           
# pdfSaveFolder = "D:/object_detection_collection/science/TEY251 - 7 - G7A_SCIENCE_QUATERLY_ - 14.pdf"
# result = subprocess.run(["aws", "s3", "cp", s3_link, pdfSaveFolder])

# TEY251 - jaycees
# TIS132 - JSS Dharwad 
# UDH276 - SFS
# IUQ821 - KLE,kuvempu Nager
# OSY247 - KLE Society School, Rajajinagar
# QVM787 - KLE, NIPANI
# RYT766 - KLE Society’s School, Haveri
# MBE743 - KLE Society’s School, Saundatti
# LQV530 - KLE,Manjunathnagar
# DLX404 - KLE Society’s School, Gadag 
# AUA097 - KLE Society's School, Nagarbhavi
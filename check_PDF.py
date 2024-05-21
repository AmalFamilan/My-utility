import os 
path = r"E:\RESEARCH_DATAS\IGY950"

for wrk_sheet in os.listdir(path):
        wrk_sheet_path = os.path.join(path,wrk_sheet) 
        for in_wrk_sheet_path in os.listdir(wrk_sheet_path):
            pdf_path = os.path.join(wrk_sheet_path,in_wrk_sheet_path)
            if in_wrk_sheet_path == "PDF":
                print(wrk_sheet)
            
           

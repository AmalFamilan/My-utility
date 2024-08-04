import pandas as pd
import requests
import wget

def download_pdf_from_google_drive(gdrive_url, destination):
    file_id = gdrive_url.split("/")[-2]
    download_link = f"https://drive.google.com/uc?id={file_id}"
    wget.download(download_link)
    # response = requests.get(download_link)
    # if response.status_code == 200:
    #     with open(destination, "wb") as f:
    #         f.write(response.content)
    #     print(f"PDF downloaded from {gdrive_url} successfully.")
    # else:
    #     print(f"Failed to download PDF from {gdrive_url}.")

# Load Excel file with pandas
excel_file = r"D:\maps\maps.xlsx"  # Update with your Excel file path
df = pd.read_excel(excel_file)

# Assuming the column containing Google Drive links is named 'Links'
for index, row in df.iterrows():
    google_drive_link = row['PDF Link']  # Update 'Links' with your column name
    destination_path = f"D:/maps/pdf/downloaded_file_{index}.pdf"  # Unique filename for each PDF
    download_pdf_from_google_drive(google_drive_link, destination_path)

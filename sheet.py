import gspread
from oauth2client.service_account import ServiceAccountCredentials

def insert_in_sheet(ingr_list):
    print(ingr_list)
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("ingredients").sheet1

    ingredients = sheet.get_all_records()
    row_query = ', '.join(ingr_list)
    insert_row = [row_query]

    sheet.delete_row(2)
    sheet.insert_row(insert_row, 2)
    print(ingredients)

# insert_in_sheet(["lettuce", "tomato", "cheese"])

# import time
#
# import requests
#
# url = 'https://energy.tar-shop.space/thank-you.php'
#
# headers = {
#     # ':authority': 'energy.tar-shop.space',
#     # ':method': 'POST',
#     # ':path': '/thank-you.php',
#     # ':scheme': 'https',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-encoding': 'gzip, deflate, br, zstd',
#     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     'cache-control': 'no-cache',
#     'content-length': '123',
#     'content-type': 'application/x-www-form-urlencoded',
#     'cookie': 'PHPREFS=full; formIsSubmitted=true',
#     'origin': 'https://energy.tar-shop.space',
#     'pragma': 'no-cache',
#     'priority': 'u=0, i',
#     'referer': 'https://energy.tar-shop.space/',
#     'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
# }
#
# body = {
#     'name': 'Nastya',
#     'phone': '+380951257854',
# }
#
# print('1 start')
# result = requests.post(url=url, headers=headers, json=body)
# with open('result1.html', 'w', encoding='utf-8') as file:
#     file.write(result.text)
#     print('1 finish\n')
#
# time.sleep(10)
#
# body = {
#     'name': 'Костя',
#     'phone': '+380986068541',
# }
#
# print('2 start')
# result = requests.post(url=url, headers=headers, json=body)
# with open('result2.html', 'w', encoding='utf-8') as file:
#     file.write(result.text)
#     print('2 finish')

# ------------------------------------------------------------------------

# import os
# from googleapiclient.discovery import build
# from google.oauth2.service_account import Credentials
#
# service_account_file = 'service_account.json'
# scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
#
# creds = Credentials.from_service_account_file(service_account_file, scopes=scopes)
# service = build('sheets', 'v4', credentials=creds)
#
# spreadsheet_id = '1dUGNYqQEjEWM2KyakwW9dbc_IA6P_56xrMvqxSCponY'
# range_1 = 'Лист1!A1B1'
# range_2 = 'Лист2!A1B1'
#
# result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_1).execute()
# values = result.get('values', [])
#
# if not values:
#     print('No data found')
# else:
#     print('Name, Name:')
#     for row in values:
#         print(row[0] + ', ' + row[1])
#     with open('result.txt', 'w') as file:
#         file.write(values)

# ------------------------------------------------------------------------

# import gspread
# from google.oauth2.service_account import Credentials
#
# scope = ['https://www.spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']
# creds = Credentials.from_service_account_file('service_account.json', scopes=scope)
#
# gc = gspread.authorize(creds)
# sheet = gc.open_by_key('1dUGNYqQEjEWM2KyakwW9dbc_IA6P_56xrMvqxSCponY').sheet1
#
# data = sheet.get('A1:B1')
#
# for row in data:
#     print(row)
#
# with open('result.txt', 'w') as file:
#     file.write(data)

# ------------------------------------------------------------------------

# import os.path
#
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
#
# # If modifying these scopes, delete the file token.json.
# SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
#
# # The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = "1dUGNYqQEjEWM2KyakwW9dbc_IA6P_56xrMvqxSCponY"
# SAMPLE_RANGE_NAME = "Лист1!A1:B1"
#
#
# def main():
#   """Shows basic usage of the Sheets API.
#   Prints values from a sample spreadsheet.
#   """
#   creds = None
#   # The file token.json stores the user's access and refresh tokens, and is
#   # created automatically when the authorization flow completes for the first
#   # time.
#   if os.path.exists("secret_key.json"):
#     creds = Credentials.from_authorized_user_file("secret_key.json", SCOPES)
#   # If there are no (valid) credentials available, let the user log in.
#   if not creds or not creds.valid:
#     if creds and creds.expired and creds.refresh_token:
#       creds.refresh(Request())
#     else:
#       flow = InstalledAppFlow.from_client_secrets_file(
#           "credentials.json", SCOPES
#       )
#       creds = flow.run_local_server(port=0)
#     # Save the credentials for the next run
#     with open("token.json", "w") as token:
#       token.write(creds.to_json())
#
#   try:
#     service = build("sheets", "v4", credentials=creds)
#
#     # Call the Sheets API
#     sheet = service.spreadsheets()
#     result = (
#         sheet.values()
#         .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
#         .execute()
#     )
#     values = result.get("values", [])
#
#     if not values:
#       print("No data found.")
#       return
#
#     print("Name, Major:")
#     for row in values:
#       # Print columns A and E, which correspond to indices 0 and 4.
#       print(f"{row[0]}, {row[4]}")
#   except HttpError as err:
#     print(err)
#
#
# if __name__ == "__main__":
#   main()

# ------------------------------------------------------------------------

import gspread

gc = gspread.service_account(filename='service_account.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open("test").sheet1

# Update a range of cells using the top left corner address
wks.update([[1, 2], [3, 4]], 'A1')

# Or update a single cell
wks.update_acell('B42', "it's down there somewhere, let me take another look.")

# Format the header
wks.format('A1:B1', {'textFormat': {'bold': True}})








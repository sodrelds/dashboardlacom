import os.path
import pandas as pd
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1n7JDIlG-ZTpJW_E_8OHhgnnMzZrT8I2eHLezbJBrHPI"
SAMPLE_RANGE_NAME = "Instagram!B4:I12"


def instagram_data():
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists(r"C:\Users\sodre\OneDrive\Dashboard-LACOM\dashboard\api\token.json"):
    creds = Credentials.from_authorized_user_file(r"C:\Users\sodre\OneDrive\Dashboard-LACOM\dashboard\api\token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    valores = result['values']
    df = pd.DataFrame(valores)
    # Usando a primeira linha (índice 0) como cabeçalho das colunas
    df.columns = df.iloc[0]

    # Removendo a primeira linha após usá-la como cabeçalho
    df = df[1:]
    

  except HttpError as err:
    print(err)

  return(df)


SAMPLE_RANGE_NAME_LINKEDIN = "LinkedIn!B4:H16"

def linkedin_data():
  creds = None
   #The file token.json stores the user's access and refresh tokens, and is
   #created automatically when the authorization flow completes for the first
   #time.
  if os.path.exists(r"C:\Users\sodre\OneDrive\Dashboard-LACOM\dashboard\api\token.json"):
    creds = Credentials.from_authorized_user_file(r"C:\Users\sodre\OneDrive\Dashboard-LACOM\dashboard\api\token.json", SCOPES)
   #If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
     #Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME_LINKEDIN)
        .execute()
    )
    valores = result['values']
    df_linkedin = pd.DataFrame(valores)

    # Usando a primeira linha (índice 0) como cabeçalho das colunas
    df_linkedin.columns = df_linkedin.iloc[0]

    # Removendo a primeira linha após usá-la como cabeçalho
    df_linkedin = df_linkedin[1:]


  except HttpError as err:
    print(err)

  return(df_linkedin)

SAMPLE_RANGE_NAME_TIKTOK = "TikTok!B4:I12"

def tiktok_data():
  creds = None
   #The file token.json stores the user's access and refresh tokens, and is
   #created automatically when the authorization flow completes for the first
   #time.
  if os.path.exists(r"C:\Users\sodre\OneDrive\Dashboard-LACOM\dashboard\api\token.json"):
    creds = Credentials.from_authorized_user_file(r"C:\Users\sodre\OneDrive\Dashboard-LACOM\dashboard\api\token.json", SCOPES)
   #If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
     #Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME_TIKTOK)
        .execute()
    )
    valores = result['values']
    df_tiktok = pd.DataFrame(valores)

    # Usando a primeira linha (índice 0) como cabeçalho das colunas
    df_tiktok.columns = df_tiktok.iloc[0]

    # Removendo a primeira linha após usá-la como cabeçalho
    df_tiktok = df_tiktok[1:]


  except HttpError as err:
    print(err)

  return(df_tiktok)

SAMPLE_RANGE_NAME_YOUTUBE = "Youtube!B4:K16"

def youtube_data():
  creds = None
   #The file token.json stores the user's access and refresh tokens, and is
   #created automatically when the authorization flow completes for the first
   #time.
  if os.path.exists(r"C:\Users\sodre\OneDrive\Dashboard-LACOM\dashboard\api\token.json"):
    creds = Credentials.from_authorized_user_file(r"C:\Users\sodre\OneDrive\Dashboard-LACOM\dashboard\api\token.json", SCOPES)
   #If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
     #Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME_YOUTUBE)
        .execute()
    )
    valores = result['values']
    df_youtube = pd.DataFrame(valores)

    # Usando a primeira linha (índice 0) como cabeçalho das colunas
    df_youtube.columns = df_youtube.iloc[0]

    # Removendo a primeira linha após usá-la como cabeçalho
    df_youtube = df_youtube[1:]


  except HttpError as err:
    print(err)

  return(df_youtube)

if __name__ == "__main__":
  instagram_data()
  tiktok_data()
  linkedin_data()
  youtube_data()
# api handler
from nt import access

import requests
import sqlite3
import os
import datetime as dt
import TradeAlert.models as models
from TradeAlert.models import AccountInformation, AccessToken, LoginHTTPResponse, OAuthToken, Credentials
from TradeAlert.api.urls import Url


# this class has the following methods:

    # login() - logs in user
    # logout() - logout user
    # is_logged_in() - returns TRUE if connected




class ApiClient():

    def __init__(self, username:str, password:str, api_key:str):
        self.username   :str = username
        self.password   :str = password
        self.api_key    :str = api_key
        self.response  : models.LoginHTTPResponse
        self.oauth      : models.OAuthToken
        self.api_env    :str
        self.static_url :str
        self.authorisation :str
        self.login_time :dt.datetime
        self.login_expiry_datetime :dt.datetime

    def is_authenticated(self):
        
        if dt.datetime.now(dt.timezone.utc) > self.login_expiry_datetime:
            return False
        else:
            return True

    def refresh_session(self, credentials: Credentials, access_token: AccessToken, account_information: AccountInformation) -> AccessToken:
        url = f'{Url.SESSION}/refresh-token'
        data = { "refresh_token" : access_token.refresh_token }
        headers = {
            "Content-Type"  : "application/json; charset=UTF-8",
            "Accept"        : "application/json; charset=UTF-8",
            "X-IG-API-KEY"  : credentials.api_key,
            "Version"       : "1",
            "Authorization" : f'{access_token.token_type} {access_token.access_token}',
            "IG-ACCOUNT-ID" : account_information.account_id,
        }
        response :OAuthToken = requests.post(url,json=data, headers=headers).json()
        token = AccessToken(
            access_token    = response["access_token"],
            refresh_token   = response["refresh_token"],
            scope           = response["scope"],
            token_type      = response["token_type"],
            expires_in      = response["expires_in"]
        )
        return token
        
        
    def create_session(self, credentials: Credentials) -> tuple[AccountInformation, AccessToken]:
        data = {
            "identifier":   credentials.username,
            "password":     credentials.password,
        }
        headers = {
            "Content-Type"  : "application/json; charset=UTF-8",
            "Accept"        : "application/json; charset=UTF-8",
            "X-IG-API-KEY"  : credentials.api_key,
            "Version"       : "3",
               
        }

        response: LoginHTTPResponse = requests.post(str(Url.SESSION), json=data, headers=headers).json()
        account = AccountInformation(
            client_id = response["clientId"],
            account_id = response["accountId"],
            timezone_offset = response["timezoneOffset"],
            ls_endpoint = response["lightstreamerEndpoint"]
        )
        token = AccessToken(
            access_token = response["oauthToken"]["access_token"],
            refresh_token = response["oauthToken"]["refresh_token"],
            scope = response["oauthToken"]["scope"],
            token_type = response["oauthToken"]["token_type"],
            expires_in = response["oauthToken"]["token_type"]
        )
        return account, token
        
    def destroy_session(self, credentials: Credentials, access_token: AccessToken, account_information: AccountInformation) -> requests.Response:
        headers = {
            "Content-Type"  : "application/json; charset=UTF-8",
            "Accept"        : "application/json; charset=UTF-8",
            "X-IG-API-KEY"  : credentials.api_key,
            "Version"       : "1",
            "Authorization" : f'{access_token.token_type} {access_token.access_token}',
            "IG-ACCOUNT-ID" : account_information.account_id,
            "_method"       : "DELETE",
        }
        return requests.delete(str(Url.SESSION), headers=headers).json()




    
        



        
    # def db_connect(self, database_name:str="credentials"):
        # if not os.path.isfile(f'{os.getcwd()}/{database_name}.db'):
            # try:
                # connection = sqlite3.connect("credentials.db")
                # return connection
            # except:
                # raise Exception("Attempt to connect to database '{database_name}.db' in the working directory failed despite the file being findable.")
        # else:
            # raise Exception(f'{os.getcwd()}{database_name}.db was not found. No database connection attempt was made.')

    # def db_close(self, connection:sqlite3.Connection):
        # try:
            # connection.close()
        # except:
            # raise Exception("The request to close the database failed.")


#     def is_logged_in(self):
        # url=f'{self.static_url}/gateway/deal/accounts'

        # headers = {
            # "Content-Type"  : "application/json; charset=UTF-8",
            # "Accept"        : "application/json; charset=UTF-8",
            # "X-IG-API-KEY"  : self.api_key,
            # "Version"       : "1",
            # "Autorization"  : "",
            # "IG-ACCOUNT-ID" : "",
        # }


#     def load_user(self, username:str):
        # if not os.path.isfile(f'{os.getcwd()}/credentials.db'):
            # print(f'{os.getcwd()}/credentials.db does not exist') 
        # connection = sqlite3.connect("credentials.db")
        # cursor = connection.cursor()
        # db_response = cursor.execute(f'select * from users where username="{username}"').fetchone()
        # try:
            # if db_response[0] == username:
                # self.username   = db_response[0]
                # self.api_key    = db_response[1]
                # self.password   = db_response[2]
                # self.api_env    = db_response[3]
        # except:
            # raise Exception(f'The database returned an invalid user record. Requested user -> {username}. Returned user -> {db_response[0]}')
        # finally:
            # connection.close()

   #  def login(self, user:str):

        # #if self.load_user(user):
        # self.load_user(user)

        # if self.api_env == "":
            # print(f'Error connecting to database with username {self.username}. The credentials were fetched successfully but no api environment is declared. Does the database record contain the key environment?')
            # return
        # if self.api_env == "demo":
            # self.static_url = "https://demo-api.ig.com/" 
        # elif self.api_env == "prod":
            # self.static_url = "https://api.ig.com/"
        # else:
            # print(f'self.api_env incorrectly set. It should be either "prod" or "demo". Is it currently set to {self.api_env}')


        # headers = {
    
            # "Content-Type"  : "application/json; charset=UTF-8",
            # "Accept"        : "application/json; charset=UTF-8",
            # "X-IG-API-KEY"  : self.api_key,
            # "Version"       : "3",
        # }
        
        # data = {

            # "identifier"    : self.username,
            # "password"      : self.password
        # }
 
        # response = requests.post(f'{self.static_url}/gateway/deal/session', json=data, headers=headers)
        # self.response = response.json()
        # print(type(self.response))
        # print(self.response["oauthToken"]["access_token"])
        # print(self.response["oauthToken"]["access_token"])
        # #print(self.response)
        # values = (
            # self.username,
            # self.response["clientId"],
            # self.response["accountId"],
            # self.response["timezoneOffset"],
            # self.response["lightstreamerEndpoint"],
            # self.response["oauthToken"]["access_token"],
            # self.response["oauthToken"]["refresh_token"],
            # self.response["oauthToken"]["scope"],
            # self.response["oauthToken"]["token_type"],
            # self.response["oauthToken"]["expires_in"]
        # )
        # con = sqlite3.connect("credentials.db")
        # cur = con.cursor()

        # cur.execute(
            # """
            # INSERT OR REPLACE INTO apiSessions
            # (username, clientId, accountId, timezoneOffset, lightstreamerEndpoint, accessToken, refreshToken, scope, tokenType, expiresIn)
            # VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            # """,
            # values,
        # )
        # con.commit()
        # con.close()
        # return 0
 

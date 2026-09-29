from TradeAlert.api.client import ApiClient
from TradeAlert.models import AccountInformation, AccessToken, Credentials

class ApiUser():
    def __init__(self, client:ApiClient):

        self.client                 :ApiClient = client
        self.account_information    :AccountInformation
        self.access_token           :AccessToken
        self.credentials            :Credentials
        
    def login(self, username: str, password: str, api_key: str):
            self.credentials.api_key = api_key
            self.credentials.username = username
            self.credentials.password = password
            account, token = self.client.create_session(
                self.credentials
            )

            self.account_information = account
            self.access_token = token
    
    def refresh_session(self):
        token = self.client.refresh_session(
            self.credentials,
            self.access_token,
            self.account_information
        )
        self.access_token = token
        

        

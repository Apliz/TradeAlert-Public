from typing import TypedDict
from dataclasses import dataclass

class OAuthToken(TypedDict):
    access_token:str
    refresh_token:str
    scope:str
    token_type:str
    expires_in:str

class LoginHTTPResponse(TypedDict):
    clientId:str
    accountId:str
    timezoneOffset:str
    lightstreamerEndpoint:str
    oauthToken:OAuthToken

@dataclass
class AccountInformation():
    client_id   :str
    account_id  :str
    timezone_offset :str
    ls_endpoint     :str

@dataclass
class AccessToken():
    access_token    :str
    refresh_token   :str
    scope           :str
    token_type      :str
    expires_in      :str

@dataclass
class Credentials():
    username        :str
    password        :str
    api_key         :str

    

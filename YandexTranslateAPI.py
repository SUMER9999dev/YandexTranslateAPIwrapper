#    todo app, that app just write tasks to json.
#    Copyright (C) 2020  SUMER
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import requests
from getch import pause
from os import system
system("title "+"TODO")
def Translate(APIkey, FirstLang, SecondLang, Text):
    requestURL = f"https://translate.yandex.net/api/v1.5/tr.json/translate?key={APIkey}&text={Text}&lang={FirstLang}-{SecondLang}"
    res = requests.get(requestURL).json()
    if res['code'] == 401:
        return "Error 401: Key invalid."  
    elif res['code'] == 402:
        return "Error 402: Key blocked."
    elif res['code'] == 404:
        return "Error 404: Limit reached."
    elif res['code'] == 413:
        return "Error 413: Text limit reached."
    elif res['code'] == 422:
        return "Error 422: Failed to translate text."
    elif res['code'] == 501:
        return "Error 501: The specified translation direction is not supported."
    else:
        try:
            return res['text'][0]
        except KeyError:
            return "KeyError. Maybe you type invalid lang code."
def GetLang(APIkey, Text):
    requestURL = f"https://translate.yandex.net/api/v1.5/tr.json/detect?key={APIkey}&text={Text}"
    res = requests.get(requestURL).json()
    if res['code'] == 401:
        return "Error 401: Key invalid."
    elif res['code'] == 402:
        return "Error 402: Key blocked."
    elif res['code'] == 404:
        return "Error 404: Limit reached."
    else:
        return res['lang']
apikey = "Your api key here"
print("Yandex translate wrapper by SUMER (https://tech.yandex.com/translate/doc/dg/concepts/about-docpage/)")
answer = input("You want detect language auto? Y/N: ")
if answer == "N":
    FirstLang = input("Type first lang code: ")
    SecondLang = input("Type second lang code: ")
    Text = input("Type text: ")
    result = Translate(apikey, FirstLang, SecondLang, Text)
    print("Result: " + result)
elif answer == "Y":
    SecondLang = input("Enter the code of the language you want to translate to: ")
    Text = input("Type text: ")
    FirstLang = GetLang(apikey, Text)
    result = Translate(apikey, FirstLang, SecondLang, Text)
    print("Result: " + result)
else:
    print("You type invalid answer.")
pause("Press any key to exit...")
#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, requests
from typing import Optional
import os
from time import sleep

def get_data() -> Optional[dict]:
    url = "https://api.chucknorris.io/jokes/random"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return json.loads(response.content)
        
    else:
        print(f"Failed to get data from API, error: {response.status_code}")
        return False

def main():
    number_of_jokes = int(os.getenv("JOKES", 1))

    # Limit maximum jokes to 5.
    if number_of_jokes > 5:
        number_of_jokes = 5
    for n in range(number_of_jokes):
        jokes_data = get_data()
        
        if jokes_data:
            joke = jokes_data.get("value") 
            print(f"\n{joke}\n")
            
            if (number_of_jokes > 1):
                sleep(1)

if __name__ == "__main__":
    main()

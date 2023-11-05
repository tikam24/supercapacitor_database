# -*- coding: utf-8 -*-
"""
contains functions to download abstracts by using EID list in text files.

"""

import requests
import json
import logging
import pandas as pd
import openpyxl



def abstract_scraper(text_file, MY_API_KEY, serial_number):

    df = pd.DataFrame(columns =['EID', 'Title', 'Journal', 'DOI'])
    
    with open(text_file, "r") as f:
        # Skip the first line of the file which contains the header
        f.readline()
                                
        # Loop over each line in the file to get the EIDs and fetch the abstracts
        for line in f:
                        
            eid = line.strip().split()[1]
            print(eid)
            
            resp = requests.get(f"https://api.elsevier.com/content/abstract/eid/{eid}",
                                headers={'Accept':'application/json',
                                        'X-ELS-APIKey': MY_API_KEY})
            
            # Parsing the response to get the abstract and print it
            response_json = resp.json()
            try:
                abstract = response_json['abstracts-retrieval-response']['coredata']['dc:description']                         

                with open(f"abstract/{eid}.txt", "w", encoding="utf-8") as abstract_file:
                    abstract_file.write(abstract)
            
                print(f"Abstract for EID {eid} saved to abstract_{serial_number}.txt")
                print("="*80)
                
            except Exception as e:
                logging.exception(f"Error occurred: {str(e)}")
                print("Error occurred:", str(e))
                break

            try:
                df.loc[serial_number, ['EID']] = eid
            except KeyError:
                df.loc[serial_number, ['EID']] = None                

            try:
                title = response_json['abstracts-retrieval-response']['coredata']['dc:title']
                df.loc[serial_number, ['Title']] = title
            except KeyError:
                df.loc[serial_number, ['Title']] = None                

            try:
                journal = response_json['abstracts-retrieval-response']['coredata']['prism:publicationName']
                df.loc[serial_number, ['Journal']] = journal
            except KeyError:
                df.loc[serial_number, ['Journal']] = None
                

            try:
                dois = response_json['abstracts-retrieval-response']['coredata']['prism:doi']
                df.loc[serial_number, ['DOI']] = dois
            except KeyError:
                df.loc[serial_number, ['DOI']] = None
                

            serial_number += 1
            f.readable()
        
        
        li = f.read()

                   
    return df, serial_number, li







        
 

# webscraping_codes

The web scraping code used for generating supercapacitor database consists of 3 steps namely abstract scraping, property parsingand CEM (Chemical Entity Mentioned) identification and finally some datacleaning. Descreption and structure of execution of each steps in the package and modules inside are explaind below:

1. The abstract scraping step consists of scraping published papers from the SCOPUS database using API with a querry word "supercapacitor". This steps first generate a text file containing list of EIDs of articles present in SCOPUS database with the above query. Secondly the abstracts of the articles having the EIDs in the list are downloaded and stored in a abstaract folder. Along with that a metadata excel sheet is also generated containing details of the research articles like Title, Journal and DOI.

2. Now the property parsing is performent on the downloaded abstract text file using specially designed Regular Expression rules. Seven important property & performance parameters of supercapacitor have been extracted namely Specific Capacitance, Surface Area, Energy Density, Power Density, Voltage, Current density and Number of cycles.

3. To find out the anode, cathode and electrolyte reported in the abstract BatteryBERT Language Model has been used along with ChemDataExtractor (CDE) Python Packge.

Finally Data Cleaning and Agumentation step has been performed using Pandas, ast and CDE python Packages.
 

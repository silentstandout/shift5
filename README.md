# shift5
TITLE: shift5 Analyst Assessment Repo

DESC: This repo contains scripts and other files created by and used by F. Bland in his Shift5 Analyst Assessment, in preparation for presentation.


------------------------------------- Assessment Prompt -------------------------------------

DATA: The dataset can be found here -> https://www.adsbexchange.com/products/historical-data/  
[data retrieved by f. bland at approx. 2024-07-04 1330z]

USE CASES:  
  1) Can we create classifications of flights for future analysis? What are key features of a classification?  
  2) How do flights differ?  
  3) <br> 

TASKS:<br> 
  1) Explore the data.  
  2) Determine the formal scope of a use case given the request is not explicit.  
  3) Determine what data should be used.  
  4) Develop a presentation of findings.

AREAS OF FOCUS:  
  - Ability to learn unknown data  
  - Transform, QA, and limit the data to the needs of the use case and future analysis  
  - Language Proficiency-
    - SQL  
    - Python  
    - R   
    - Data Viz  
    - Others  
  - Analysis proficiency that supports the use case and highlights the depth of your skillset
  - Writing and presentation proficiency of the results that highlights the depth of your skillset.
      
  
TECHNICAL REVIEW EXPECTATIONS:  
  - Presentation: 30 minutes
  - Presentation Questions: 15 minutes
  - General Interview Questions: 15 minutes  

  Exploration Process -  
    - What data was used?  
    - What technology was leveraged? Why?  
    - What factors determined final use case?  

  Analysis Process -  
    - What methodologies were used? Why?  
    - What are the findings and how are the valuable to the use case?  

  Deliverable -  
    - Is the analysis more research-focused and warranting a white-paper format?  
    - Is the audience an end-user, which an interactive dashboard is appropriate?  
    - Some of both?  

---------------------------------------------------------------------------------------------


DATA USED:  
  - readsb-hist for 2024-06-01  
  - ACAS for 2024-06-01  
  - Trace Files for 2024-06-01 00  
  - HiRes Trace Files for 2024-06-01 00  
  - Why?:  
    - Latest date = freshest data (if field names etc changed at all between 2016 and now).  
    - Limited to only 00 for trace and hires trace files due to breadth of directories and time/resource limitations for task.  

TECHNOLOGY LEVERAGED:  
  - Mac OS (OS on my personal machine)  
  - Python (determined as best option for batch downloading, cleaning/reformatting/aggregating, initial exploration, etc. for gzipped json data of this volume)
    - requests
    - gzip
    - json  
    - os  
    - csv  
    - defaultdict  
    - pandas  
    - sqlite3  
  - Google Sheets  
  - Microsoft Power BI

LANGUAGES LEVERAGED:
  - SQL
  - Python
  - M
  - DAX

FACTORS TO DETERMINE FINAL USE CASE:

METHODOLOGIES USED:

FINDINGS:

DELIVERABLES:  
  - White Paper + PowerPoint + Data Viz Report (interactive optional. live dashboard not needed without data flow and/or closer to realtime data.
  



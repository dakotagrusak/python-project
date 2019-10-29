# Python-Project

I need a way to save jobs that I like or am excited about and analyse the important parts.

I NEED TO CROSS REF THEM WITH A COLLECTION OF JOB DESCRIPTIONS THAT I LIKE. THIS YIELDS THINGS I LIKE AND THE SKILLS, TOPICS AND SENTIMENT THAT COMPANIES AND TEAMS ARE CURRENTLY LOOKING FOR.


## FIRST FLOW CHART IDEAS

JOB POSTS --> {JOB DESCRIPTION | SKILLS} --> SCAPE/PARSE --> FILTER --> SENTIMENT ANALYSIS


## PROJECT SUB-SECTIONS:

1. UPLOAD / SCRAPE DATA FROM JOBS
2. FILTER THE DATA FOR PROCESSING
3. DERIVE LIKES AND SKILLS / SENTIMENT

#----------------------------------------------------------------------------------------


Job Sources
    - AngelList
    - hanckernews jobs
    - stackoverflow jobs
    - indeed
    - linkedin
    - glassdoor



To collect the data:
    - query an API
        - Indeed (must sign up as a developer)
        -
    - scape web pages
        - AngelList ***
        - BuiltInAustin
        - StackOverflow

Let's begin with AngelList. We want to collect job information from job postings in Texas. We want to exclude Dallas and maybe Austin later. The focus is on Houston and San Antonio. What do we do about smaller cities and suburbs like Katy, Bellaire which are their own entities? Is filtering by DistanceFrom sufficient?

Using scapy seems the most logic library to use.

Beautiful soup could also be used. But let's stop for a moment and think about the goal for this project. I already know some basic keywords and interests that I'm fairly confident with.






## USEFULL LINKS AND RESOURCES
https://medium.com/towards-artificial-intelligence/text-mining-in-python-steps-and-examples-78b3f8fd913b

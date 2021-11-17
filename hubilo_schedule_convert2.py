import pandas as pd
import difflib
import numpy as np


"""
{
    "name": "Yevonnael Andrew",
    "email": "yevonnael.andrew@gmail.com",
    "avatar": "https://secure.gravatar.com/avatar/9475b1797be7252a6a0a79ac018bce51?s=500",
    "location": "Unknown",
    "bio": "Hi everyone! My name is Yevonnael Andrew, from Indonesia!  I currently finishing my study at Master's in ML & AI at Liverpool JMU, UK. Currently, I am doing my internship at UNDP in Indonesia as Data Analyst, I am also a Digital and Data bureau at one of the Indonesian political parties. I have multiple teaching experiences, for example, DTS Kominfo (training on Ministry of ICT Indonesia), Bootcamp by DQLab, teaching on local universities, etc. I also delivered a talk at Pycon Indonesia last year on a similar topic.",
    "twitter": "",
    "url": "https://www.linkedin.com/in/yevonnael-andrew-3351b9a7/",
    "organization": "UNDP",
    "shirt_size": "Men's XL",
    "talk_format": "Workshop (> 60 minutes)",
    "title": "Stock Portfolio Optimization for Beginner Investors using Python",
    "abstract": "Are you an investor? If yes, then this talk is for you! Here I will demonstrate the basic theory and Python skills you need to design and evaluate the most optimal investment portfolio, which has low risk and maximum return according to your investment objectives.",
    "description": "All investors, from large investors to the smallest individual investors, have a common problem with investing: how to decide where to invest, how much amount to invest, and how much risk to take? There are so many early investors when investing, do not use the required analytical techniques, this is due to the lack of sufficient fundamentals. In this tutorial, I'll cover the minimum theory you'll need as well as the Python skills you'll need to do portfolio analysis. So that after this session, you can immediately start your own portfolio analysis so that your investment level will be more optimal.\n\nI won't go into much of the math formulas, as Python will do it, but I'll give a conceptual one with relevant examples. I will give a stock optimization method, namely the Markowitz model, where this model is essentially looking for a combination of stocks that has the highest ratio of returns and the lowest volatility.\n\nIn this demonstration, I will conduct an investment simulation of stocks in a portfolio. The results of this simulation will be compared to an unoptimized portfolio (distribute the funds equal to 1/n to n types of shares). From the simulation results, we can see that with just a simple optimization using Python, we can produce a more optimal portfolio.",
    "notes": "I'm going to do a demonstration using Jupyter Notebook. There are no special requirements. I have arranged the material so that it is general and can be understood by the wider community. The presentation material is in the form of ppt and I will provide a notebook so that participants can follow along while I do the presentation. I currently finishing my study at Master's in ML & AI at Liverpool JMU, UK. Currently, I am doing my internship at UNDP in Indonesia as Data Analyst, I am also a Digital and Data bureau at one of the Indonesian political parties. I have multiple teaching experiences, for example, DTS Kominfo (training on Ministry of ICT Indonesia), Bootcamp by DQLab, teaching on local universities, etc. I also delivered a talk at Pycon Indonesia last year on a similar topic.",
    "audience_level": "Intermediate",
    "tags": [
      "data science",
      "finance",
      "investing",
      "Python",
      "Fintech",
      "Machine Learing"
    ],
    "rating": 56,
    "state": "accepted",
    "confirmed": "TRUE",
    "created_at": "July 31, 2021 09:56 UTC",
    "date": "2021-11-02",
    "start_time": "11:00",
    "end_time": "11:30"
  }
"""


# Import live schedule
live = pd.read_excel("Live Sessions - Speakers and emcees.xlsx", skiprows=1, sheet_name=0)
live[["start_time", "end_time"]] = live['Date and Time (ICT)'].str.split("-", expand=True)
live[["date", "start_time"]] = live['start_time'].str.split("2021", expand=True)
live['date'] = live['date'] + "2021"
live['start_time'] = pd.to_datetime(live["date"] + " " + live['start_time'])
live['end_time'] = pd.to_datetime(live["date"] + " " + live['end_time'])
live['date'] = pd.to_datetime(live['date'])

# Import habilo export
talks = pd.read_excel("Session export from Hubilo.xlsx", skiprows=3, sheet_name="Session Data").iloc[1:]
tracks = pd.read_excel("Session export from Hubilo.xlsx", header=0, sheet_name="Track(Read Only)")
speakers = pd.read_excel("Session export from Hubilo.xlsx", header=0, sheet_name="Speaker(Read Only)")


talks['date'] = pd.to_datetime(talks["Date (Req.)"])
talks = talks.merge(tracks, left_on="Track", right_on="Track ID", suffixes=('_x', ''))

# TODO. need to expand out the speakers and then join and then groupby talk again.

talks = talks.rename(columns={'Title (Req.)': "title",
                              'Start Time (Req.)': 'start_time', 
                              'End Time (Req.)': 'end_time', 
                              'Description': 'description', 
                              'Speaker Name': 'name', 
                              'Track Name': 'location'})
talks['start_date'] = pd.to_datetime(talks['Date (Req.)'] + " " + talks['start_time'])
talks['end_date'] = pd.to_datetime(talks['Date (Req.)'] + " " + talks['end_time'])

talks = talks.drop(columns=["Speakers", "Track", 'Session ID (Read only)'])

# get rid of test data
talks = talks[talks['date'] > "2021-11-18"]



# Match up Q&A with 
talks[["speaker_pronoun", "short_title"]] = talks['title'].str.split("\) - ", 1, expand=True)
# Try a fuzzy match
talks['matched_title'] = talks["title"].map(lambda x: next(iter(difflib.get_close_matches(x, live['Topic'].dropna(), 1,)), None), na_action="ignore")
matched = talks.merge(live, left_on="matched_title", right_on="Topic", suffixes=("_old", "_qa"))
qa = matched[matched["Type of Live Session"] == 'Q&A']

# Now get mew start time
dur = (qa['end_date'] - qa['start_date'])
dur_min = dur / np.timedelta64(1,'m')
qa['sess_start'] = qa['start_time_qa'] - dur


# Convert to json web format
exportweb = qa[["title", "description"]]
exportweb['name'] = qa['Speaker/s']
exportweb['location'] = qa['Topic']
exportweb['date'] = qa['sess_start'].dt.date
exportweb['start_time'] = qa['sess_start'].dt.time
exportweb['end_time'] = qa['end_time_qa'].dt.time

def export_web(talks):
    # TODO: maybe sort by track so teh same tracks end up the in same location?
    talks = talks.sort_values(["date", "start_time", "location"])
    talks.to_json("theme/static/schedule.json", orient='records', indent=4, date_format="iso")

export_web(exportweb)
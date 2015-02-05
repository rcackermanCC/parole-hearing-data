import re, time, csv, datetime
import os, sys

def format_date(date):
  if int(date) <= 50:
    date = 2000 + int(date)
    return date
  elif int(date) > 50 and int(date) < 100:
    date = 1900 + int(date)
    return date
  else:
    return date

def no_names(x):
  if type(x) == list:
    return x[1:len(x)]

def security_level(in_list):
  security_levels = {"Adirondack Correctional Facility": "medium", "Albion Correctional Facility": "medium",
                     "Altona Correctional Facility": "medium", "Arthur Kill Correctional Facility": "medium",
                     "Attica Correctional Facility": "max/supermax/disciplinary", "Auburn Correctional Facility": "max",
                     "Bare Hill Correctional Facility": "medium", "Bayview Correctional Facility": "medium",
                     "Beacon Correctional Facility": "minimum", "Bedford Hills Correctional Facility": "max",
                     "Buffalo Correctional Facility": "minimum", "Butler Correctional Facility": "medium",
                     "Butler ASACTC": "", "Camp Gabriels": "minimum", "Camp Georgetown": "minimum",
                     "Chateaugay Correctional Facility": "medium/parole violators/ASACTC alcohol and substance abuse correctional treatment center",
                     "Clinton Correctional Facility": "max", "Collins Correctional Facility": "medium",
                     "Coxsackie Correctional Facility": "maximum", "Downstate Correctional Facility": "maximum/classification center",
                     "Eastern Correctional Facility": "maximum", "Edgecombe Correctional Facility": "minimum",
                     "Elmira Correctional Facility": "maximum", "Fishkill Correctional Facility": "medium",
                     "Five Points Correctional Facility": "maximum/disciplinary", "Franklin Correctional Facility": "medium",
                     "Gouverneur Correctional Facility": "medium", "Gowanda Correctional Facility": "medium/sex offender counseling program",
                     "Great Meadow Correctional Facility": "maximum", "Green Haven Correctional Facility": "maximum",
                     "Greene Correctional Facility": "medium", "Groveland Correctional Facility": "high-end security",
                     "Hale Creek ASACTC": "medium", "Hudson Correctional Facility": "medium",
                     "Lakeview Shock Incarceration Correctional Facility": "medium/shock", "Lincoln Correctional Facility": "minimum/work release",
                     "Livingston Correctional Facility": "medium", "Lyon Mountain Correctional Facility": "minimum ",
                     "Marcy Correctional Facility": "medium; co-located with Central NY Psychiatric Center and Mid-State Corr. Facility",
                     "Mid-Orange Correctional Facility": "", "Mid-State Correctional Facility": "medium with max solitary blocks",
                     "Mohawk Correctional Facility": "medium", "Monterey Shock Incarceration Correctional Facility": "minimum/shock",
                     "Moriah Shock Incarceration Correctional Facility": "minimum/shock/ASAT",
                     "Mt. McGregor Correctional Facility": "medium", "Ogdensburg Correctional Facility": "medium",
                     "Orleans Correctional Facility": "medium", "Otisville Correctional Facility": "medium",
                     "Queensboro Correctional Facility": "minimum", "Rochester Correctional Facility": "minimum",
                     "Shawangunk Correctional Facility": "maximum", "Sing Sing Correctional Facility": "maximum, supermax",
                     "Southport Correctional Facility": "supermax", "Sullivan Correctional Facility": "maximum",
                     "Taconic Correctional Facility": "medium", "Ulster Correctional Facility": "medium",
                     "Upstate Correctional Facility": "maximum, supermax", "Wallkill Correctional Facility": "medium",
                     "Washington Correctional Facility": "medium", "Watertown Correctional Facility": "medium",
                     "Wende Correctional Facility": "maximum", "Willard Drug Treatment Center": "drug treatment center",
                     "Woodbourne Correctional Facility": "medium", "Wyoming Correctional Facility": "medium"
                    }
  
  out_list = []
  return out_list
    
  

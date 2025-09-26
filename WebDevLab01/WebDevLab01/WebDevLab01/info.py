#CHANGE BELOW
import streamlit as st
from pathlib import Path
ROOT = Path(__file__).resolve().parent
IMG = ROOT / "Images"
profile_picture = str(IMG / "japan.png")
about_me = "I am Elijah Forrest, a 2nd year IE major from Collingswood, NJ"

#CHANGE BELOW (OPTIONAL)
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://logowik.com/content/uploads/Images/513_email.jpg"

#CHANGE BELOW
my_linkedin_url = "https://www.linkedin.com/in/elijah-forrest-680659323/details/featured/"
my_github_url = ""
my_email_address = "elijahforrest11@gmail.com"

education_data ={
    'Degree': 'Bachelor of Science in Industrial Engineering with Focus on Data Science & Analytics',
    'Institution': 'Georgia Institute of Technology',
    'Location': 'Atlanta, GA',
    'Graduation Date': '2028',
    'GPA': 'N/A'
}
course_data = {
    "code":["Math 1554", "PUBP 3042", "PHYS 2211", "PSYC 1101", "ENGL 1102", "CS 2316", "MATH 2550", "PSYC 3005", "APPH 1060", "CS 1301", "MATH 2603", "ISYE 2027", "PSYC 2220"],
    "names":["Linear Algebra", "Data Science for Public Policy", "Principles of Physics I", "Introduction to General Psychology", "English Composition II", "Data Manipulation for Science and Industry", "Introduction to Multivariable Calculus", "Mindfulness: Science and Practice", "Flourishing: Strategies for Well-being and Resilience", "Introduction to Computing", "Introduction to Discrete Mathematics", "Probability with Applications", "Industrial/Organizational Psychology"],
    "semester_taken":["1st", "1st", "1st", "1st", "2nd", "2nd", "2nd", "2nd", "2nd", "3rd", "3rd", "3rd", "3rd"],
    "skills":["Matrices and stuff", "What does data science even have to do with public policy?", "Why do industrial engineers need to learn physics?", "Learn about the billions of neurons in the brain!", "Engineers biggest nightmare", "Wasn't I supposed to take this after 1301? Oops", "Only Two credits but may as well be 50", "How to be zen 101", "Show up to class and get an A", "1301 then 2316? Nah", "All based off logic but nothing logically makes sense", "The main reason people drop IE", "How did we end up in this class?"],
    }
experience_data = {
    "Gymnastics and Cheerleading Academy": (["- Led activities for 20-30 campers and had fun during it",
                                                                          "- resolving staffing or schedule gaps to maintain safety, engagement, and efficiency.", "- Made my manager proud"], str(IMG / "camp.jpg")),
    "Host at Westmont Diner":(["- Was the friendly guy who kind of hated his job...",
                                                           "- Allowed hosts on weekends to go from two working at a time to one"],str(IMG / "host.jpg")),
    "Concert Venue Parking Director":(["- Only worked here to get free concert tickets"],str(IMG / "pavilion.jpg"))

}

projects_data = {
    "Climate-Wellbeing Correlation Analysis Project": "Still not sure why I took this class before 1301. But anyway. Cleaned and merged 21M+ NOAA climate records with CDC/Wikipedia wellbeing data using Python (pandas, BeautifulSoup), eliminating data inconsistencies and enabling correlation analysis across 77 countries.",
}

programming_data = {
    "Python": 90,
    "Java": 70,
}

#CHANGE BELOW (OPTIONAL)
programming_icons = {
    "Python": "🐍",
    "Java": "☕",
}
spoken_icons = {
    "English": "🇬🇧",
}

#CHANGE BELOW
spoken_data = {
    "English": "Fluent",
}
leadership_data = {
    "Green team club senior board": (["- Helped make decisions for the club every week"],str(IMG / "green_club.jpg")),

}
activity_data={
    "Homeless Shelter": ["- Restocked and Helped people pick out clothes, food and tools from a homeless shelter",]
}

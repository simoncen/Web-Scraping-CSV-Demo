from bs4 import BeautifulSoup
import requests
import time
import csv

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f"Filtering out {unfamiliar_skill}")

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    #print(html_text)

    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' or '1' or '2' or '3' or '4' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href'] # the link for the specific job

            if unfamiliar_skill not in skills:
                with open(f"posts/{index}.csv", 'w') as f:
                    # print(f"Company Name: {company_name.strip()}") # removing both the leading and the trailing space characters
                    # print(f"Required Skills: {skills.strip()}")
                    # print(f"More Info: {more_info}")
                    writer = csv.writer(f)

                    name = "Company Name: " + company_name.strip()
                    nameList = [name]
                    skill = "Required Skills: " + skills.strip()
                    skillsList = [skill]
                    info = "More Info: " + more_info
                    infoList = [info]

                    writer.writerow(nameList) # removing both the leading and the trailing space characters
                    writer.writerow(skillsList)
                    writer.writerow(infoList)
                print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        # have the program run every 10 minutes
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)

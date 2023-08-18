from bs4 import BeautifulSoup
import json

# logging.basicConfig(level=logging.INFO)  

overall = {"data":[
    {
      "testid": "1",
      "status": "success",
      "score": 0,
      "message": ""
    }
]
}

# Task that must be present in the assignment 
indexChecks ={"hometitle":0,
            "projecttitle":0,
            "educationtitle":0,
            "introduction":0,
            "profileImage":0,
            "profileImageCaption":0,
            "video":0,
            "contact-me-openInNewTab":0,
            "contact-me-linksWorking":0,
            "projects":0,
            "inlineCss":0,
            "internalCss":0,
            "externalCss":0,
            "education":0,
            "total_marks":0}


#distribution of marks
markdistributions ={
            "hometitle": 0.5,
            "projecttitle":0.5,
            "educationtitle":0.5,
            "introduction":1,
            "profileImage":0.5,
            "profileImageCaption":0.5,
            "video":1,
            "contact-me-openInNewTab":0.5,
            "contact-me-linksWorking":0.5,
            "projects":1,
            "inlineCss":0.5,
            "internalCss":0.5,
            "externalCss":0.5,
            "education":1
            }


# ------------------ Index Page ------------------------

html_doc = open("./public_html/index.html","r")
soup = BeautifulSoup(html_doc, 'html.parser')
try:
    title = soup.title.string
    if len(title)>1 :
        indexChecks["hometitle"] = markdistributions['hometitle']
except AttributeError:
    pass

try:
    intro = soup.find_all('p',id='desc')
    # if Same id used twice
    if len(intro)==1 and len(str(intro[0]))>150:
        indexChecks["introduction"] = markdistributions['introduction']
except AttributeError:
    pass

try:
    if (str(intro[0]).find('font-size')!=-1):
        indexChecks['inlineCss'] = markdistributions['inlineCss']
except IndexError:
    pass

# Image chech Title present and image file exists check
try:
    image =  soup.find_all('img',id='myimage')
    if len(image)>0:
        try:
            pathToImage = image[0]['src']
        except IndexError:
            pathToImage = 0
        indexChecks['profileImage'] = (markdistributions['profileImage'] if pathToImage else 0)

    if len(image[0]['title'])>0:
        indexChecks['profileImageCaption']= markdistributions['profileImageCaption']
except IndexError:
    pass


# Video  file exists check
try:
    video  =  soup.find_all('video',id='myvideo')
    if len(video)>0:
        try:
            pathToVideo = video[0]['src']
        except:
            pathToVideo = 0
        if(pathToVideo==0 and len(video[0].find_all('source'))>0):
            pathToVideo = video[0].find('source')['src']
        indexChecks['video'] = (markdistributions['video'] if pathToVideo else 0)
except AttributeError:
    pass
    
try:
    contactMe =  soup.find('div',id='contact-me')
    if len(soup.findAll('div',id='contact-me'))>1:
        pass
    else:
        socialLinks = contactMe.find_all('a')
        numberSocialLink = len(socialLinks)
        linkTargetExists = markdistributions['contact-me-openInNewTab']
        working = markdistributions['contact-me-linksWorking']
        
        for link in socialLinks:
            if not link.has_attr('target'):
                linkTargetExists = 0
                break
            if len(link['href'])==0:
                working = 0
                break

        indexChecks["contact-me-openInNewTab"] = linkTargetExists
        indexChecks["contact-me-linksWorking"] = working
except AttributeError:
    pass

# ------------------ projects Page ------------------------

html_doc = open("./public_html/projects.html","r")
soup = BeautifulSoup(html_doc, 'html.parser')
try:
    title = soup.title.string
    if len(title)>1 :
        indexChecks["projecttitle"] = markdistributions['projecttitle']
except AttributeError:
    pass

try:
    g_flag = 0
    projects = soup.find_all('div',id='projects')
    if len(projects)==0:
        g_flag = 1
        projects = soup.find_all('ol',id='projects')
    #checks if any external css file is linked
    if (soup.link is not None):
        indexChecks['externalCss'] = markdistributions['externalCss']

#Projects list with atleast 2 projects listed

    if g_flag==0 and len(projects)==1 and (projects[0].find('ul') is not None or projects[0].find('ol') is not None):
        projects_list = list()
        if projects[0].find('ul') is not None:
            projects_list = projects[0].find('ul')
        elif projects[0].find('ol') is not None:
            projects_list = projects[0].find('ol')

        if len(projects_list.find_all('li')) >= 2 :
            indexChecks['projects'] = markdistributions['projects']
    if g_flag==1 and len(projects)==1:
        if len(projects[0].find_all('li')) >= 2 :
            indexChecks['projects'] = markdistributions['projects']
except AttributeError:
    pass


# ------------------ education Page ------------------------

html_doc = open("./public_html/education.html","r")
soup = BeautifulSoup(html_doc, 'html.parser')

try:
    title = soup.title.string
    if len(title)>1 :
        indexChecks["educationtitle"] = markdistributions['educationtitle']
except AttributeError:
    pass

#checks if internal css is defined
try:
    if (soup.style is not None):
        indexChecks['internalCss'] = markdistributions['internalCss']
except AttributeError:
    pass

try:
    edu_table = soup.find_all('table',id='education')
    print()
    #education has a table with a header and a body
    if len(edu_table)==1 and len(edu_table[0].find_all('tr'))>1 :
        indexChecks['education'] = markdistributions['education']
except AttributeError:
    pass

total_marks = 0
for k in indexChecks:
    total_marks = total_marks + indexChecks[k]

indexChecks['total_marks'] = total_marks
overall['data'][0]["score"] = total_marks
overall['data'][0]["message"] = indexChecks
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
    json.dump(overall,f,indent=4)

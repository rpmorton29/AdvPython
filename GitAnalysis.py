import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def readCSV():

    countries =['andorra', 'united arab emirates', 'afghanistan', 'antigua and barbudaanguilla', 'albania', 'armenia', 'angola', 'argentina', 'american samoaaustria', 'australia', 'aruba', 'aland islands', 'azerbaijanbosnia and herzegovina', 'barbados', 'bangladesh', 'belgium', 'burkina fasobulgaria', 'bahrain', 'burundi', 'benin', 'saint barthelemy', 'bermudabrunei', 'bolivia', 'bonaire, saint eustatius and saba', 'brazil', 'bahamasbhutan', 'botswana', 'belarus', 'belize', 'canada', 'cocos islandsdemocratic republic of the congo', 'central african republicrepublic of the congo', 'switzerland', 'ivory coast', 'cook islandschile', 'cameroon', 'china', 'colombia', 'costa rica', 'cuba', 'cape verdecuracao', 'christmas island', 'cyprus', 'czech republic', 'germanydjibouti', 'denmark', 'dominica', 'dominican republic', 'algeria', 'ecuadorestonia', 'egypt', 'western sahara', 'eritrea', 'spain', 'ethiopia', 'finlandfiji', 'falkland islands', 'micronesia', 'faroe islands', 'france', 'gabonunited kingdom', 'grenada', 'georgia', 'french guiana', 'guernsey', 'ghanagibraltar', 'greenland', 'gambia', 'guinea', 'guadeloupeequatorial guinea', 'greecesouth georgia and the south sandwich islands', 'guatemala', 'guamguinea-bissau', 'guyana', 'hong kong', 'honduras', 'croatia', 'haitihungary', 'indonesia', 'ireland', 'israel', 'isle of man', 'india', 'iraqiran', 'iceland', 'italy', 'jersey', 'jamaica', 'jordan', 'japan', 'kenyakyrgyzstan', 'cambodia', 'kiribati', 'comoros', 'saint kitts and nevisnorth korea', 'south korea', 'kuwait', 'cayman islands', 'kazakhstan', 'laoslebanon', 'saint lucia', 'liechtenstein', 'sri lanka', 'liberia', 'lesotholithuania', 'luxembourg', 'latvia', 'libya', 'morocco', 'monaco', 'moldovamontenegro', 'saint martin', 'madagascar', 'marshall islands', 'macedoniamali', 'myanmar', 'mongolia', 'macao', 'northern mariana islandsmartinique', 'mauritania', 'montserrat', 'malta', 'mauritius', 'maldivesmalawi', 'mexico', 'malaysia', 'mozambique', 'namibia', 'new caledonianiger', 'norfolk island', 'nigeria', 'nicaragua', 'netherlands', 'norwaynepal', 'nauru', 'niue', 'new zealand', 'oman', 'panama', 'perufrench polynesia', 'papua new guinea', 'philippines', 'pakistan', 'polandsaint pierre and miquelon', 'pitcairn', 'puerto ricopalestinian territory', 'portugal', 'palau', 'paraguay', 'qatar', 'reunionromania', 'serbia', 'russia', 'rwanda', 'saudi arabia', 'solomon islandsseychelles', 'sudan', 'sweden', 'singapore', 'saint helena', 'sloveniasvalbard and jan mayen', 'slovakia', 'sierra leone', 'san marino', 'senegalsomalia', 'suriname', 'south sudan', 'sao tome and principe', 'el salvadorsint maarten', 'syria', 'swaziland', 'turks and caicos islands', 'chadfrench southern territories', 'togo', 'thailand', 'tajikistan', 'east timorturkmenistan', 'tunisia', 'tonga', 'turkey', 'trinidad and tobago', 'tuvalutaiwan', 'tanzania', 'ukraine', 'uganda', 'united states', 'uruguayuzbekistan', 'vatican', 'saint vincent and the grenadines', 'venezuelabritish virgin islands', 'u.s. virgin islands', 'vietnam', 'vanuatuwallis and futuna', 'samoa', 'kosovo', 'yemen', 'mayotte', 'south africazambia', 'zimbabwe']
    df = pd.read_csv(r"world-cities_csv.csv", usecols=['name', 'country'])

    dfs = []
    for i in range(0,8):
        filename = "github_timeline_data00000000000"+str(i)+".csv"
        dfs.append(pd.read_csv(filename,low_memory=False, usecols = ['repository_url', 'repository_has_downloads','url', 'repository_created_at','repository_has_issues','repository_description','repository_forks','repository_fork','repository_has_wiki','repository_size','repository_name','repository_owner','repository_watchers','repository_language','repository_organization','actor_attributes_login','actor_attributes_name','actor_attributes_location','created_at','type']))

    gitdata = pd.concat(dfs, axis=0, ignore_index=True)
    
    return gitdata

def toptenlang(gitdata):
    languages = gitdata['repository_language'].value_counts()
    languages=languages.nlargest(10)

    languages.plot.bar(x='repository_language', y='repository_watchers')
    plt.xlabel('Languages')
    plt.ylabel('Frequency')
    plt.title('Top Ten Languages')
    plt.show()

def toplocation(gitdata):#todo store top langs and graph 3d
    all = gitdata[gitdata['actor_attributes_login'].isin(gitdata['repository_owner'])]
    all = all[['actor_attributes_location','actor_attributes_login']].groupby('actor_attributes_location').agg('count')
    all = all.nlargest(10,'actor_attributes_login')

    lang = toptenlang(gitdata)
    print(all)
    print(lang)
    fig = plt.figure()
    #ax1=fig.add_subplot(111,projection='3d')
    ##ax1.bar(lang.index,all['actor_attributes_location'], lang['repository_language'], shade=True)
    #for index, row in all.iterrows():
     #  findtoplangs(index,gitdata)
   # plt.show()


def findtoplangs(location,gitdata):
    temp =[]
    temp.append(location)
    toplangs =  gitdata[gitdata['actor_attributes_location'].isin(temp)]
    toplangs = toplangs[['actor_attributes_location','actor_attributes_login','repository_language']].groupby('repository_language',as_index=False).agg('count')
    toplangs.plot.bar(x='repository_language', y='actor_attributes_location')
    print(toplangs['actor_attributes_location'])




def toprepo(gitdata):#2a

    repos = gitdata[['repository_url','repository_name','type','repository_watchers']]

    top = repos[['repository_name','repository_url']].groupby('repository_name',as_index=False).agg('count')
    top = top.nlargest(10,'repository_url')
    print(top)
    topwatchrepo(repos,top)

def topwatchrepo(repos,top):#2b
    watch = gitdata.loc[gitdata['type']!='WatchEvent']
    #repos['actorcount'] = np.nan
    watch = watch[['repository_name','type','repository_watchers']].groupby('repository_name',as_index=False).agg('count')
    watch = watch[watch['repository_name'].isin(top['repository_name'])]
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'g']

    watch.plot.scatter(x='type',y='repository_watchers', color=colors)
    plt.xlabel('Watchers')                 
    plt.ylabel('Contributors')             
    plt.title('Contributors Vs Watchers')
    plt.show()


def security(gitdata):#2c
    security = gitdata['repository_description'].str.lower()
    gitdata.update(security)

    security = gitdata[gitdata['repository_description'].str.contains("security")==True]
    dates= pd.to_datetime(security["repository_created_at"]).map(lambda x: x.year)
    gitdata['repository_created_at'].update(dates)
    security = gitdata[gitdata['repository_description'].str.contains("security")==True]
    security = security[["repository_created_at",'repository_description']].groupby('repository_created_at',as_index=False).agg('count')
    total = security['repository_description'].sum(axis=0)
    percent = security['repository_description'].div(total)*100
    security.update(percent)
    print("Percent of Repos related to security over the Years:")
    print(security.to_string(header=False,index=False))

def timeframe(gitdata): #3a
    window = gitdata[gitdata['repository_created_at'].str.contains("2012-")==True]
    window =window.copy(deep=True)
    dates= pd.to_datetime(gitdata["repository_created_at"]).map(lambda x: x.hour)
    window['repository_created_at'].update(dates)
    
    ax = window['repository_created_at'].plot.hist(bins=4, alpha=0.5)
    plt.xlabel('Time Blocks')
    plt.ylabel('Number of Repos')
    plt.title('Most Popular Times')
    plt.xticks([0,6,12,18,23])
    plt.show()
    eventtype(window)

def eventtype(window):#3b
    eventwin = window.groupby(['repository_created_at','type'],as_index=False).agg('count')
    eventwin=eventwin[['repository_created_at','type','url']]
    pt = eventwin.pivot(index='repository_created_at',columns='type',values='url')
    plt.xlabel('Time')
    plt.ylabel('Number of Repos')
    plt.title('Events during Timeframe')
    pt.plot.bar(stacked=True)
    plt.show()

def topCompany(gitdata): #extra credit
    companies = gitdata['repository_organization'].value_counts()
    companies = companies.nlargest(10)
    companies.plot.bar()
    plt.xlabel('Companies')
    plt.ylabel('Repos Owned')
    plt.title('Top Ten Companies')
    plt.show()


gitdata = readCSV()
toptenlang(gitdata)
toplocation(gitdata)    #not done
toprepo(gitdata)
topCompany(gitdata)
security(gitdata)
timeframe(gitdata)











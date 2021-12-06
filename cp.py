import streamlit as st

st.title("Math 10: Course Project")

st.markdown("Name: Sarah Yee")
st.markdown("UCI ID(s): 80797166")
st.write("Source: [DATASET LINK](https://www.nbastuffer.com/2020-2021-nba-player-stats/)")
st.write("[Course Project Github](https://github.com/syee12/Math-10-Course-Project)")

#My Strategy & Thought Process
st.subheader("My Strategy & Thought Process")
"Throughout this project, I will be exploring a list of topics and distinctives to learn more about the past 2020-2021 NBA Regular Season as well as its players. Each section of this project is categorized by its topic. Within each topic, there is a certain goal/distinctive that was meant to be achieved in order to know more about the NBA season and the top-performing players in the league. Specifically, the first few topics will be an attempt to learn more about each NBA team. The goal is to simply view each team and see who top players are, how team stats look (ie player stats combined), and which players stood out amongst their teammates."


#Cleaning & Introducing the Data
import pandas as pd
import numpy as np
rng = np.random.default_rng()
import altair as alt

st.subheader("Introducing the Data")

df = pd.read_csv("nba21season.csv")
df = df.replace(" ", np.nan)
columns = list(df.columns)
"Below is our dataset from nba.stuffer.com ([linked](https://www.nbastuffer.com/2020-2021-nba-player-stats/) above as well) corresponding to the 2020-2021 NBA Regular Season"
"The first column and last 3 columns included in the original dataset from the source are not typical statistics used for basketball analysis. Therefore, since the Rank, Versatility Index, and Offensive and Defensive Rating columns are not particularly relevant, these columns will not be included in our data study."
df = df.drop(columns = ['RANK', 'VI (Versatility Index)', 'ORTG (Offensive Rating)', 'DRTG (Defensive Rating)'])
st.dataframe(df)

st.markdown("""---""")
st.write("Source: [REFERENCE: Horizontal Line Mark](https://discuss.streamlit.io/t/horizontal-separator-line/11788/5)")

#Topic 1
st.subheader("Topic 1: Top Team Scorers")
"> **Goal**: The goal for this topic is to view the top scorers of the league and see who the top scorers are for each NBA team."


st.write("The following code and resulting number shows us how many NBA team there are within the league.")
st.code("""len(list(df["TEAM"].value_counts()))""")
a = len(list(df["TEAM"].value_counts()))
st.write(a)

"Here we are able to see how many players are on each respective team."
#st.code("""df["TEAM"].value_counts()""")
st.write(df["TEAM"].value_counts())

"Here are the players according to the respective team they play on"
df2 = df.sort_values("TEAM")
df2
"For example, here is the player roster from the Atlanta Team"
df_ATL = df2.head(18)
df_ATL
"Here are the ultimate top 50 scorers from the Regular Season"
df_ATL.sort_values("PPG (Points Per Game)",ascending = False)
df_ppg = df.sort_values("PPG (Points Per Game)",ascending = False)
df_pgg1 = df_ppg.head(50)
df_pgg1

#Code to sort top scorers on each team
team_ppg_list = []
player_PPG_list = []
STAT_top_ppg_list = []
for i in df.index:
    if df_ppg.iloc[i,1] not in team_ppg_list:
        team_ppg_list.append(df_ppg.iloc[i,1])
        player_PPG_list.append(df_ppg.iloc[i,0])
        STAT_top_ppg_list.append(df_ppg.iloc[i,17])
#player_PPG_list

"Here is a list of each team's top scorer"
d = {"Full Name": player_PPG_list, "TEAM": team_ppg_list, "PPG (Points Per Game)": STAT_top_ppg_list}
Point_Leaders_df = pd.DataFrame(d)
Point_Leaders_df

"**SLIDE TO SEE WHO THE TOP SCORERS ARE!**"
Z = st.select_slider('Select a NBA Team to see who was the team top scorer', options = Point_Leaders_df['TEAM'])
Point_Leaders_df[Point_Leaders_df["TEAM"] == Z]

"Through the following chart, we can also view this data through a bar graph to see who the top scorers were."
PPG_graph = alt.Chart(Point_Leaders_df).mark_bar().encode(
    x='Full Name:O',
    y='PPG (Points Per Game):Q',
    tooltip = ['Full Name', 'TEAM', 'PPG (Points Per Game)']
)
mean_line = alt.Chart(Point_Leaders_df).mark_rule(color='red').encode(
    y='mean(PPG (Points Per Game)):Q'
)

topic1_chart = (PPG_graph + mean_line).properties(height=400)
topic1_chart

st.write("Source: [REFERENCE: Bar Chart with Line at Mean](https://altair-viz.github.io/gallery/bar_chart_with_mean_line.html)")

">> **Conclusion**: From these sorted tables, we can see that Stephen Curry from the Golden State Warriors Team was the top scorer for the NBA, averaging 32.0 points per game over the regular season. We can also conclude that Bradley Beal, Damian Lillard, Joel Embiid, and Giannis Antetokounmpo were a part of the top 5 scorers for this season. By viewing the top 50 scorers of the season, we can also conclude that some teams had several high scoring players, such as Kyrie Irving and Kevin Durant from the Brooklyn Team. For this reason, we cannot assume that each team had an equal number of high scorers; therefore, we will dig into the Effective Shooting Percentage for Topic 2 in order to learn more about the teams."

st.markdown("""---""")


#Topic 2
st.subheader("Topic 2: Effective Shooting Teams")
"> **Goal**: The goal for this topic is to see who each team effectively shoots. We will try to sort out who the most effective shooting teams are in the league for the past season. To do so, first, we're going to try to sort the data depending on which team the player is from. From there, we will determine what the team's average effective shooting percentage was. To do this, we will take the mean from the players' stats."

"Below, is the Pandas Dataframe that displays each team's mean Effective Shooting Percentage."
import statistics
import math

Hou_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Hou':
        Hou_team.append(df2.iloc[i,15])
b1 = statistics.mean(Hou_team)

Orl_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Orl':
        Orl_team.append(df2.iloc[i,15])
b2 = statistics.mean(Orl_team)

Bro_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Bro':
        Bro_team.append(df2.iloc[i,15])
b3 = statistics.mean(Bro_team)


Cle_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Cle':
        Cle_team.append(df2.iloc[i,15])
b4 = statistics.mean(Cle_team)

Sac_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Sac':
        Sac_team.append(df2.iloc[i,15])
b5 = statistics.mean(Sac_team)

Phi_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Phi':
        Phi_team.append(df2.iloc[i,15])
b6 = statistics.mean(Phi_team)


Mil_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Mil':
        Mil_team.append(df2.iloc[i,15])
b7 = statistics.mean(Mil_team)

Chi_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Chi':
        Chi_team.append(df2.iloc[i,15])
b8 = statistics.mean(Chi_team)

Den_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Den':
        if type(df2.iloc[i,15]) == np.float64:
            Den_team.append(df2.iloc[i,15])
Den_team.pop()
b9 = statistics.mean(Den_team)

Okc_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Okc':
        Okc_team.append(df2.iloc[i,15])
b10 = statistics.mean(Okc_team)

Tor_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Tor':
        Tor_team.append(df2.iloc[i,15])
b11 = statistics.mean(Tor_team)

Det_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Det':
        Det_team.append(df2.iloc[i,15])
b12 = statistics.mean(Det_team)

Was_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Was':
        Was_team.append(df2.iloc[i,15])
b13 = statistics.mean(Was_team)

Nor_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Nor':
        Nor_team.append(df2.iloc[i,15])
b14 = statistics.mean(Nor_team)

Bos_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Bos':
        Bos_team.append(df2.iloc[i,15])
b15 = statistics.mean(Bos_team)

Mia_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Mia':
        Mia_team.append(df2.iloc[i,15])
b16 = statistics.mean(Mia_team)

Ind_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Ind':
        Ind_team.append(df2.iloc[i,15])
b17 = statistics.mean(Ind_team)

Lac_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Lac':
        Lac_team.append(df2.iloc[i,15])
b18 = statistics.mean(Lac_team)

Dal_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Dal':
        Dal_team.append(df2.iloc[i,15])
b19 = statistics.mean(Dal_team)

Lal_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Lal':
        Lal_team.append(df2.iloc[i,15])
b20 = statistics.mean(Lal_team)

Nyk_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Nyk':
        Nyk_team.append(df2.iloc[i,15])
b21 = statistics.mean(Nyk_team)

Atl_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Atl':
        Atl_team.append(df2.iloc[i,15])
b22 = statistics.mean(Atl_team)

Mem_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Mem':
        Mem_team.append(df2.iloc[i,15])
b23 = statistics.mean(Mem_team)

San_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'San':
        San_team.append(df2.iloc[i,15])
b24 = statistics.mean(San_team)

Gol_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Gol':
        Gol_team.append(df2.iloc[i,15])
b25 = statistics.mean(Gol_team)

Uta_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Uta':
        Uta_team.append(df2.iloc[i,15])
b26 = statistics.mean(Uta_team)

Pho_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Pho':
        Pho_team.append(df2.iloc[i,15])
b27 = statistics.mean(Pho_team)

Por_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Por':
        Por_team.append(df2.iloc[i,15])
b28 = statistics.mean(Por_team)

Cha_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Cha':
        Cha_team.append(df2.iloc[i,15])
b29 = statistics.mean(Cha_team)

Min_team = []
for i in df2.index:
    if df2.iloc[i,1] == 'Min':
        if math.isnan(df2.iloc[i,15]) == False:
            Min_team.append(df2.iloc[i,15])
b30 = statistics.mean(Min_team)

st.write("Source: [REFERENCE: Pandas Mean Function](https://www.geeksforgeeks.org/python-statistics-mean-function/)")

new = np.array([['Hou', b1],
                ['Orl', b2],
                ['Bro', b3],
                ['Cle', b4],
                ['Sac', b5],
                ['Phi', b6],
                ['Mil', b7],
                ['Chi', b8],
                ['Den', b9],
                ['Okc', b10],
                ['Tor', b11],
                ['Det', b12],
                ['Was', b13],
                ['Nor', b14],
                ['Bos', b15],
                ['Mia', b16],
                ['Ind', b17],
                ['Lac', b18],
                ['Dal', b19],
                ['Lal', b20],
                ['Nyk', b21],
                ['Atl', b22],
                ['Mem', b23],
                ['San', b24],
                ['Gol', b25],
                ['Uta', b26],
                ['Pho', b27],
                ['Por', b28],
                ['Cha', b29],
                ['Min', b30],
               ])
eff_df = pd.DataFrame(new, columns = ("TEAM", "eFG% (Effective Shooting %)"))
eff_df

"**SLIDE TO SEE THE MEAN Effective Shooting % FOR EACH TEAM!**"
Y = st.select_slider('Select a NBA Team to see what their mean Effective Shooting % was', options = eff_df['TEAM'])
eff_df[eff_df["TEAM"] == Y]

"Here's a table showing who the top Effective Shooting Teams were!"
eff_df2 = eff_df.sort_values("eFG% (Effective Shooting %)", ascending = False)
eff_df2

"We can also take this data and graph it to view teams in comparison."

st.write("Source: [REFERENCE: Using Images in Python](https://www.geeksforgeeks.org/working-images-python/)")
st.write("Source: [REFERENCE: Implementing Images in Streamlit](https://medium.com/analytics-vidhya/ep5-adding-media-files-in-our-streamlit-web-app-74564af03642)")
st.write("Source: [REFERENCE: NBA Logo Pictures](https://en.wikipedia.org/wiki/National_Basketball_Association)")

source = pd.DataFrame.from_records([
      {"TEAM Name": 1, "eFG% (Effective Shooting %)": b1, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/2/28/Houston_Rockets.svg/1200px-Houston_Rockets.svg.png"},
      {"TEAM Name": 2, "eFG% (Effective Shooting %)": b2, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/1/10/Orlando_Magic_logo.svg/1200px-Orlando_Magic_logo.svg.png"},
      {"TEAM Name": 3, "eFG% (Effective Shooting %)": b3, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Brooklyn_Nets_newlogo.svg/1200px-Brooklyn_Nets_newlogo.svg.png"},
      {"TEAM Name": 4, "eFG% (Effective Shooting %)": b4, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/4/4b/Cleveland_Cavaliers_logo.svg/165px-Cleveland_Cavaliers_logo.svg.png"},
      {"TEAM Name": 5, "eFG% (Effective Shooting %)": b5, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/SacramentoKings.svg/1200px-SacramentoKings.svg.png"},
      {"TEAM Name": 6, "eFG% (Effective Shooting %)": b6, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/0/0e/Philadelphia_76ers_logo.svg/1200px-Philadelphia_76ers_logo.svg.png"},
      {"TEAM Name": 7, "eFG% (Effective Shooting %)": b7, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/4/4a/Milwaukee_Bucks_logo.svg/1200px-Milwaukee_Bucks_logo.svg.png"},
      {"TEAM Name": 8, "eFG% (Effective Shooting %)": b8, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Chicago_Bulls_logo.svg/300px-Chicago_Bulls_logo.svg.png"},
      {"TEAM Name": 9, "eFG% (Effective Shooting %)": b9, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/7/76/Denver_Nuggets.svg/1200px-Denver_Nuggets.svg.png"},
      {"TEAM Name": 10, "eFG% (Effective Shooting %)": b10, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/5/5d/Oklahoma_City_Thunder.svg/1200px-Oklahoma_City_Thunder.svg.png"},
      {"TEAM Name": 11, "eFG% (Effective Shooting %)": b11, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/3/36/Toronto_Raptors_logo.svg/1200px-Toronto_Raptors_logo.svg.png"},
      {"TEAM Name": 12, "eFG% (Effective Shooting %)": b12, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Pistons_logo17.svg/1200px-Pistons_logo17.svg.png"},
      {"TEAM Name": 13, "eFG% (Effective Shooting %)": b13, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/0/02/Washington_Wizards_logo.svg/1200px-Washington_Wizards_logo.svg.png"},
      {"TEAM Name": 14, "eFG% (Effective Shooting %)": b14, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/0/0d/New_Orleans_Pelicans_logo.svg/338px-New_Orleans_Pelicans_logo.svg.png"},
      {"TEAM Name": 15, "eFG% (Effective Shooting %)": b15, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/Boston_Celtics.svg/1200px-Boston_Celtics.svg.png"},
      {"TEAM Name": 16, "eFG% (Effective Shooting %)": b16, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/f/fb/Miami_Heat_logo.svg/1200px-Miami_Heat_logo.svg.png"},
      {"TEAM Name": 17, "eFG% (Effective Shooting %)": b17, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/1/1b/Indiana_Pacers.svg/1200px-Indiana_Pacers.svg.png"},
      {"TEAM Name": 18, "eFG% (Effective Shooting %)": b18, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/b/bb/Los_Angeles_Clippers_%282015%29.svg/1200px-Los_Angeles_Clippers_%282015%29.svg.png"},
      {"TEAM Name": 19, "eFG% (Effective Shooting %)": b19, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/9/97/Dallas_Mavericks_logo.svg/1200px-Dallas_Mavericks_logo.svg.png"},
      {"TEAM Name": 20, "eFG% (Effective Shooting %)": b20, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Los_Angeles_Lakers_logo.svg/1200px-Los_Angeles_Lakers_logo.svg.png"},
      {"TEAM Name": 21, "eFG% (Effective Shooting %)": b21, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/2/25/New_York_Knicks_logo.svg/1200px-New_York_Knicks_logo.svg.png"},
      {"TEAM Name": 22, "eFG% (Effective Shooting %)": b22, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/2/24/Atlanta_Hawks_logo.svg/1200px-Atlanta_Hawks_logo.svg.png"},
      {"TEAM Name": 23, "eFG% (Effective Shooting %)": b23, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/f/f1/Memphis_Grizzlies.svg/1200px-Memphis_Grizzlies.svg.png"},
      {"TEAM Name": 24, "eFG% (Effective Shooting %)": b24, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/San_Antonio_Spurs.svg/1200px-San_Antonio_Spurs.svg.png"},
      {"TEAM Name": 25, "eFG% (Effective Shooting %)": b25, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/0/01/Golden_State_Warriors_logo.svg/1200px-Golden_State_Warriors_logo.svg.png"},
      {"TEAM Name": 26, "eFG% (Effective Shooting %)": b26, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/Utah_Jazz_logo_%282016%29.svg/1200px-Utah_Jazz_logo_%282016%29.svg.png"},
      {"TEAM Name": 27, "eFG% (Effective Shooting %)": b27, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/d/dc/Phoenix_Suns_logo.svg/1200px-Phoenix_Suns_logo.svg.png"},
      {"TEAM Name": 28, "eFG% (Effective Shooting %)": b28, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/2/21/Portland_Trail_Blazers_logo.svg/1200px-Portland_Trail_Blazers_logo.svg.png"},
      {"TEAM Name": 29, "eFG% (Effective Shooting %)": b29, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c4/Charlotte_Hornets_%282014%29.svg/1200px-Charlotte_Hornets_%282014%29.svg.png"},
      {"TEAM Name": 30, "eFG% (Effective Shooting %)": b30, "img": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/Minnesota_Timberwolves_logo.svg/1200px-Minnesota_Timberwolves_logo.svg.png"},
])

topic2_chart = alt.Chart(source).mark_image(
    width=30,
    height=30
).encode(
    x='TEAM Name',
    y='eFG% (Effective Shooting %)',
    url='img',
    tooltip = 'eFG% (Effective Shooting %)'
).properties(
width=1000,
height=400)
topic2_chart

">> **Conclusion**: After sorting the data and comparing the means using a sorted dataframe and the above altair chart, we can see that the Miami team was the clear top dog when viewing effective shooting percentage. The next few highest effective shooting teams were Toronto, Boston, Los Angeles (Lakers), and Phoenix. But specifically when looking at the data from this topic, Miami was the best team for effective shooting percentage."

st.markdown("""---""")

#Topic #3
st.subheader("Topic 3: Assist Percentage")
"> **Goal**: The goal for this topic is to see which team plays the best together. In basketball, a good sign of whether a team works well together is if they pass well and try to get each other to score often. An assist is essentially when one teammate passes to another to eventually lead to the second teammate scoring. Ultimately, this is reflected in their assist statistics. So, similarly to Topic 2, we are going to look at each team's average statistic; but for this topic, we will take the mean assist statistic to see which team seems to play the best together."

"Here below, we have all of the respective teams' average assist percentage."
Hou_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Hou':
        Hou_team2.append(df2.iloc[i,21])
c1 = statistics.mean(Hou_team2)

Orl_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Orl':
        Orl_team2.append(df2.iloc[i,21])
c2 = statistics.mean(Orl_team2)

Bro_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Bro':
        Bro_team2.append(df2.iloc[i,21])
c3 = statistics.mean(Bro_team2)

Cle_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Cle':
        Cle_team2.append(df2.iloc[i,21])
c4 = statistics.mean(Cle_team2)

Sac_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Sac':
        Sac_team2.append(df2.iloc[i,21])
c5 = statistics.mean(Sac_team2)

Phi_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Phi':
        Phi_team2.append(df2.iloc[i,21])
c6 = statistics.mean(Phi_team2)

Mil_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Mil':
        Mil_team2.append(df2.iloc[i,21])
c7 = statistics.mean(Mil_team2)

Chi_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Chi':
        Chi_team2.append(df2.iloc[i,21])
c8 = statistics.mean(Chi_team2)

Den_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Den':
        Den_team2.append(df2.iloc[i,21])
c9 = statistics.mean(Den_team2)

Okc_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Okc':
        Okc_team2.append(df2.iloc[i,21])
c10 = statistics.mean(Okc_team2)

Tor_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Tor':
        Tor_team2.append(df2.iloc[i,21])
c11 = statistics.mean(Tor_team2)

Det_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Det':
        Det_team2.append(df2.iloc[i,21])
c12 = statistics.mean(Det_team2)

Was_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Was':
        Was_team2.append(df2.iloc[i,21])
c13 = statistics.mean(Was_team2)

Nor_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Nor':
        Nor_team2.append(df2.iloc[i,21])
c14 = statistics.mean(Nor_team2)

Bos_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Bos':
        Bos_team2.append(df2.iloc[i,21])
c15 = statistics.mean(Bos_team2)

Mia_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Mia':
        Mia_team2.append(df2.iloc[i,21])
c16 = statistics.mean(Mia_team2)

Ind_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Ind':
        Ind_team2.append(df2.iloc[i,21])
c17 = statistics.mean(Ind_team2)

Lac_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Lac':
        Lac_team2.append(df2.iloc[i,21])
c18 = statistics.mean(Lac_team2)

Dal_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Dal':
        Dal_team2.append(df2.iloc[i,21])
c19 = statistics.mean(Dal_team2)

Lal_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Lal':
        Lal_team2.append(df2.iloc[i,21])
c20 = statistics.mean(Lal_team2)

Nyk_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Nyk':
        Nyk_team2.append(df2.iloc[i,21])
c21 = statistics.mean(Nyk_team2)

Atl_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Atl':
        Atl_team2.append(df2.iloc[i,21])
c22 = statistics.mean(Atl_team2)

Mem_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Mem':
        Mem_team2.append(df2.iloc[i,21])
c23 = statistics.mean(Mem_team2)

San_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'San':
        San_team2.append(df2.iloc[i,21])
c24 = statistics.mean(San_team2)

Gol_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Gol':
        Gol_team2.append(df2.iloc[i,21])
c25 = statistics.mean(Gol_team2)

Uta_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Uta':
        Uta_team2.append(df2.iloc[i,21])
c26 = statistics.mean(Uta_team2)

Pho_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Pho':
        Pho_team2.append(df2.iloc[i,21])
c27 = statistics.mean(Pho_team2)

Por_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Por':
        Por_team2.append(df2.iloc[i,21])
c28 = statistics.mean(Por_team2)

Cha_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Cha':
        Cha_team2.append(df2.iloc[i,21])
c29 = statistics.mean(Cha_team2)

Min_team2 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Min':
        Min_team2.append(df2.iloc[i,21])
c30 = statistics.mean(Min_team2)

new2 = np.array([['Hou', c1],
                ['Orl', c2],
                ['Bro', c3],
                ['Cle', c4],
                ['Sac', c5],
                ['Phi', c6],
                ['Mil', c7],
                ['Chi', c8],
                ['Den', c9],
                ['Okc', c10],
                ['Tor', c11],
                ['Det', c12],
                ['Was', c13],
                ['Nor', c14],
                ['Bos', c15],
                ['Mia', c16],
                ['Ind', c17],
                ['Lac', c18],
                ['Dal', c19],
                ['Lal', c20],
                ['Nyk', c21],
                ['Atl', c22],
                ['Mem', c23],
                ['San', c24],
                ['Gol', c25],
                ['Uta', c26],
                ['Pho', c27],
                ['Por', c28],
                ['Cha', c29],
                ['Min', c30],
               ])
ast_df = pd.DataFrame(new2, columns = ("TEAM", "AST%(Assist%)"))
ast_df

"**SLIDE TO SEE THE MEAN Assist % FOR EACH TEAM!**"
X = st.selectbox('Select a NBA Team (or multiple teams) to see what their mean Assist % was', options = ast_df['TEAM'])
ast_df[ast_df["TEAM"] == X]

"Now, to be more specific and to sort the data, here's a list of the teams with the highest mean Assist percentage!"
ast_df2 = ast_df.sort_values("AST%(Assist%)", ascending = False)
ast_df2

bars = alt.Chart(ast_df2).mark_bar().encode(
    x='AST%(Assist%):Q',
    y="TEAM:O",
    tooltip = ['TEAM', 'AST%(Assist%)'],
    color = alt.Color('AST%(Assist%)',scale=alt.Scale(scheme="viridis"))
)

text = bars.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='AST%(Assist%):Q'
)

"Here, we can see each team's assist percentage clearly and we can conclude which teams had the strongest assist statistics."
topic3_chart = (bars + text).properties(height=800, width=900)
topic3_chart


">> **Conclusion**: According to the bar chart above and the dataframe used above, we can conclude that Detroit had the strongest team mean assist percentage. The teams that were in the top 5 running for assist percentage were: Charlotte, Houston, Brooklyn, and Cleveland. All of these teams had high mean assist percentages. Because these assist passes eventually lead to teammates scoring, we can conclude that the teams with high assist percentages ultimately worked well together. Therefore, in conclusion, Detroit (on paper) seemed to be the strongest team to work together."


st.markdown("""---""")

#Topic #4
st.subheader("Topic 4: Turnovers Per Game")
"> **Goal**: After seeing the strengths of each team, it's time to evaluate the weaknesses for each team. In basketball statistics, turnovers are when the team loses possession of the basketball, ultimately at the cost of scoring points or capitalizing on a time period. So overall, turnovers are a bad statistic and each team strives to have as little turnovers as possible. So, during this topic, we will explore which teams had the lowest mean for turnovers per game."

"After sorting the data, here is each team's average number of turnovers per game."
Hou_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Hou':
        Hou_team3.append(df2.iloc[i,24])
d1 = statistics.mean(Hou_team3)

Orl_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Orl':
        Orl_team3.append(df2.iloc[i,24])
d2 = statistics.mean(Orl_team3)

Bro_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Bro':
        Bro_team3.append(df2.iloc[i,24])
d3 = statistics.mean(Bro_team3)

Cle_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Cle':
        Cle_team3.append(df2.iloc[i,24])
d4 = statistics.mean(Cle_team3)

Sac_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Sac':
        Sac_team3.append(df2.iloc[i,24])
d5 = statistics.mean(Sac_team3)

Phi_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Phi':
        Phi_team3.append(df2.iloc[i,24])
d6 = statistics.mean(Phi_team3)

Mil_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Mil':
        Mil_team3.append(df2.iloc[i,24])
d7 = statistics.mean(Mil_team3)

Chi_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Chi':
        Chi_team3.append(df2.iloc[i,24])
d8 = statistics.mean(Chi_team3)

Den_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Den':
        Den_team3.append(df2.iloc[i,24])
d9 = statistics.mean(Den_team3)

Okc_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Okc':
        Okc_team3.append(df2.iloc[i,24])
d10 = statistics.mean(Okc_team3)

Tor_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Tor':
        Tor_team3.append(df2.iloc[i,24])
d11 = statistics.mean(Tor_team3)

Det_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Det':
        Det_team3.append(df2.iloc[i,24])
d12 = statistics.mean(Det_team3)

Was_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Was':
        Was_team3.append(df2.iloc[i,24])
d13 = statistics.mean(Was_team3)

Nor_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Nor':
        Nor_team3.append(df2.iloc[i,24])
d14 = statistics.mean(Nor_team3)

Bos_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Bos':
        Bos_team3.append(df2.iloc[i,24])
d15 = statistics.mean(Bos_team3)

Mia_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Mia':
        Mia_team3.append(df2.iloc[i,24])
d16 = statistics.mean(Mia_team3)

Ind_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Ind':
        Ind_team3.append(df2.iloc[i,24])
d17 = statistics.mean(Ind_team3)

Lac_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Lac':
        Lac_team3.append(df2.iloc[i,24])
d18 = statistics.mean(Lac_team3)

Dal_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Dal':
        Dal_team3.append(df2.iloc[i,24])
d19 = statistics.mean(Dal_team3)

Lal_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Lal':
        Lal_team3.append(df2.iloc[i,24])
d20 = statistics.mean(Lal_team3)

Nyk_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Nyk':
        Nyk_team3.append(df2.iloc[i,24])
d21 = statistics.mean(Nyk_team3)

Atl_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Atl':
        Atl_team3.append(df2.iloc[i,24])
d22 = statistics.mean(Atl_team3)

Mem_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Mem':
        Mem_team3.append(df2.iloc[i,24])
d23 = statistics.mean(Mem_team3)

San_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'San':
        San_team3.append(df2.iloc[i,24])
d24 = statistics.mean(San_team3)

Gol_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Gol':
        Gol_team3.append(df2.iloc[i,24])
d25 = statistics.mean(Gol_team3)

Uta_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Uta':
        Uta_team3.append(df2.iloc[i,24])
d26 = statistics.mean(Uta_team3)

Pho_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Pho':
        Pho_team3.append(df2.iloc[i,24])
d27 = statistics.mean(Pho_team3)

Por_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Por':
        Por_team3.append(df2.iloc[i,24])
d28 = statistics.mean(Por_team3)

Cha_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Cha':
        Cha_team3.append(df2.iloc[i,24])
d29 = statistics.mean(Cha_team3)

Min_team3 = []
for i in df2.index:
    if df2.iloc[i,1] == 'Min':
        Min_team3.append(df2.iloc[i,24])
d30 = statistics.mean(Min_team3)

new3 = np.array([['Hou', d1],
                ['Orl', d2],
                ['Bro', d3],
                ['Cle', d4],
                ['Sac', d5],
                ['Phi', d6],
                ['Mil', d7],
                ['Chi', d8],
                ['Den', d9],
                ['Okc', d10],
                ['Tor', d11],
                ['Det', d12],
                ['Was', d13],
                ['Nor', d14],
                ['Bos', d15],
                ['Mia', d16],
                ['Ind', d17],
                ['Lac', d18],
                ['Dal', d19],
                ['Lal', d20],
                ['Nyk', d21],
                ['Atl', d22],
                ['Mem', d23],
                ['San', d24],
                ['Gol', d25],
                ['Uta', d26],
                ['Pho', d27],
                ['Por', d28],
                ['Cha', d29],
                ['Min', d30],
               ])
to_df = pd.DataFrame(new3, columns = ("TEAM", "TOPG (Turnovers per Game)"))
to_df

"Again, slightly similarly to the previous topics, here are the strongest teams in terms of turnovers per game. Only, this time, the strongest teams will be the teams with the lowest average of turnovers per game."
to_df2 = to_df.sort_values("TOPG (Turnovers per Game)", ascending = True)
to_df2

topg = st.radio("Select a team to view their average turnovers per game", to_df["TEAM"])
to_df[to_df["TEAM"] == topg]

V = alt.Chart(to_df).mark_bar().encode(
    x='TEAM:O',
    y='TOPG (Turnovers per Game):Q',
    tooltip = ['TEAM', 'TOPG (Turnovers per Game)'],
    color = alt.Color('TOPG (Turnovers per Game)',scale=alt.Scale(scheme="redpurple"))
).properties(height=400, width = 900)
V

">> **Conclusion**: We can clearly see through the radio selection, the dataframe, and the red chart above, that the Dallas team had the lowest mean for turnovers per game amongst their players. The other top 4 teams were: Philadelphia, San Antonio, New York, and Denver. We can conclude that these 5 teams were the best at handling the ball and each possession because the turnover rate was lower. However, just because these statistics may provide a conclusion on paper, this does not guarantee that the Dallas team was always the best at no turnovers."

st.markdown("""---""")

#Topic #5
st.subheader("Topic 5: Clustering Data")
"> **Goal**: For the last topic, I wanted to explore the dataset some more using a Kmeans algorithm. Specifically, I wanted to explore more about players' statistics regarding Games Played and Minutes Per Game."

df = pd.read_csv(r'C:\Users\yeesa\Math_10_Files_Spyder\nba_21_season.csv')
df = df.replace(" ", np.nan)
df = df.fillna(0)
df = df.drop(columns = ['RANK', 'VI (Versatility Index)', 'ORTG (Offensive Rating)', 'DRTG (Defensive Rating)'])
df2 = df.sort_values("TEAM")
from pandas.api.types import is_numeric_dtype
numeric_cols = [f for f in df.columns if is_numeric_dtype(df2[f])]
df3 = df2[numeric_cols].copy()
df4 = df3[~df3["MPG (Minutes per Game)"].isna()].copy()
from sklearn.cluster import KMeans
kmeans = KMeans(5)
kmeans.fit(df4)
kmeans.predict(df4)
df4["My Cluster"] = kmeans.predict(df4)
U = alt.Chart(df4).mark_circle().encode(
    x = "GP (Games Played)",
    y = "MPG (Minutes per Game)",
    color = "My Cluster:O",
    tooltip = "PPG (Points Per Game)").properties(width=700,height=500)

"In the graphic below, we were able to use 5 clusters to better understand the data. And we can clearly see how the 5 clusters were defined. We can also see the relation to points per game (Hint: Look at the graph's tooltip)."
U

st.markdown("""---""")

#Conclusion
st.subheader("**CONCLUSION**")
"> **Conclusion**: After viewing all of the data, we can come to a lose conclusion that some teams were stronger than others. Specifically in the data topics we observed, we can conclude that 2 main teams seemed dominant in these aspects."

if st.button('Click Here to Reveal the 1st of the 2 Strong Teams!!'):
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/9/97/Dallas_Mavericks_logo.svg/1200px-Dallas_Mavericks_logo.svg.png", width = 200)
    st.write("DALLAS MAVERICKS!!")
    
if st.button('Click Here to Reveal the 2nd of the 2 Strong Teams!!'):
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/0/0e/Philadelphia_76ers_logo.svg/1200px-Philadelphia_76ers_logo.svg.png", width = 200)
    st.write("PHILADELPHIA 76ERS!!")
    
"> *My Conclusion:* Obviously, to some extent, this exploration and conclusion with the dataset didn't perfectly figure out who the best NBA team was. However, it was very clear who the strong NBA teams were for the 2020-2021 Regular Season and who the stand-out players were."

st.markdown("""---""")

st.subheader("This is the end of my app! Hope you enjoyed learning about the NBA league!!")

st.markdown("""---""")

st.subheader("**References**")
st.write("Source: [Horizontal Line Mark](https://discuss.streamlit.io/t/horizontal-separator-line/11788/5)")
st.write("Source: [Altair Mark Charts (where I got most of my altair chart ideas)](https://altair-viz.github.io/user_guide/marks.html)")
st.write("Source: [Bar Chart with Line at Mean](https://altair-viz.github.io/gallery/bar_chart_with_mean_line.html)")
st.write("Source: [Pandas Mean Function](https://www.geeksforgeeks.org/python-statistics-mean-function/)")
st.write("Source: [Using Images in Python](https://www.geeksforgeeks.org/working-images-python/)")
st.write("Source: [Implementing Images in Streamlit](https://medium.com/analytics-vidhya/ep5-adding-media-files-in-our-streamlit-web-app-74564af03642)")
st.write("Source: [NBA Logo Pictures](https://en.wikipedia.org/wiki/National_Basketball_Association)")

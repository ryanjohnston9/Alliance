import ipywidgets as widgets
import random

##teams are created beforehand, then players are saved to their team:
Nova = []
Helios = []
Zenith = []
Aurora = []
teams = [Nova, Helios, Zenith, Aurora]
#...

player = widgets.Text(
       value='',
       description='Player', )

team = widgets.Dropdown(
       options=['Pick team', 'Nova', 'Helios', 'Aurora', 'Zenith'],
       value='Pick team',
       description='Team:')
finish_button = widgets.Button(description='Add Player')
out = widgets.Output()

box1 = widgets.VBox([player, team, finish_button])

def finish_button_clicked(_):
    if team.value == 'Nova':
        Nova.append(player.value.lower())
    elif team.value == 'Helios':
        Helios.append(player.value.lower())
    elif team.value == 'Zenith':
        Zenith.append(player.value.lower())
    elif team.value == 'Aurora':
        Aurora.append(player.value.lower())
    else:
        print('Pick a real team')
        return
    team.value = 'Pick team'
    player.value = ''

finish_button.on_click(finish_button_clicked)

def PlayerView(team):
    player_label.value = team[random.randint(0,(len(team)-1))]

check_player = widgets.Text(
       value='',
       description='Player', )

player_label = widgets.Label(value = '')

check_button = widgets.Button(description='Check')
clear_button = widgets.Button(description='Clear Player')

out = widgets.Output()

box2 = widgets.VBox([check_player, check_button, player_label, clear_button])

def check_button_clicked(_):
    other_team = []
    while True:
        other_team = teams[random.randint(0,(len(teams)-1))]
        if check_player.value not in other_team and other_team != []: break
    PlayerView(other_team)

def clear_button_clicked(_):
    player_label.value = ''
    check_player.value = ''

check_button.on_click(check_button_clicked)
clear_button.on_click(clear_button_clicked)

declare_team = widgets.Dropdown(
       options=['Pick team', 'Nova', 'Helios', 'Aurora', 'Zenith'],
       value='Pick team',
       description='Declare Team:')

add_player = widgets.Text(
       value='',
       description='Player:', )

list_label = widgets.Label(value = '')

add_button = widgets.Button(description='Add Player')
declare_button = widgets.Button(description='Declare')

box3 = widgets.VBox([declare_team, add_player, add_button, declare_button, list_label])

declared_list = []

def add_button_clicked(_):
    declared_list.append(add_player.value.lower())
    list_label.value += ' '
    list_label.value += add_player.value.lower()
    add_player.value = ''

def declare_button_clicked(_):
    list_label.value = ''
    actual_team_list = []
    if declare_team.value == 'Nova':
        actual_team_list = Nova
    elif declare_team.value == 'Helios':
        actual_team_list = Helios
    elif declare_team.value == 'Zenith':
        actual_team_list = Zenith
    elif declare_team.value == 'Aurora':
        actual_team_list = Aurora
    else:
        print('Pick a real team')
        return
    declared_list.sort()
    actual_team_list.sort()
    #print(declared_list), print(actual_team_list)
    if declared_list == actual_team_list:
        print('You win!')
        #print(declared_list), print(actual_team_list)
    else:
        print('Sorry, that is not correct. Continue playing.')
        declared_list.clear()
    declare_team.value = 'Pick team'


add_button.on_click(add_button_clicked)
declare_button.on_click(declare_button_clicked)

# defining a list with the contents of our windows
children = [box1, box2, box3]
# initializing a tab
tab = widgets.Tab()
# setting the tab windows
tab.children = children
# changing the title of the first and second window
tab.set_title(0, 'Set up teams')
tab.set_title(1, 'Check other team')
tab.set_title(2, 'Declare team')
tab

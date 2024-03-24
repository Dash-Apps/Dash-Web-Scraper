from pywebcopy import save_webpage
url = 'https://www.coolmathgames.com/'
folder = 'Desktop/March 2023'
kwargs = {'bypass_robots': True, 'project_name': 'sample_webpage'}
save_webpage(url, **kwargs)
print("webpage saved in the location:",folder)
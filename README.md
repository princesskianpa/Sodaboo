# Sodaboo
Soldatenspiel Bot. Test Project. 

I'm completly new to programming, so forgive me and my code. 
After 3 book chapters  about python I wanted to try something out and yeah.
Obviously I also googled quite a while to find out about the librarys I need to realize my Project.

Requirements can be found in the txt file.
Also required is the geckodriver wich can be downloaded here: https://github.com/mozilla/geckodriver/releases

So far Sodaboo only works on 1920x1080, Windows 10 basic layout & basic geckodriver layout.
Tested only with "Luftwaffe" game layout.

# Features:

1. Löst alle captchas. | Solves all captchas. =D
2. Trainiert zur Zeit ausschließlich Wachausbildung. | Only trains guardtactics.
3. Automatische Patrouille. | Automatic Patrouille.
4. Automatische Missionen & füllt bei Bedarf Ausdauer auf. | Auto mission & recharges stamina.
5. Bombenwetterevent wartet bis 100 Wut vorhanden sind und investiert diese in den Munitionsbau. | Bombenwetter event ammo creation.
6. Automatisches Begleiter Training | Auto companion training.


# Known Bugs:
1. Popups coming in the wrong time can crash/stop the bot, because it doesnt find the next element. (I didn't find a solution for this so far since threading does NOT work.)
2. After all missions are done, incl. stamina recharges and after done all training till money is completly gone bot crashes. Because it isn't finished yet. :)
3. Buggy when Firefox(Webdriver) is minimized.


# Questions? Suggestions? Need someone to talk to?
princesskianpa ADD gmail.com       :)

# ToDo
1. Auto train lowest tactics.
2. Auto companion attacks (Only level one enemys for patrons).
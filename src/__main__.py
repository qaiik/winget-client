import eel

eel.init('web')

@eel.expose
def listpackages():
  pack = os.popen('winget search').read().replace('\n','<br/>')
  return pack

eel.start('main.html')

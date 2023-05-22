import glob
import os


path =  os.path.dirname(os.path.realpath(__file__))

for file in glob.glob("./pages/*.html"):
    with open(file, 'r') as f:
        html_content = f.read()
    old_code = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&display=swap"
      rel="stylesheet" />
    <link
      href="https://fonts.googleapis.com/css2?family=Aboreto&display=swap"
      rel="stylesheet" />
    <link rel="stylesheet" href="../css/style.css" />
    <link rel="icon" type="image/x-icon" href="../images/test3.png" />
    <title>The power of music</title>
  </head>
  <body>
    <nav>
      <ul>
        <div class="dropdown">
          <button class="dropbtn">History</button>
          <div class="dropdown-content">
            <a href="centoPassi.html">Cento Passi</a>
            <a href="erika.html">Erika</a>
            <a href="IchBinSoldat.html"> Ich bin soldat </a>
            <a href="laGuerraDiPiero.html">La guerra di Piero</a>
            <a href="ohApple.html"> Oh Apple! </a>
            <a href="OBellaCiao.html">O Bella Ciao</a>
          </div>
        </div>
        <div class="dropdown">
          <button class="dropbtn">Literature</button>
          <div class="dropdown-content">
            <a href="Gulliver.html"> Gulliver </a>
            <a href="romeoAndJuliet.html">Romeo and Juliet</a>
            <a href="TheTaleOfCuChulainn.html"> The Tale of Cu Chulainn </a>
          </div>
        </div>
        <div class="dropdown">
          <button class="dropbtn">Jerry</button>
          <div class="dropdown-content">
            <a href="ricchiNo.html">Ricchi No</a>
          </div>
        </div>
        <div class="dropdown">
          <button class="dropbtn">Civics</button>
          <?-- non c'era più spazio*/>
          <div class="dropdown-content">
            <a href="anotherBrickInTheWall.html"> Another Brick in The Wall </a>
            <a href="allEyezOnMe.html">All Eyez On Me</a>
            <a href="bones.html">Bones</a>
            <a href="bornInTheUsa.html">Born in the Usa</a>
            <a href="californiaDreamin.html">California Dreamin</a>
            <a href="canYouFeelMyHeart.html">Can you feel my heart</a>
            <a href="copycat.html">Copycat</a>
            <a href="differentWorld.html">Different world</a>
            <a href="die.html">DIE</a>
            <a href="FUKDaPolice.html">Fucd da Police</a>
            <a href="imagine.html">Imagine</a>
          </div>
        </div>
        <div class="dropdown">
          <button class="dropbtn">Civics 2.0</button>
          <div class="dropdown-content">
            <a href="buonanotte.html"> Buonanotte </a>
            <a href="childrenOfTheGrave.html">Children of The Grave</a>
            <a href="goodKid.html"> Good Kid </a>
            <a href="GuerrillaRadio.html"> GuerrillaRadio </a>
            <a href="JeremySpoken.html"> Jeremy Spoken </a>
            <a href="laPaura.html"> La Paura </a>
            <a href="meAndMyBrokenHeart.html">Me and my broken heart</a>
            <a href="PezziDiCarta.html">Pezzi di Carta</a>
            <a href="TheSoundOfThSilence.html"> The Sound of the Silence </a>
            <a href="whiteAmerica.html"> White America </a>
            <a href="Zero.html"> Zero </a>
            <a href="zombie.html"> Zombie </a>
          </div>
        </div>
        <div class="dropdown">
          <button class="dropbtn">P.E.</button>
          <div class="dropdown-content">
            <a href="1-800-273-8255.html"> 1-800-273-8255 </a>
            <a href="7miliardi.html">7 Miliardi</a>
            <a href="alconnoneunproblema.html">L'Alcool non è un problema</a>
          </div>
        </div>
      </ul>
    </nav>
    '''
    new_code = '''
    '''

    updated_content = html_content.replace(old_code, new_code)
    with open(file, 'w') as f:
        f.write(updated_content)
    print("Updated:", file)
    # with open(file, "")
    # line = file.
    # while(line.strip() not "<nav>")
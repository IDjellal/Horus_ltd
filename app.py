from flask import Flask, render_template

app=Flask(__name__)
#run fonction generer et  avec paramettre dans la fonction taux monte 
#ect...pour faire userrequest
PAGES=[
    {
      'id':1,
      'Nom Page':'Horus Time Trek',
      'Descriptif':'Test Horus on Time Trek. Witness past predictions.',
      },
    {
      'id':2,
      'Nom Page':'HorusCraft Forge',
      'Descriptif':'Customize at HorusCraft Forge. Generate your own portfolio',
      },
    {
      'id':3,
      'Nom Page':'Horus Odyssey',
      'Descriptif':'Dive into Horus vision. Read the manifesto, understand philosophy.',
      }
  
    ]
@app.route("/")
def hello():
  return render_template("home.html",
                        pages=PAGES)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
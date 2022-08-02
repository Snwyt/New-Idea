from website import create_app

app = create_app()

if __name__ == '__main__':
  app.run(debug=True) #turn false when this site goes live

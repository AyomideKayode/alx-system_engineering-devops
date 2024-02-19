
- ssh into your web server
  ssh ubuntu@your-web-server-ip

- Install the net-tools package on your server by running the command:
  sudo apt install -y net-tools

- Git clone your AirBnB_clone_v2 on your web-01 server:
  git clone https://github.com/your-username/AirBnB_clone_v2.git

- Navigate to the web_flask directory:
  cd AirBnB_clone_v2/web_flask

- Modify the 0-hello_route.py script to serve its content from the route /airbnb-onepage/ on port 5000. Update the file as follows:

  @app.route('/airbnb-onepage/', strict_slashes=False)
  def hello_hbnb():
  """Function called through the /airbnb-onepage/ route."""
  return 'Hello HBNB!'

  if **name** == '**main**':
  app.run(host='0.0.0.0', port=5000)

- Save the changes and run your Flask application:
  python3 -m web_flask.0-hello_route

- Verify the configuration using curl: (on another window)
  curl 127.0.0.1:5000/airbnb-onepage/

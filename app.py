from application import app #app from __init__
from application.books import routes
from application import routes



if __name__=='__main__':
    #app.run()
    app.run(port=4000, debug=True,host="0.0.0.0") 

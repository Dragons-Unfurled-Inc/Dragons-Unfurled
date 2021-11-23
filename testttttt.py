# #Test2
# import uvicorn
# from flask import Flask, jsonify
# from flask_restful import Resource, Api


# """
# # Connect to your postgres DB
# conn = psycopg2.connect("dbname=test user=postgres")

# # Open a cursor to perform database operations
# cur = conn.cursor()

# # Execute a query
# cur.execute("SELECT * FROM my_data")

# # Retrieve query results
# records = cur.fetchall()
# """

# app = Flask(__name__)
# api = Api(app)

# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}
    
# @app.route("/hello")
# def hello():
#     return "Hello World!"

# @app.route('/meteo')
# def meteo():
#     dictionnaire = {
#         'type': 'Prévision de température',
#         'valeurs': [24, 24, 25, 26, 27, 28],
#         'unite': "degrés Celcius"
#     }
#     return jsonify(dictionnaire)

# api.add_resource(HelloWorld, '/')

# if __name__ == '__main__':
#     uvicorn.run("__main__:app", host="0.0.0.0", port="5000", log_level="info")

# #test

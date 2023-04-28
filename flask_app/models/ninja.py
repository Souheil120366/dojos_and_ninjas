from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id= data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
# Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
    # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
    # Create an empty list to append our instances of friends
        ninjas = []
    # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
    
        return ninjas
    
    @classmethod
    def get_ninja(cls,id):
        
        query = "SELECT * FROM users WHERE id ="+str(id)
        # make sure to call the connectToMySQL function with the schema you are targeting.
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        
        return result
    
    @classmethod
    def del_ninja(cls,id):
        
        query = "DELETE FROM ninjas WHERE id ="+str(id)
        
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        
        return result
    
    @classmethod
    def update_ninja(cls,data):
        
        query = "UPDATE ninjas SET first_name=%(fname)s, last_name=%(lname)s, age=%(age)s, updated_at=NOW() WHERE id = %(id)s;"
        
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(result)
        
        return result
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas ( first_name , last_name , age , created_at, updated_at, dojo_id ) VALUES ( %(fname)s , %(lname)s , %(age)s , NOW() , NOW(),%(dojo_id)s );"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )        

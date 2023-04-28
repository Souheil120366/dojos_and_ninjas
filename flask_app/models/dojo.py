from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__( self , data ):
        self.id= data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
  
        return dojos
    
    @classmethod
    def get_dojo_ninjas(cls,data):
        # query = "SELECT * FROM dojos WHERE id ="+str(id)
        query = "SELECT * FROM ninjas LEFT JOIN dojos ON ninjas.dojo_id = dojos.id WHERE ninjas.dojo_id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print("result",result)
        return result
    
    @classmethod
    def get_dojo_name(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print("result",result)
        return cls(result[0])
    
    @classmethod
    def del_dojo(cls,id):
        
        query = "DELETE FROM dojos WHERE id ="+str(id)
        
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        
        return result
    
    @classmethod
    def update_dojo(cls,data):
        query = "UPDATE dojos SET name=%(name)s, updated_at=NOW() WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )        

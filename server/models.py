from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    name = db.Column(db.String, nullable=False, unique=True)
    phone_number = db.Column(db.String)

    # nullable = False, unique = True
    # the above will raise IntegrityErrors from table level
    # we can manually write ValueErrors with @validates

    @validates('name')
    def validate_name(self, key, name_value):
        #1. all authors have a name
        # see tests - requires ValueError on fail
        if not name_value:
            raise ValueError('name cannot be null')
        #2. all author names must be unique
        #get all existing authors name
        names = db.session.query(Author.name).all()
        #check if current name_value exists in names
        if name_value in names:
            raise ValueError('name must be unique')
        return name_value
    
    #3. phone numbers are exactly 10 digits
    @validates('phone_number')
    def validate_number(self, key, cur_phone):
        if(len(cur_phone) != 10):
            raise ValueError('phone number must be length 10')
        return cur_phone



    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'
    
        
class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #4. all posts have a title
    # tests expect an IntegrityError which is returned by table-level constraints
    # if tests called for a ValueError, we would create @validates and manually return a ValueError
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    summary = db.Column(db.String)
    category = db.Column(db.String)

    #5. post content is at least 250 characters long
    # @validates('content')
    # def validate_content(self, key, cur_content):
    #     if(len(cur_content) < 250):
    #         raise ValueError('content too short')
    #     return cur_content
    
    #6. post summary is a maximum of 250 chars
    @validates('summary')
    def validate_summary(self, key, cur_summary):
        if(len(cur_summary) > 250):
            raise ValueError('max 250 chars')
        return cur_summary

    #7. post category is either Fiction or Non-Fiction
    @validates('category')
    def validate_category(self, key, cur_cat):
        if(cur_cat != 'Fiction' and cur_cat != 'Non-Fiction'):
            raise ValueError('must be Fiction or Non-Fiction')
        return cur_cat

    #8. 
    @validates('title')
    def validate_title(self, key, cur_title):
        baits = ["Won't Believe", "Secret", "Top", "Guess"]
        # if not cur_title in [need for need in baits]:
        #     raise ValueError('need a bait')
        # make sure to check all values in bait before raising ValueError
        for bait in baits: #bait = Won't Believe
            if bait in cur_title: #cur_title = Secret
                return cur_title
        raise ValueError('need bait')
    
    
    
    #@validate(column_name)
    #def fxn(self, key, incoming_value):
    #   if incoming_value is valid:
    #       return incoming_value
    #   raise ValueError
    #
    #   if incoming_value not valid:
    #       raise ValueError
    #   return incoming_value
    
    
    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
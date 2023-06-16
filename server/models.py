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

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

    @validates('name')
    def validate_name(self, key, name):
        names = db.session.query(Author.name).all()
        if not name:
            raise ValueError('Name field is required')
        elif name in names: 
            raise ValueError('Name must be unique')
        else:
            return name 
    
    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if len(phone_number) != 10:
            raise ValueError('10 digits please')
        return phone_number
        
class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    summary = db.Column(db.String())
    category = db.Column(db.String)

    @validates('title')
    def validate_title(self, key, title):
        if not title:
            raise ValueError('must have title')
        list = ["Won't Believe", "Secret", "Top", "Guess"]
        for bait in list:
            if (bait in title):
                return title 
        raise ValueError('need a bait')

    
    @validates('content')
    def validate_content(self, key, content):
        if(len(content) < 250):
            raise ValueError('post content must be 250 chars or more')
        return content 

    @validates('summary')
    def validate_summary(self, key, summary):
        if(len(summary) > 250):
            raise ValueError('summary must be less than 250 chars')
        return summary 

    @validates('category')
    def validate_category(self, key, cat):
        if(cat != 'Fiction' and cat != 'Non-Fiction'):
            raise ValueError('cat must be Fiction or Non-Fiction')
        return cat

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
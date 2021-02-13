from coreapp import db

class CollaboratorProject(db.Model):
    

    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
    project_id = db.Column('project_id', db.Integer, db.ForeignKey('project.id', ondelete='CASCADE'), primary_key=True)
    #Permisos del Colaborador
    leader = db.Column(db.Boolean, default=False)
    add_task = db.Column(db.Boolean, default= False)
    delete_task = db.Column(db.Boolean, default=False)
    done_task = db.Column(db.Boolean, default=True)
    store_task = db.Column(db.Boolean, default=False)
    add_collaborator = db.Column(db.Boolean, default=False)
    delete_collaborator = db.Column(db.Boolean, default=False)
    update_charges = db.Column(db.Boolean, default=False)
    #Relaciones
    collaborator = db.relationship('User', back_populates='collaborations')
    project = db.relationship('Project', back_populates='collaborators')

    def __repr__(self):
        return f'<{self.collaborator} collaborating in {self.project}>'

class Project(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.Text)
    creation_date = db.Column(db.String(20), nullable=False)
    limit_date = db.Column(db.String(20))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    color = db.Column(db.String(10), default='#00b295')
    public = db.Column(db.Boolean, default=0, nullable=False)
    collaborators = db.relationship('CollaboratorProject', back_populates='project')

    def __init__(self, title, description, public):
        self.title = title
        self.description = description
        self.public = public


    def __repr__(self):
        return f'<Project {self.title}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_by_id(id):
        return Project.query.get(id)

    @staticmethod
    def get_by_title(title):
        return Project.query.filter_by(title=title).first()


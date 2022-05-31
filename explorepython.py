#A Python library for explaining the capabilities of python.
import wikipedia
def python():
    print('Python Programming')
    definition=wikipedia.summary("Python Programming")
    print(definition)
    print('--------------------------')
def pythonusecases():
    print("Uses of Python")
    usecases="""
    1.Webdevelopment
    2.Datascience
    3.Business
    4.Artificial Intelligence
    5.Computer aided design
    6.Webscraping
    7.Analytics
    8.Data visualization
    9.Internet of things
    """
    print(usecases)

def Datascienceframeworks():
    print('--------Data science Frameworks--------')
    libml="""
    1.Keras
    2.Tensorflow
    3.Pytorch
    4.Numpy
    5.Scipy
    6.Scikit-learn
    7.Theano
    8.Pandas
    9.Matplotlib
    10.Plotly
    """
    print(libml)
def Datascienceframeworksdocumentation():
    print('-------Libraries documentation links-------')
    doc="""
    1.Keras='https://keras.io/'
    2.Tensorflow='https://www.tensorflow.org/'
    3.PyTorch='https://pytorch.org/'
    4.Numpy='https://numpy.org/'
    5.Scipy='https://scipy.org/"
    6.Scikit-learn='https://scikit-learn.org/stable/index.html'
    7.Theano="https://pypi.org/project/Theano/"
    8.Pandas='https://pandas.pydata.org/'
    9.Matplotlib='https://matplotlib.org/'
    10.Plotly='https://plotly.com/'

    """
    print(doc)

def webdevelopmentframeworks():
    print('--------Webdevelopment Frameworks--------')
    libweb="""
    1.Django
    2.CherryPy
    3.TurboGears
    4.Flask
    5.Web2py
    6.Bottle
    7.Falcon
    8.CubicWeb
    9.Quixote
    10.Pyramid
    """
    print(libweb)
def webdevelopmentlibrariesdocumentation():
    webdoc="""
    1.Django='https://www.djangoproject.com/'
    2.CherryPy='https://github.com/cherrypy/cherrypy/tree/main/cherrypy'
    3.TurboGears='https://turbogears.org/welcome/turbogears-way.html'
    4.Flask='https://flask.palletsprojects.com'
    5.Web2py='http://www.web2py.com/'
    6.Bottle='https://github.com/bottlepy/bottle'
    7.Falcon='https://falconframework.org/'
    8.CubicWeb='https://cubicweb.readthedocs.io/en/latest/'
    9.Quixnote='http://quixote.ca/'
    10.Pyramid='https://github.com/Pylons/pyramid/blob/2.0-branch/docs/index.rst'
    """
    print(webdoc)


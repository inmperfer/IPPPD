from sklearn.cross_validation import KFold, StratifiedKFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.grid_search import RandomizedSearchCV, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss
from sklearn.metrics import make_scorer
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor
from xgboost import XGBClassifier
from sklearn.linear_model import Lasso
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import BayesianRidge
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import ElasticNet
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor

from feature_selection import TreeBased
import persistance
from feature_transform import LabelTransform, InteractionTransform, ImputerTransform, RemoveStringsTransform, Encoder, LogTransform, DummyId


DATA_DIR = 'cs570/data'
DATA_READER = persistance.FileReader
DATA_COLUMN_SEP = ','

SAVE_MODELS = False
MODELS_DIR = 'cs570/models'

PREDICTIONS_DIR = 'cs570/submissions'
PREDICTIONS_PREPROCESS = [DummyId()]
PREDICTION_COLUMNS = ['id']
NEED_PROBA = False

TARGET = "y"
TARGET_TRANSFORM = LabelTransform

SCORER = make_scorer(log_loss,
                     needs_proba=True,
                     greater_is_better=False)

RANDOM_STATE = 2016
JOBS = 3

FEATURE_SELECTION_N = 20

PREPROCESSING = [

    ('scaler_int', [
        ('dropNaN', ImputerTransform()),
        ('clean', RemoveStringsTransform(strings=['%', '$'])),
        ('encode', Encoder()),
       # ('log', LogTransform()),
        ('inter', InteractionTransform(
            interactions=['add'],
            columns=['x%d' % i for i in range(1, 10)])),
        ('std', StandardScaler()),
        ('fs', TreeBased('extra_trees_regressor', 20, 190)),

    ]),


]

MODELS = {
    ('lr', LogisticRegression(fit_intercept=True, solver='newton-cg',
                              multi_class='multinomial')),
    ('rf', RandomForestClassifier(random_state=RANDOM_STATE)),
    ('xgbClasifier', XGBClassifier(base_score=0.5, colsample_bylevel=0.6, colsample_bytree=0.6,
       gamma=0, learning_rate=0.1, max_delta_step=0,
       max_depth=10, min_child_weight=1,
       n_estimators=1000, nthread=-1, objective='binary:logistic',
       reg_alpha=0.6, reg_lambda=1, scale_pos_weight=1, silent=True,
       subsample=1)),

    ('xgb', XGBRegressor()),
    ('lasso', Lasso(fit_intercept=True)), # inma
    ('ridge', Ridge(fit_intercept=True)),
    ('elastic_net', ElasticNet(fit_intercept=True)),
    ('bayes_ridge', BayesianRidge(fit_intercept=True)),
    ('SGD', SGDRegressor()),
    ('gb', GradientBoostingRegressor()),
    #('KNN', KNeighborsRegressor(n_neighbors=10)),
}

FOLDS = {
    'generator': StratifiedKFold,
    'params': {
         'n_folds': 3,
         'shuffle': True,
         'random_state': RANDOM_STATE,
    }
}

META_PARAMETER_OPTIMIZATION = True
META_PARAMETER_OPTIMIZER = GridSearchCV
MAX_PARAMETER_SEARCH_ITERATIONS = 100
META_PARAMETERS = {

    'lr': {
        'fit_intercept': [True, False],
        'C': [200, 2000, 20000],
        'tol': [0.006]
    },


    'rf': {
        'n_estimators': [25],
        'criterion': ['gini'],
        'max_features': ['sqrt'],
        'max_depth': [3],
        'min_samples_split': [1],
        'min_samples_leaf': [3, 1]
    },

    'gb': {
        'n_estimators': [4],
        'max_features': ['sqrt'],
        'max_depth': [6],
        'min_samples_split': [0.6],
        'min_samples_leaf': [5],
    },

    'KNN': {
        'n_neighbors': [5, 10, 20],
        'algorithm': ['ball_tree', 'kd_tree'],
        'leaf_size': [20, 30],
        'p': [1, 2]
    }
}





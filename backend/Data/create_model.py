import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import joblib

# Charger les données à partir du fichier CSV
data = pd.read_csv('cleanData4.csv')

# Séparer les caractéristiques et la variable cible
features = data[['Manufacturer', 'Prod. year', 'Category', 'Mileage', 'Airbags', 'Engine volume', 'Gear box type',
                 'Levy', 'Turbo', 'Fuel type', 'Drive wheels', 'Model', 'Cylinders', 'Leather interior']]
target = data['Price']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Définir les colonnes catégorielles et numériques
categorical_cols = ['Manufacturer', 'Category', 'Gear box type', 'Fuel type', 'Drive wheels', 'Model']
numeric_cols = ['Prod. year', 'Mileage', 'Airbags', 'Engine volume', 'Levy', 'Cylinders']

# Créer les transformateurs pour les colonnes catégorielles et numériques
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

# Créer la colonne transformer pour appliquer les transformations aux bonnes colonnes
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_cols),
        ('num', numeric_transformer, numeric_cols)
    ])

# Créer le pipeline complet avec le préprocesseur et le modèle de régression linéaire
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Entraîner le modèle
model.fit(X_train, y_train)

# Évaluer le modèle sur l'ensemble de test
score = model.score(X_test, y_test)
print(f"Score du modèle : {score}")

# Sauvegarder le modèle et les encodages
joblib.dump(model, 'modele_regression_linaire.pkl')
joblib.dump(preprocessor, 'encodages.pkl')
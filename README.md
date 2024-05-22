# 2023_wa_sa_gavrylenko_gaflix

## První inicializace projektu
```
# Vyklonovani repozitare a presun do slozky projektu
git clone https://github.com/gyarab/2023_wa_sa_gavrylenko_gaflix.git
cd 2023_wa_sa_gavrylenko_gaflix
```

#### Vytvoreni virtualniho prostredi a aktivace
```
python -m venv venv
source ./venv/Scripts/activate
```
#### Instalace potrebnych balicku
```
pip install -r requirements.txt
```
#### Tvorba a vyplneni databaze
```
python manage.py migrate
python manage.py loaddata fixtures/*.json
```

## Pri zmene `models.py`
```
python manage.py makemigrations
python manage.py migrate
```

## Spusteni projektu
```
git pull
source ./venv/Scripts/activate
python manage.py migrate
python manage.py runserver
```

## Pri zmene v databazi
```
python manage.py dumpdata --indent 2 *model* > fixtures/*model*.json

# Prepisem json soubor
python manage.py loaddata fixtures/*.json
```

## Reset databaze
```
# Smazani soucasne db
rm db.sqlite3

# Vytvoreni nove db s nasi strukturou
python manage.py migrate

# Nahrani dat ze vsech json souboru
python manage.py loaddata fixtures/*.json
```

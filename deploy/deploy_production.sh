read -p "Are you sure you want to deploy to Heroku [production] [y/n]? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    cd ..
    git push heroku master
    heroku run python src/manage.py migrate
    heroku open
    cd deploy
fi

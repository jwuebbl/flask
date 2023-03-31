if [ $(pwd) = "/c/Users/JeffW/Desktop/flask" ]; then
    cd ./golf
fi


ng build --base-href "/static/" 

cp ./dist/golf/*.js ../app/static
cp ./dist/golf/*.css ../app/static
cp ./dist/golf/*.html ../app/templates/index.html
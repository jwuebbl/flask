if [ $(pwd) = "/c/Users/JeffW/Desktop/flask" ]; then
    cd ./golf
fi


ng build

cp ./dist/golf/*.js ../app/static

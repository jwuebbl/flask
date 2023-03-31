function runApp() {
    echo "runApp() called."
}

if [ "$(pwd)" = "/home/ubuntu/flask/golf" ]; then
    echo "Correct directory, running application"
    runApp
elif [ "$(pwd)" = "/home/ubuntu/flask" ]; then
    cd ./golf
    echo $(pwd)
fi
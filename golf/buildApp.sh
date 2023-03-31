function runApp() {
    echo "runApp() called."
}

if [ "$(pwd)" = "/home/ubuntu/flask/golf" ]; then
    echo "Correct directory, running application"
    runApp
elif [ "$(pwd)" = "/home/ubuntu/flask" ]; then
    echo "buildApp.sh called from $(pwd)."
    runApp
else
    echo "Can't run the script from this directory"
    exit
fi
pwd = $(pwd)
echo $pwd

function runApp() {
    echo "runApp() called."
}
echo $pwd
if [ "$pwd" = "/home/ubuntu/flask/golf" ]; then
    echo "Correct directory, running application"
    runApp
fi
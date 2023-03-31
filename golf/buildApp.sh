pwd = $(pwd)
echo $pwd

if [ $pwd != "/c/Users/JeffW/Desktop/flask/golf" ]; then
  echo "You can't run this here"
  exit
elif [ $pwd != "/home/ubuntu/flask/golf" ]; then
    echo "You can't run this here"
    exit
else
    echo "Passed directory check"
fi

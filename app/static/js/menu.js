function displayGifAndGoToPage(pageName) {
    setTimeout(function() {
        window.location.href = pageName;
    }, 1500);
}

document.addEventListener('DOMContentLoaded', function() {
    // Buttons
    var rouletteButton = document.getElementById('rouletteButton');
    var leagueButton = document.getElementById('leagueButton');
    var logoutButton = document.getElementById('logoutButton');

    // The Gif Displayed when a button is clicked
    var ciggyGif = document.getElementById('ciggyGif');

    // Actions when buttons are clicked
    rouletteButton.addEventListener('click', displayGifAndGoToPage('/roulette'));
    leagueButton.addEventListener('click', displayGifAndGoToPage('/submitLeagueGame'));
    logoutButton.addEventListener('click', displayGifAndGoToPage('/logout'));
});
document.addEventListener('DOMContentLoaded', function() {
    var rouletteButton = document.getElementById('rouletteButton');
    var leagueButton = document.getElementById('leagueButton');
    var logoutButton = document.getElementById('logoutButton');

    var ciggyGif = document.getElementById('ciggyGif');

    rouletteButton.addEventListener('click', function() {
        ciggyGif.style.display = 'block';
        setTimeout(function() {
            window.location.href = '/roulette';
        }, 2500);
    });

    leagueButton.addEventListener('click', function() {
        ciggyGif.style.display = 'block';
        setTimeout(function() {
            window.location.href = '/submitLeagueGame';
        }, 2500);
    });

    logoutButton.addEventListener('click', function() {
        ciggyGif.style.display = 'block';
        setTimeout(function() {
            window.location.href = '/logout';
        }, 2500);
    });
});
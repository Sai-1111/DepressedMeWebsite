function myAnxiety() {
    document.getElementById("anxit").style.display = "block"
    document.getElementById("deppr").style.display = "none"
}

function myDepression() {
    document.getElementById("deppr").style.display = "block"
    document.getElementById("anxit").style.display = "none"
}


document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('anx_button').addEventListener('click', function() {
        document.getElementById('AnxbuttonClicked').value = 'true';
    });
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('dep_button').addEventListener('click', function() {
        document.getElementById('DepbuttonClicked').value = 'true';
    });
});
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <title>Profil JobIA</title>
</head>

<body>

<h1>Mon profil JobIA</h1>

<p>Métier recherché :</p>
<input id="metier" type="text">

<p>Ville :</p>
<input id="ville" type="text">

<p>Mes compétences :</p>
<textarea id="competences"></textarea>

<br><br>

<button onclick="analyserProfil()">
    Analyser mon profil
</button>

<h2>Résultat JobIA :</h2>

<p id="resultat">
    En attente...
</p>


<script>

function analyserProfil(){

    let metier = document.getElementById("metier").value;
    let ville = document.getElementById("ville").value;
    let competences = document.getElementById("competences").value;


    document.getElementById("resultat").innerHTML =
    "🚀 JobIA a analysé ton profil :<br><br>" +
    "Métier : " + metier + "<br>" +
    "Ville : " + ville + "<br>" +
    "Compétences : " + competences + "<br><br>" +
    "✅ Voici ton profil prêt pour la recherche d'emploi !";

}

</script>


</body>

</html>
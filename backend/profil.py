<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <title>Profil JobIA</title>
</head>

<body>

<h1>Créer mon profil JobIA</h1>

<label>Métier recherché :</label><br>
<input id="metier" type="text"><br><br>

<label>Ville :</label><br>
<input id="ville" type="text"><br><br>

<label>Compétences :</label><br>
<textarea id="competences"></textarea><br><br>

<button onclick="analyser()">
    Lancer mon analyse IA
</button>


<h2>Résultat :</h2>

<pre id="resultat">
En attente...
</pre>


<script>

async function analyser(){

    let reponse = await fetch("http://127.0.0.1:8000/analyse", {
        method: "POST",
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            metier: document.getElementById("metier").value,
            ville: document.getElementById("ville").value,
            competences: document.getElementById("competences").value
        })
    });


    let resultat = await reponse.json();

    document.getElementById("resultat").textContent =
    JSON.stringify(resultat, null, 2);

}

</script>


</body>

</html>
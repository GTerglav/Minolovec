<!DOCTYPE html>
<html>
<head>
  <title> Minolovec </title>
</head>

<style>
  body {
      background-color: lightblue;
    }

  h1 {
      color:black;
      text-align: center;
      font-family: verdana;
      font-size: 40px;
      margin-bottom: 20px
    }
  h2 {
      font-family: verdana;
      font-size: 30px;
      margin-left: 10px
  }
  p {
      font-family: verdana;
      margin-left: 10px
  }
  form {
        margin-left: 10px;
  }

  input[type=text], select {
  width: 7%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  }

  input[type=submit] {
    width: 7%;
    background-color: #4CAF50;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  input[type=submit]:hover {
    background-color: #45a049;
  }
</style>

<body>

   <h1 align="center">Minolovec</h1>

   <h2>
    Navodila
   </h2>

    <p>
       Cilj igre je odkriti vsa polja, ki ne vsebujejo mine. <br>
       Če hočeš polje odkriti, vpiši vrstico, nato pa še stolpec v katerem se polje nahaja. Loči ju s presledkom!(Primer: 1 3). <br>
       Če hočeš postaviti zastavico, moraš na koncu dodati še f, ki naj bo tudi ločen s presledkom. (Primer: 1 3 f) <br>
       Pred začetkom igre določi velikost kvadratnega polja na katerem želiš igrati, tako da vpišeš dolžino stranice kvadrata. <br>
       Izbereš lahko tudi število min.
    </p>
    <p>
        Vpiši velikost polja, nato pa število min. Števili loči s presledkom (Primer: 9 10):
        <form action="/igra/" method="post">
            <input type="text" name="velikost_mine">
            <input type="submit" value="Nova igra">
        </form>
        
    </p>
</body>

</html>
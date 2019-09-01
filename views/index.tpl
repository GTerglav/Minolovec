<!DOCTYPE html>
<html>

<body>

   <h1 align="center">Minolovec</h1>

   <p>
    Minolovec je najboljša igra za preganjanje dolgčasa (poleg tetrisa).
   </p>

    <p>
       Cilj igre je odkriti vsa polja, ki ne vsebujejo mine.
    </p>
    <p>
        Če hočeš polje odkriti, vpiši vrstico, nato pa še stolpec v katerem se polje nahaja. Loči ju s presledkom!(Primer: 1 3)
    </p>
    <p>
        Če hočeš postaviti zastavico, moraš na koncu dodati še f, ki naj bo tudi ločen s presledkom. (Primer: 1 3 f)
    </p>
       
    <!-- <img src="img10.png"> -->
    <p>
        Pred začetkom igre določi velikost kvadratnega polja na katerem želiš igrati, tako da vpišeš dolžino stranice kvadrata.
        Izbereš lahko tudi število min.
    </p>
    <p>
        Vpiši velikost polja, nato pa število min. Števili loči s presledkom:
        <form action="/igra/" method="post">
            <input type="text" name="velikost_mine">
            <input type="submit" value="Nova igra">
        </form>
        
    </p>
 <!--   <p>
        Vpiši število min:
        <input type="text" name="mine">
        <input type="submit" value="izberi">
        
    </p>
    


  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form> -->
</body>

</html>
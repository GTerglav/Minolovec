% import model


<!DOCTYPE html>
<html>

<body>

  <h1 align="center">Minolovec</h1>

  <table align="center">
    <tr>
        
      <td>
          
% if igra == "F":
    <p>
        Verjetno si se zatipkal. Poskusi ponovno:
    </p>    
    <form action="/igra/" method="post">
      <input type="text" name="velikost_mine">
      <input type="submit" value="Nova igra">
    </form>  
   

                
% else: 
          <pre>
{{  model.izpis_igre(igra) }}                           
          </pre>
      </td>    
    </tr>

    % if poskus == model.ZMAGA: 
    <tr>
        <td align="center">
            <p>
                Čestitamo, zmagali ste!
            </p>
            <form action="/igra/" method="post">
              <input type="text" name="velikost_mine">
              <input type="submit" value="Nova igra">
          </form>
        </td>
      </tr>
    
    
    
    
    % elif poskus == model.PORAZ:
    <tr>
      <td align="center">
          <p>
              Ha, ha, razneslo te je!
          </p>
          <form action="/igra/" method="post">
            <input type="text" name="velikost_mine">
            <input type="submit" value="Nova igra">
        </form>
      </td>
    </tr>

    %else:
    <tr>
        <td align="center">         
              {{ model.ostale(igra, mine) }}                 
        </td>
    </tr>

    <tr>
      <td align="center">
          <form action="/igra/{{id_igre}}/" method="post">
            <input type="text" name="poskus">
            <input type="submit" value="ugibaj">
      </td>
    </tr>    
    %end
  </table>

  


  
</body>

</html>
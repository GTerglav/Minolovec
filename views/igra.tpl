% import model


<!DOCTYPE html>
<html>

<body>

  <h1 align="center">Minolovec</h1>

  <table align="center">
    <tr>
        
      <td>
          <pre>
% if igra == "F": 
{{"Verjetno si se zatipkal. Poskusi ponovno"}} 
<form action="/igra/" method="post">
  <input type="text" name="velikost_mine">
  <input type="submit" value="Nova igra">
</form>  
              
% else: 
{{  model.izpis_igre(igra) }}                           
          </pre>
      </td>    
    </tr>

    % if poskus == model.ZMAGA: 
    <tr>
        <td align="center">
            <p>
                Čestitamo, pravilno ste rešili polje!
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
              Ha ha, idiot, razneslo te je!
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
          <form action="/igra/{{id_igre}}/" method="post">
            <input type="text" name="poskus">
            <input type="submit" value="ugibaj">
      </td>
      <td>
        {{ model.ostale(igra, mine) }}
      </td>
      
    </tr>

    %end

    
  </table>

  


  
</body>

</html>
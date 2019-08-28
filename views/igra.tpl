% import model
<!DOCTYPE html>
<html>

<body>

  <h1>Minolovec</h1>

  <table>
    <tr>
      <td>
          {{ model.izpis_igre(igra) }}
      </td>
    </tr>

</table>

  


  
</body>

</html>





 <!--      <tr>
      <td>
          Nepravilne crke: {{ igra.nepravilni_ugibi() }}
      </td>
    </tr>

    % if poskus == model.ZMAGA or poskus == model.PORAZ:
      <form action="/igra/" method="post">
        <button type="submit">Nova igra</button>
      </form>


    %else:
    <tr>
      <form action="/igra/{{id_igre}}/" method="post">
      <input type="text" name="poskus">
      <input type="submit" value="ugibaj">
    </tr>

    %end
    <tr>
      <td>
          <img src="img/10.jpg" alt="Obesanje:">
      </td>
    </tr>
    
  </table>

  


  
</body>

</html>-->
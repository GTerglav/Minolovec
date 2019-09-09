% import model


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
  }

  td {
    width: 50%;
    font-family: 'Courier New', Courier, monospace;
    text-align: center;
    align: center
  }

  pre {
    border-style: solid;
    border-width: 2px;
    padding-top: 25px; 
  }
  p {
    font-family: verdana;
    text
  }
  input[type=text], select {
    width: 20%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
  }

  input[type=submit] {
    width: 25%;
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
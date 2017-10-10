var counter = 0;
var limit = 10;
function addInput(divName){
     if (counter == limit)  {
          alert("Você atingiu o limite de Ordens de " + counter + " Ordens Serviço por Plano de Manutenção!");
     }
     else {
          var newdiv = document.createElement('div');
          // newdiv.innerHTML = "Ordem de Serviço " + (counter + 1) + " <br><input type='text' name='myInputs[]'>";
          newdiv.innerHTML = "<h4> Ordem de Serviço " + (counter + 1) + "</h3><br>\
          <div class='container'>\
          <div class='form-group'>\
            <label class='control-label col-sm-2' for='email'>CAMPO A: </label>\
            <div class='col-sm-10'>\
              <input type='text' class='form-control' id='email'>\
            </div>\
          </div>\
          <div class='form-group'>\
            <label class='control-label col-sm-2' for='email'>CAMPO B: </label>\
            <div class='col-sm-10'>\
              <input type='text' class='form-control' id='email'>\
            </div>\
          </div>\
          <div class='form-group'>\
            <label class='control-label col-sm-2' for='email'>CAMPO C: </label>\
            <div class='col-sm-10'>\
              <input type='text' class='form-control' id='email'>\
            </div>\
          </div>\
          <div class='form-group'>\
            <label class='control-label col-sm-2' for='email'>CAMPO D: </label>\
            <div class='col-sm-10'>\
              <input type='text' class='form-control' id='email'>\
            </div>\
          </div>\
          <div class='form-group'>\
            <label class='control-label col-sm-2' for='email'>CAMPO E: </label>\
            <div class='col-sm-10'>\
              <input type='text' class='form-control' id='email'>\
            </div>\
          </div>\
          </div>";
          document.getElementById(divName).appendChild(newdiv);
          counter++;
     }
}

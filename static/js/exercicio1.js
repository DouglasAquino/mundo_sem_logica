var respostas = document.querySelectorAll(".celula-resposta");
var caixa = document.querySelector(".caixa-final");
function verificarRespostas(){
    pontos=0;
    resp=['0','1','0','0','1','0','0','0','1']
    for(let i=0;i<respostas.length;i++){
        var select = respostas[i].childNodes[1];
        var valor = select.options[select.selectedIndex].value;
        if(valor == resp[i]){
            pontos++;
        }
    }
    return pontos;
    
}
function salvar(pontos){
    let id = document.querySelector("#id-exercicio");
    window.location.href = "/Salvar/"+id.textContent+"/"+pontos;
}

function salvarPontos(){
    salvar(verificarRespostas())
}
function enviarRespostas(){
    var pontos = verificarRespostas();
    var msg = caixa.querySelector("#titulo");
    msg.textContent = "você acertou "+pontos+"/9";
    caixa.hidden = false;
}

function fechar(){
    caixa.hidden = true;
}


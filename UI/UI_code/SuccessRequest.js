

function successRecipents(dataReq, pagination){
    const table = document.querySelector('#recipientsList');
    table.innerHTML =""
    pagination.numPages= dataReq.pages
    console.log("data req",dataReq)
    for (let a of dataReq.data) {
        let reci= `<tr>
                    <td>${a["name"]}</td>
                    <td>${a["info"]}</td>
                    <td>${a["recipe"]["Details"]}</td>
                   </tr>`;

        table.innerHTML += reci;
        // for (let com of a["recipe"]["components"]) {
        //     reci += com + "<br/>"
        // }
        // reci += "<br/>" + "recipe: The order- " + a["recipe"]["order"] +"<br/>" +
        //     "Link to the website: " + a["link"] + "<br/>"
        // recipients += reci + "<br/>"
    }
    $('#recipientsList').show();
}


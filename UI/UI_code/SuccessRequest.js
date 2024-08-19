
function success_info(dataReq){
    const cards = document.getElementById("dataOfObject");
    cards.innerHTML ="";
    let i= 0;
    for (let a of dataReq) {
        items.push(a);
        let fruit_name= localStorage.getItem("currentFruit");

        let oneInfo= `<div class="card flip-card">
                        <div class="flip-card-inner">
                            <div class="flip-card-front">
                                <h1><b>${a["name"]}</b></h1>
                            </div>
                            <div class="flip-card-back">
                                <p>${fruit_name}</p>
                                <div class="textHide">
                                    <p>מידע כללי:</p>
                                    <p>${a["info"]}</p>
                                    <p>מידע תזונתי</p>
                                    <p>${a["Details"]}</p>
                                </div>
                                <p>
                                    <button onclick="orderInfoModal('${i}')" class="card-button" data-toggle="modal" data-target="#myModal">More...</button>
                                </p>
                            </div>
                        </div>
                    </div>`;
        cards.innerHTML += oneInfo;
        i++;
    }

    $('#dataOfObject').show();

}

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
function success_CosharotInfo(dataReq){
    console.log("data req", dataReq)
    const table = document.querySelector('#cosharot');
    pagination.size= dataReq.pages
    for (let item of dataReq) {
        let reci= `<tr>
                     <td>${item["name"]}</td>
                     <td>${item["text"]}</td>
                     <td>
                        <a title="Go visit the web source!" href="${item["link"]}">link</a>
                     </td>
                   </tr>`;

        table.innerHTML += reci;
    }
    $('#cosharot').html(`<span
                style="color: darkmagenta;font-weight: bolder;">${info}</span>`);
    $('#cosharot').show();
}


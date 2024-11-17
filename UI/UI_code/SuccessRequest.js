

function successRecipents(dataReq, pagination){
    const table = document.querySelector('#recipientsList');
    table.innerHTML =`<tr>
                        <th>Name</th>
                        <th>Information</th>
                        <th>More deatails</th>
                        <th>Link</th>
                      </tr>`
    pagination.numPages= dataReq.pages
    cratePagination(pagination.page)
    console.log("data req",dataReq)
    for (let a of dataReq.data) {
        let reci= `<tr data-toggle="modal" data-target="#myModal" onclick= "getOneRecipient(${a["index"]})">
                    <td>${a["name"]}</td>
                    <td>${a["info"]}</td>
                    <td>${a["recipe"]["Details"]}</td>
                    <td>
                        <a title="Go visit the web source!" href="${a["link"]}">link</a>
                    </td>
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

function cratePagination(currentPage){
    let pages = document.querySelector('#paginationSelector');
    let activ='';
    let localSize = pagination.size
    let i = (currentPage-2)>1? (currentPage-2): 1;
    console.log("this is i", i)
    if(currentPage>1) {
        pages.innerHTML = `<li class="page-item"><a class="page-link" onclick="changeDataPage(` + 1 + `,`+localSize+`)">first</a></li>`;
        pages.innerHTML += `<li class="page-item"><a class="page-link" onclick="changeDataPage(` + (currentPage - 1) + `,`+ localSize+`)">&laquo;</a></li>`;
    } else
        pages.innerHTML =''
    console.log("current page", currentPage)
    while (i<=(currentPage+2) && i<=pagination.numPages){
        if(i==currentPage){
            activ ="active"
        }
        else
            activ='';
        pages.innerHTML += `<li class="page-item `+ activ+`"><a class="page-link" onclick="changeDataPage(`+i+`,` +localSize+`)" >`+i+`</a></li>`
        i++;
    }
    if(currentPage<pagination.numPages)
        pages.innerHTML += `<li class="page-item"><a class="page-link" onclick="changeDataPage(`+(currentPage+1)+`,`+ localSize+`)">&raquo;</a></li>`
}


